from dataclasses import dataclass

FEET_PER_METER = 3.28084
YARD_PER_METER = 1.09361


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
