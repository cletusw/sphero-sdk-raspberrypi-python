from numpy import interp

async def drive(x, y, z, rz, rvr, MIN_SPEED, MAX_SPEED, DEADBAND_RADIUS, MAX_MAGNITUDE):
    def normalize(value, minNormalizedMagnitude, maxNormalizedMagnitude):
        isPositive = True
        if value < 0:
            value = -value
            isPositive = False

        if value < DEADBAND_RADIUS:
            return 0

        normalizedValue = int(interp(
            value,
            [DEADBAND_RADIUS, MAX_MAGNITUDE],
            [minNormalizedMagnitude, maxNormalizedMagnitude]
        ))

        return normalizedValue if isPositive else -normalizedValue

    linear_velocity = -normalize(y, MIN_SPEED, MAX_SPEED)

    # Calculate max angular speed that decreases as linear speed increases
    linear_speed = abs(linear_velocity)
    max_angular_speed = int(MAX_SPEED * interp(
        linear_speed,
        [0, MAX_SPEED],
        [0.7, 0.4],
    ))

    yaw_angular_velocity = -normalize(x, MIN_SPEED, max_angular_speed)
    # print(y, linear_velocity, x, yaw_angular_velocity)

    # Valid linear & angular velocity values are -127..127
    await rvr.drive_rc_normalized(
        linear_velocity = linear_velocity,
        yaw_angular_velocity = yaw_angular_velocity,
        flags = 0,
    )
