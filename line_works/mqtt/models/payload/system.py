import json
from typing import Any, List, Literal, Optional

from pydantic import BaseModel, Field

from line_works.mqtt.enums.control_packet_type import ControlPacketType
from line_works.mqtt.models.payload._base import BasePayload


class User(BaseModel):
    id: int
    name: str
    domain_id: int = Field(alias="domainId")


class Leaver(User):
    reason: str


class KickedUser(User):
    reason: str


class JoinExtras(BaseModel):
    active_user_list: List[User] = Field(alias="activeUserList")
    title: str


class LeaveExtras(BaseModel):
    away_user_list: List[Leaver] = Field(alias="awayUserList")


class MessageBody(BaseModel):
    class Config:
        populate_by_name = True

    msg_sn: int = Field(alias="msgSn")
    msg_type_code: int = Field(alias="msgTypeCode")
    uid: str
    uno: int
    bot_no: int = Field(alias="botNo")
    msg: str = ""
    mbr_cnt: int = Field(alias="mbrCnt")
    ctime: int
    utime: int
    extras: str = ""
    preview_data: str = Field(alias="previewData", default="")
    msg_tid: int = Field(alias="msgTid")
    msg_status_type: str = Field(alias="msgStatusType")
    writer_info: dict = Field(alias="writerInfo", default_factory=dict)


class KickedBody(BaseModel):
    kicked_user: KickedUser = Field(alias="kickedUser")

    class Config:
        populate_by_name = True


class RelayData(BaseModel):
    ver: str
    cmd: int
    bdy: dict[str, Any]
    msg_tid: Optional[int] = Field(alias="msgTid", default=None)
    msg_status_type: Optional[str] = Field(alias="msgStatusType", default=None)

    class Config:
        populate_by_name = True


class SessionInfo(BaseModel):
    type: str
    tid: str


class SystemPayload(BasePayload):
    session_info: SessionInfo = Field(alias="sessionInfo")
    svcid: Literal["works"]
    cid: str
    relay_data_list: List[RelayData] = Field(alias="relayDataList")
    autolang: Optional[str] = None

    class Config:
        populate_by_name = True

    @property
    def cmd(self) -> int:
        return self.relay_data_list[0].cmd

    @property
    def _bdy(self) -> dict[str, Any]:
        return self.relay_data_list[0].bdy

    @property
    def body(self) -> "JoinLeaveBody | BotKickedBody":
        if self.cmd in (ControlPacketType.JOIN, ControlPacketType.QUIT):
            return JoinLeaveBody.model_validate(self._bdy)
        elif self.cmd == ControlPacketType.BOT_KICKED:
            return BotKickedBody.model_validate(self._bdy)
        raise ValueError(f"Unknown system command: {self.cmd}")

    @property
    def unique_id(self) -> str:
        """Generate unique id using loc_key and message TID.

        For JOIN / QUIT  : msgTid is inside body.
        For BOT_KICKED   : msgTid is in the RelayData item.
        """
        msg_tid: Optional[int] = None
        if hasattr(self.body, "msg_tid"):
            msg_tid = getattr(self.body, "msg_tid")
        if msg_tid is None:
            msg_tid = self.relay_data_list[0].msg_tid
        return f"{self.loc_key}_{msg_tid}"


class JoinLeaveBody(MessageBody):
    pass


class BotKickedBody(KickedBody):
    pass


class UserJoinLeavePayload(SystemPayload):
    cmd: Literal[ControlPacketType.JOIN, ControlPacketType.QUIT]

    @property
    def body(self) -> JoinLeaveBody:
        body = super().body
        if not isinstance(body, JoinLeaveBody):
            raise TypeError(
                f"Expected JoinLeaveBody, but got {type(body).__name__}"
            )
        return body

    @property
    def extras_dict(self) -> dict[str, Any]:
        return json.loads(self.body.extras)

    @property
    def join_info(self) -> JoinExtras:
        return JoinExtras.model_validate(self.extras_dict)

    @property
    def leave_info(self) -> LeaveExtras:
        return LeaveExtras.model_validate(self.extras_dict)


class BotKickedPayload(SystemPayload):
    cmd: Literal[ControlPacketType.BOT_KICKED]

    @property
    def body(self) -> BotKickedBody:
        body = super().body
        if not isinstance(body, BotKickedBody):
            raise TypeError(
                f"Expected BotKickedBody, but got {type(body).__name__}"
            )
        return body
