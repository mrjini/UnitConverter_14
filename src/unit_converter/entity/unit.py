from dataclasses import dataclass


@dataclass(frozen=True)
class Unit:
    name: str
    to_meter_factor: float


@dataclass(frozen=True)
class ConversionResult:
    input_unit: str
    input_value: float
    target_unit: str
    target_value: float
