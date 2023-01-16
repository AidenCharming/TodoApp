solid = 0
gas = 100


def state(temperature):
    if temperature <= solid:
        return "Solid"
    elif solid < temperature < gas:
        return "Liquid"
    else:
        return "Gas"
