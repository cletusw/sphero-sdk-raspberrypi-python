#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x18-sensors.json
# Device ID:          0x18
# Device Name:        sensor
# Timestamp:          07/13/2020 @ 20:24:40.444651 (UTC)

from sphero_sdk.common.enums.sensor_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter
from sphero_sdk.common.sequence_number_generator import SequenceNumberGenerator


def enable_gyro_max_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_gyro_max_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='is_enabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_gyro_max_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.gyro_max_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='flags',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def reset_locator_x_and_y(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.reset_locator_x_and_y,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def set_locator_flags(flags, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.set_locator_flags,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='flags',
                data_type='uint8_t',
                index=0,
                value=flags,
                size=1
            ),
        ],
    }


def get_bot_to_bot_infrared_readings(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_bot_to_bot_infrared_readings,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='sensor_data',
                data_type='uint32_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_rgbc_sensor_values(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_rgbc_sensor_values,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='red_channel_value',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='green_channel_value',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='blue_channel_value',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
            Parameter( 
                name='clear_channel_value',
                data_type='uint16_t',
                index=3,
                size=1,
            ),
        ]
    }


def magnetometer_calibrate_to_north(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.magnetometer_calibrate_to_north,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def start_robot_to_robot_infrared_broadcasting(far_code, near_code, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_robot_to_robot_infrared_broadcasting,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='far_code',
                data_type='uint8_t',
                index=0,
                value=far_code,
                size=1
            ),
            Parameter( 
                name='near_code',
                data_type='uint8_t',
                index=1,
                value=near_code,
                size=1
            ),
        ],
    }


def start_robot_to_robot_infrared_following(far_code, near_code, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_robot_to_robot_infrared_following,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='far_code',
                data_type='uint8_t',
                index=0,
                value=far_code,
                size=1
            ),
            Parameter( 
                name='near_code',
                data_type='uint8_t',
                index=1,
                value=near_code,
                size=1
            ),
        ],
    }


def stop_robot_to_robot_infrared_broadcasting(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_robot_to_robot_infrared_broadcasting,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def on_robot_to_robot_infrared_message_received_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.robot_to_robot_infrared_message_received_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='infrared_code',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_ambient_light_sensor_value(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_ambient_light_sensor_value,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='ambient_light_value',
                data_type='float',
                index=0,
                size=1,
            ),
        ]
    }


def stop_robot_to_robot_infrared_following(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_robot_to_robot_infrared_following,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def start_robot_to_robot_infrared_evading(far_code, near_code, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_robot_to_robot_infrared_evading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='far_code',
                data_type='uint8_t',
                index=0,
                value=far_code,
                size=1
            ),
            Parameter( 
                name='near_code',
                data_type='uint8_t',
                index=1,
                value=near_code,
                size=1
            ),
        ],
    }


def stop_robot_to_robot_infrared_evading(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_robot_to_robot_infrared_evading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def enable_color_detection_notify(is_enabled, interval, minimum_confidence_threshold, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_color_detection_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='is_enabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
            Parameter( 
                name='interval',
                data_type='uint16_t',
                index=1,
                value=interval,
                size=1
            ),
            Parameter( 
                name='minimum_confidence_threshold',
                data_type='uint8_t',
                index=2,
                value=minimum_confidence_threshold,
                size=1
            ),
        ],
    }


def on_color_detection_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.color_detection_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='red',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='green',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='blue',
                data_type='uint8_t',
                index=2,
                size=1,
            ),
            Parameter( 
                name='confidence',
                data_type='uint8_t',
                index=3,
                size=1,
            ),
            Parameter( 
                name='color_classification_id',
                data_type='uint8_t',
                index=4,
                size=1,
            ),
        ]
    }


def get_current_detected_color_reading(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_current_detected_color_reading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def enable_color_detection(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_color_detection,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='is_enabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def configure_streaming_service(token, configuration, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.configure_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='token',
                data_type='uint8_t',
                index=0,
                value=token,
                size=1
            ),
            Parameter( 
                name='configuration',
                data_type='uint8_t',
                index=1,
                value=configuration,
                size=15
            ),
        ],
    }


def start_streaming_service(period, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='period',
                data_type='uint16_t',
                index=0,
                value=period,
                size=1
            ),
        ],
    }


def stop_streaming_service(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def clear_streaming_service(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.clear_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def on_streaming_service_data_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.streaming_service_data_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='token',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='sensor_data',
                data_type='uint8_t',
                index=1,
                size=9999,
            ),
        ]
    }


def enable_robot_infrared_message_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_robot_infrared_message_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='is_enabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def send_infrared_message(infrared_code, front_strength, left_strength, right_strength, rear_strength, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.send_infrared_message,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='infrared_code',
                data_type='uint8_t',
                index=0,
                value=infrared_code,
                size=1
            ),
            Parameter( 
                name='front_strength',
                data_type='uint8_t',
                index=1,
                value=front_strength,
                size=1
            ),
            Parameter( 
                name='left_strength',
                data_type='uint8_t',
                index=2,
                value=left_strength,
                size=1
            ),
            Parameter( 
                name='right_strength',
                data_type='uint8_t',
                index=3,
                value=right_strength,
                size=1
            ),
            Parameter( 
                name='rear_strength',
                data_type='uint8_t',
                index=4,
                value=rear_strength,
                size=1
            ),
        ],
    }


def get_temperature(id0, id1, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_temperature,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='id0',
                data_type='uint8_t',
                index=0,
                value=id0,
                size=1
            ),
            Parameter( 
                name='id1',
                data_type='uint8_t',
                index=1,
                value=id1,
                size=1
            ),
        ],
        'outputs': [ 
            Parameter( 
                name='id0',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='temp0',
                data_type='float',
                index=1,
                size=1,
            ),
            Parameter( 
                name='id1',
                data_type='uint8_t',
                index=2,
                size=1,
            ),
            Parameter( 
                name='temp1',
                data_type='float',
                index=3,
                size=1,
            ),
        ]
    }


def get_motor_thermal_protection_status(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_motor_thermal_protection_status,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='left_motor_temperature',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter( 
                name='left_motor_status',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='right_motor_temperature',
                data_type='float',
                index=2,
                size=1,
            ),
            Parameter( 
                name='right_motor_status',
                data_type='uint8_t',
                index=3,
                size=1,
            ),
        ]
    }


def enable_motor_thermal_protection_status_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_motor_thermal_protection_status_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='is_enabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_motor_thermal_protection_status_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.motor_thermal_protection_status_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='left_motor_temperature',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter( 
                name='left_motor_status',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='right_motor_temperature',
                data_type='float',
                index=2,
                size=1,
            ),
            Parameter( 
                name='right_motor_status',
                data_type='uint8_t',
                index=3,
                size=1,
            ),
        ]
    }


def on_magnetometer_calibration_complete_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.magnetometer_calibration_complete_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='is_successful',
                data_type='bool',
                index=0,
                size=1,
            ),
            Parameter( 
                name='yaw_north_direction',
                data_type='int16_t',
                index=1,
                size=1,
            ),
        ]
    }


def get_magnetometer_reading(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_magnetometer_reading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='x_axis',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter( 
                name='y_axis',
                data_type='float',
                index=1,
                size=1,
            ),
            Parameter( 
                name='z_axis',
                data_type='float',
                index=2,
                size=1,
            ),
        ]
    }


def get_encoder_counts(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_encoder_counts,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='encoder_counts',
                data_type='int32_t',
                index=0,
                size=2,
            ),
        ]
    }


def disable_notifications_and_active_commands(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.disable_notifications_and_active_commands,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }
