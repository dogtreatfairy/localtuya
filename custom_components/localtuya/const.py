"""Constants for localtuya integration."""

DOMAIN = "localtuya"

DATA_DISCOVERY = "discovery"
DATA_CLOUD = "cloud_data"

# Platforms in this list must support config flows
PLATFORMS = [
    "binary_sensor",
    "climate",
    "cover",
    "fan",
    "light",
    "number",
    "select",
    "sensor",
    "switch",
    "vacuum",
]

TUYA_DEVICES = "tuya_devices"

ATTR_CURRENT = "current"
ATTR_CURRENT_CONSUMPTION = "current_consumption"
ATTR_VOLTAGE = "voltage"
ATTR_UPDATED_AT = "updated_at"

# config flow
CONF_LOCAL_KEY = "local_key"
CONF_ENABLE_DEBUG = "enable_debug"
CONF_PROTOCOL_VERSION = "protocol_version"
CONF_DPS_STRINGS = "dps_strings"
CONF_MODEL = "model"
CONF_PRODUCT_KEY = "product_key"
CONF_PRODUCT_NAME = "product_name"
CONF_USER_ID = "user_id"
CONF_ENABLE_ADD_ENTITIES = "add_entities"


CONF_ACTION = "action"
CONF_ADD_DEVICE = "add_device"
CONF_EDIT_DEVICE = "edit_device"
CONF_SETUP_CLOUD = "setup_cloud"
CONF_NO_CLOUD = "no_cloud"
CONF_MANUAL_DPS = "manual_dps_strings"
CONF_DEFAULT_VALUE = "dps_default_value"
CONF_RESET_DPIDS = "reset_dpids"
CONF_PASSIVE_ENTITY = "is_passive_entity"

# light
CONF_BRIGHTNESS_LOWER = "brightness_lower"
CONF_BRIGHTNESS_UPPER = "brightness_upper"
CONF_COLOR = "color"
CONF_COLOR_MODE = "color_mode"
CONF_COLOR_MODE_SET = "color_mode_set"
CONF_COLOR_TEMP_MIN_KELVIN = "color_temp_min_kelvin"
CONF_COLOR_TEMP_MAX_KELVIN = "color_temp_max_kelvin"
CONF_COLOR_TEMP_REVERSE = "color_temp_reverse"
CONF_MUSIC_MODE = "music_mode"

# switch
CONF_CURRENT = "current"
CONF_CURRENT_CONSUMPTION = "current_consumption"
CONF_VOLTAGE = "voltage"

# cover
CONF_COMMANDS_SET = "commands_set"
CONF_POSITIONING_MODE = "positioning_mode"
CONF_CURRENT_POSITION_DP = "current_position_dp"
CONF_SET_POSITION_DP = "set_position_dp"
CONF_POSITION_INVERTED = "position_inverted"
CONF_SPAN_TIME = "span_time"

# fan
CONF_FAN_SPEED_CONTROL = "fan_speed_control"
CONF_FAN_OSCILLATING_CONTROL = "fan_oscillating_control"
CONF_FAN_SPEED_MIN = "fan_speed_min"
CONF_FAN_SPEED_MAX = "fan_speed_max"
CONF_FAN_ORDERED_LIST = "fan_speed_ordered_list"
CONF_FAN_DIRECTION = "fan_direction"
CONF_FAN_DIRECTION_FWD = "fan_direction_forward"
CONF_FAN_DIRECTION_REV = "fan_direction_reverse"
CONF_FAN_DPS_TYPE = "fan_dps_type"

# sensor
CONF_SCALING = "scaling"

# climate
CONF_TARGET_TEMPERATURE_DP = "target_temperature_dp"
CONF_CURRENT_TEMPERATURE_DP = "current_temperature_dp"
CONF_TEMPERATURE_STEP = "temperature_step"
CONF_MAX_TEMP_DP = "max_temperature_dp"
CONF_MIN_TEMP_DP = "min_temperature_dp"
CONF_TEMP_MAX = "max_temperature_const"
CONF_TEMP_MIN = "min_temperature_const"
CONF_PRECISION = "precision"
CONF_TARGET_PRECISION = "target_precision"
CONF_HVAC_MODE_DP = "hvac_mode_dp"
CONF_HVAC_MODE_SET = "hvac_mode_set"
CONF_HVAC_FAN_MODE_DP = "hvac_fan_mode_dp"
CONF_HVAC_FAN_MODE_SET = "hvac_fan_mode_set"
CONF_HVAC_SWING_MODE_DP = "hvac_swing_mode_dp"
CONF_HVAC_SWING_MODE_SET = "hvac_swing_mode_set"
CONF_PRESET_DP = "preset_dp"
CONF_PRESET_SET = "preset_set"
CONF_HEURISTIC_ACTION = "heuristic_action"
CONF_HVAC_ACTION_DP = "hvac_action_dp"
CONF_HVAC_ACTION_SET = "hvac_action_set"
CONF_ECO_DP = "eco_dp"
CONF_ECO_VALUE = "eco_value"

