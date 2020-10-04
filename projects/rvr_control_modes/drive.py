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

    # print(y, normalize(y), z, normalize(z))

    # Valid linear & angular velocity values are -127..127
    await rvr.drive_rc_normalized(
        linear_velocity = -normalize(y, MIN_SPEED, MAX_SPEED),
        yaw_angular_velocity = -normalize(z, MIN_SPEED, MAX_SPEED),
        flags = 0,
    )
