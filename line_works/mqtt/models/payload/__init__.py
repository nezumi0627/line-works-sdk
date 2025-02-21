from typing import Type

from line_works.mqtt.enums.notification_type import NotificationType
from line_works.mqtt.models.payload.badge import BadgePayload
from line_works.mqtt.models.payload.message import MessagePayload
from line_works.mqtt.models.payload.service import ServicePayload

PayloadTypes = MessagePayload | ServicePayload | BadgePayload

NOTIFICATION_TYPE_MODEL_MAPPING: dict[int, Type[PayloadTypes]] = {
    NotificationType.NOTIFICATION_UNKNOWN: 0,
    NotificationType.NOTIFICATION_MESSAGE: 1,
    NotificationType.NOTIFICATION_CONTACT: 3,
    NotificationType.NOTIFICATION_LOCATION: 4,
    NotificationType.NOTIFICATION_BOT: 5,
    NotificationType.NOTIFICATION_OFFICIAL: 6,
    NotificationType.NOTIFICATION_CHANNELNOTI: 7,
    NotificationType.NOTIFICATION_RICH: 8,
    NotificationType.NOTIFICATION_NEW_RICH: 10,
    NotificationType.NOTIFICATION_IMAGE: 11,
    NotificationType.NOTIFICATION_AUDIO: 12,
    NotificationType.NOTIFICATION_RECORD: 13,
    NotificationType.NOTIFICATION_VIDEO: 14,
    NotificationType.NOTIFICATION_STICKER_OLD: 15,
    NotificationType.NOTIFICATION_STICKER_V3: 18,
    NotificationType.NOTIFICATION_FILE: 16,
    NotificationType.NOTIFICATION_LOCATION_EMOJI: 27,
    NotificationType.NOTIFICATION_CALL: 31,
    NotificationType.NOTIFICATION_VCALL: 32,
    NotificationType.NOTIFICATION_INVITE_DSSHARE: 34,
    NotificationType.NOTIFICATION_STOP_DSSHARE: 35,
    NotificationType.NOTIFICATION_CANCEL_CALL: 33,
    NotificationType.NOTIFICATION_NEW_MAIL: 40,
    NotificationType.NOTIFICATION_BADGE: 41,
    NotificationType.NOTIFICATION_CAL_SCHD_REMIND: 50,
    NotificationType.NOTIFICATION_CAL_TASK_REMIND: 51,
    NotificationType.NOTIFICATION_CAL_APPO_INVITE: 52,
    NotificationType.NOTIFICATION_CAL_APPO_UPDATE: 53,
    NotificationType.NOTIFICATION_CAL_APPO_CANCEL: 54,
    NotificationType.NOTIFICATION_API_EXEC_COMMAND: 61,
    NotificationType.NOTIFICATION_SERVICE: 100,

    # 現在V3が使われているようなので、18をNOTIFICATION_STICKERとして定義
    NotificationType.NOTIFICATION_STICKER: 18
}