# vacuum
CONF_POWERGO_DP = "powergo_dp"
CONF_IDLE_STATUS_VALUE = "idle_status_value"
CONF_RETURNING_STATUS_VALUE = "returning_status_value"
CONF_DOCKED_STATUS_VALUE = "docked_status_value"
CONF_BATTERY_DP = "battery_dp"
CONF_MODE_DP = "mode_dp"
CONF_MODES = "modes"
CONF_FAN_SPEED_DP = "fan_speed_dp"
CONF_FAN_SPEEDS = "fan_speeds"
CONF_CLEAN_TIME_DP = "clean_time_dp"
CONF_CLEAN_AREA_DP = "clean_area_dp"
CONF_CLEAN_RECORD_DP = "clean_record_dp"
CONF_LOCATE_DP = "locate_dp"
CONF_FAULT_DP = "fault_dp"
CONF_PAUSED_STATE = "paused_state"
CONF_RETURN_MODE = "return_mode"
CONF_STOP_STATUS = "stop_status"

# number
CONF_MIN_VALUE = "min_value"
CONF_MAX_VALUE = "max_value"
CONF_STEPSIZE_VALUE = "step_size"

# select
CONF_OPTIONS = "select_options"
CONF_OPTIONS_FRIENDLY = "select_options_friendly"

# States
ATTR_STATE = "raw_state"
CONF_RESTORE_ON_RECONNECT = "restore_on_reconnect"

KNOWN_DEVICES = {
    "lsbkqogj5ztove0f": {
        # Device dp_id assignments:
        # 20: Master Switch (overall power toggle)
        # 21: Not Used
        # 22: Star Brightness (dimming control, min 10-max 1000; combined with 63 for Star light entity)
        # 26: Timer (countdown in seconds, 0-86400 with 60s steps)
        # 28: Not Used
        # 53: Meteor (toggle for meteor effect)
        # 60: Rotation (on/off for rotation; combined with 62 for Rotation light entity)
        # 62: Rotation Speed (speed adjustment 1-100, treated as brightness in Rotation light)
        # 63: Star (on/off for stars; combined with 22 for Star light entity)
        "name": "Orzors Lite Plus Star Projector",
        "category": "xktyd",
        "entities": [
            {
                "platform": "switch",
                "friendly_name": "Orzors Master Switch",
                "id": 20,
                "state_on": True,
                "state_off": False,
            },
            {
                "platform": "switch",
                "friendly_name": "Orzors Meteor",
                "id": 53,
                "state_on": True,
                "state_off": False,
            },
            {
                "platform": "light",
                "friendly_name": "Orzors Star",
                "id": 63,
                "brightness": 22,
                "brightness_lower": 10,
                "brightness_upper": 1000,
                "music_mode": False,
                "color_temp_reverse": False,
                "color_temp_min_kelvin": 2700,
                "color_temp_max_kelvin": 6500,
            },
            {
                "platform": "light",
                "friendly_name": "Orzors Rotation",
                "id": 60,
                "brightness": 62,
                "brightness_lower": 1,
                "brightness_upper": 100,
                "music_mode": False,
                "color_temp_reverse": False,
                "color_temp_min_kelvin": 2700,
                "color_temp_max_kelvin": 6500,
            },
            {
                "platform": "number",
                "friendly_name": "Orzors Timer",
                "id": 26,
                "min_value": 0,
                "max_value": 86400,
                "step_size": 60,
            },
        ],
    },
    "kuskdnpwgso1qinx": {
        # Device dp_id assignments:
        # 1: Power (fan on/off; combined with 3 and 5 for main fan entity)
        # 2: Mode (select 0/Normal, 1/Natural, 2/Sleep, 3/Auto)
        # 3: Speed (fan speed levels 1-5; combined with 1 for main fan entity)
        # 5: Oscillation (toggle; combined with 1 for main fan entity)
        # 13: Mute (toggle for silent mode)
        # 15: Backlight (toggle for display)
        # 21: Temperature (sensor in °F)
        # 22: Timer (select "1h" to "12h" only; values must be exactly "1h", "2h", etc.)
        "name": "OmniBreeze Tower Fan-5M-F",
        "category": "fs",
        "entities": [
            {
                "platform": "fan",
                "friendly_name": "OmniBreeze Tower Fan",
                "id": 1,
                "fan_speed_control": 3,
                "fan_speed_min": 1,
                "fan_speed_max": 5,
                "fan_dps_type": "int",
                "fan_oscillating_control": 5,
                "fan_direction": None,
                "fan_speed_ordered_list": "disabled",
            },
            {
                "platform": "select",
                "friendly_name": "OmniBreeze Mode",
                "id": 2,
                "select_options": "0;1;2;3",
                "select_options_friendly": "Normal;Natural;Sleep;Auto",
            },
            {
                "platform": "switch",
                "friendly_name": "OmniBreeze Mute",
                "id": 13,
                "state_on": False,
                "state_off": True,
            },
            {
                "platform": "switch",
                "friendly_name": "OmniBreeze Backlight",
                "id": 15,
                "state_on": True,
                "state_off": False,
            },
            {
                "platform": "sensor",
                "friendly_name": "OmniBreeze Temperature",
                "id": 21,
                "device_class": "temperature",
                "unit_of_measurement": "°F",
            },
            {
                "platform": "select",
                "friendly_name": "OmniBreeze Timer",
                "id": 22,
                "select_options": "1h;2h;3h;4h;5h;6h;7h;8h;9h;10h;11h;12h",
                "select_options_friendly": "1h;2h;3h;4h;5h;6h;7h;8h;9h;10h;11h;12h",
            },
        ],
    },
}