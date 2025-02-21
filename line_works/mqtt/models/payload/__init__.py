from typing import Type

from line_works.mqtt.enums.notification_type import NotificationType
from line_works.mqtt.models.payload.badge import BadgePayload
from line_works.mqtt.models.payload.message import MessagePayload
from line_works.mqtt.models.payload.service import ServicePayload

PayloadTypes = MessagePayload | ServicePayload | BadgePayload

NOTIFICATION_TYPE_MODEL_MAPPING: dict[int, Type[PayloadTypes]] = {
    NotificationType.NOTIFICATION_MESSAGE.value: MessagePayload,
    NotificationType.NOTIFICATION_SERVICE.value: ServicePayload,
    NotificationType.NOTIFICATION_BADGE.value: BadgePayload,
    NotificationType.NOTIFICATION_UNKNOWN.value: MessagePayload,
    NotificationType.NOTIFICATION_MESSAGE.value: MessagePayload,
    NotificationType.NOTIFICATION_CONTACT.value: MessagePayload,
    NotificationType.NOTIFICATION_LOCATION.value: MessagePayload,
    NotificationType.NOTIFICATION_BOT.value: MessagePayload,
    NotificationType.NOTIFICATION_OFFICIAL.value: MessagePayload,
    NotificationType.NOTIFICATION_CHANNELNOTI.value: MessagePayload,
    NotificationType.NOTIFICATION_RICH.value: MessagePayload,
    NotificationType.NOTIFICATION_NEW_RICH.value: MessagePayload,
    NotificationType.NOTIFICATION_IMAGE.value: MessagePayload,
    NotificationType.NOTIFICATION_AUDIO.value: MessagePayload,
    NotificationType.NOTIFICATION_RECORD.value: MessagePayload,
    NotificationType.NOTIFICATION_VIDEO.value: MessagePayload,
    NotificationType.NOTIFICATION_STICKER_OLD.value: MessagePayload,
    NotificationType.NOTIFICATION_STICKER_V3.value: MessagePayload,
    NotificationType.NOTIFICATION_FILE.value: MessagePayload,
    NotificationType.NOTIFICATION_LOCATION_EMOJI.value: MessagePayload,
    NotificationType.NOTIFICATION_CALL.value: MessagePayload,
    NotificationType.NOTIFICATION_VCALL.value: MessagePayload,
    NotificationType.NOTIFICATION_INVITE_DSSHARE.value: MessagePayload,
    NotificationType.NOTIFICATION_STOP_DSSHARE.value: MessagePayload,
    NotificationType.NOTIFICATION_CANCEL_CALL.value: MessagePayload,
    NotificationType.NOTIFICATION_NEW_MAIL.value: MessagePayload,
    NotificationType.NOTIFICATION_BADGE.value: MessagePayload,
    NotificationType.NOTIFICATION_CAL_SCHD_REMIND.value: MessagePayload,
    NotificationType.NOTIFICATION_CAL_TASK_REMIND.value: MessagePayload,
    NotificationType.NOTIFICATION_CAL_APPO_INVITE.value: MessagePayload,
    NotificationType.NOTIFICATION_CAL_APPO_UPDATE.value: MessagePayload,
    NotificationType.NOTIFICATION_CAL_APPO_CANCEL.value: MessagePayload,
    NotificationType.NOTIFICATION_API_EXEC_COMMAND.value: MessagePayload,
    NotificationType.NOTIFICATION_SERVICE.value: ServicePayload,
    # 現在V3が使われているようなので、18をNOTIFICATION_STICKERとして定義
    NotificationType.NOTIFICATION_STICKER.value: MessagePayload,
}
