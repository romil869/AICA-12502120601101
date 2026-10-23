"""Blood Group Compatibility System - Python version of both Prolog methods.
Simplified red-cell model for learning only, not for clinical use."""

# ---------- Method 1: facts (like blood_facts.pl) ----------
compatible_facts = {
    ("o", "o"), ("o", "a"),
    ("o", "b"), ("o", "ab"),
    ("a", "a"), ("a", "ab"),
    ("b", "b"), ("b", "ab"),
    ("ab", "ab"),
}


def is_compatible(donor, recipient):
    return (donor, recipient) in compatible_facts


# ---------- Method 2: rules (like blood_rules.pl) ----------
ANTIGENS = {
    "o": set(), "a": {"a"},
    "b": {"b"}, "ab": {"a", "b"},
}


def compatible(d, r):
    return ANTIGENS[d] <= ANTIGENS[r]


def recipients_of(d):
    return [r for r in ANTIGENS
            if compatible(d, r)]


def donors_for(r):
    return [d for d in ANTIGENS
            if compatible(d, r)]


if __name__ == "__main__":
    print("Method 1 (facts)")
    print(is_compatible("o", "ab"))   # True
    print(is_compatible("ab", "o"))   # False

    print("Method 2 (rules)")
    print(compatible("o", "ab"))      # True
    print(compatible("ab", "o"))      # False
    print(recipients_of("a"))         # ['a', 'ab']
    print(donors_for("ab"))           # ['o', 'a', 'b', 'ab']
