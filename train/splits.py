"""Deterministic patient-level split shared by every training script (20% held out)."""


def is_val(patient) -> bool:
    return (int(patient) * 2654435761) % 1000 < 200
