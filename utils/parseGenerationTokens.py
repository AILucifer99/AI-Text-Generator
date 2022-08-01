def GenerationTokenSynthesizer(parse, limit_1, limit_2, generation_seed):
    import random
    import math
    if parse:
        L1 = random.choice([random.randint(limit_1, limit_2) for _ in range(generation_seed)])
        return L1
    else:
        return math.ceil((limit_2 / 10) + limit_1)
