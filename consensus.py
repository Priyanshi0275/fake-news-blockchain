import random
from reputation import reputation

def select_validator():

    auditors = list(reputation.keys())
    stakes = list(reputation.values())

    validator = random.choices(auditors,weights=stakes,k=1)[0]

    return validator