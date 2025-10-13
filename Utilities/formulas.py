# A module that contains formula functions for use in the rest of the code.

def health_increase(old_health: int, levels: int) -> int:

    return old_health + (5 * levels)

def strength_increase(old_strength: int, levels: int) -> int:

    return old_strength + (1 * levels)