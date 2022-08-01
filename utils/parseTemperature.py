def TemperatureSynthesizer(parse):
    import random
    import math
    if parse:
        L1 = random.choice([0.6, 0.65, 0.7, 0.75, 0.8, 0.85])
        return L1
    else:
        return random.choice([0.65, 0.75, 0.85])
