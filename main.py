from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    # === TODO ===
    return set(mapping.keys())
    # === END TODO ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    # === TODO ===
    return set(mapping.values())
    # === END TODO ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    # === TODO ===
    return len(get_range(mapping)-target) == 0
    # === END TODO ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    # === TODO ===
    return len(get_domain(mapping)) == len(get_range(mapping))
    # === END TODO ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    # === TODO ===
    return get_range(mapping) == target
    # === END TODO ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    # === TODO ===
    return is_injective(mapping) and is_surjective(mapping,target)
    # === END TODO ===
