from decimal import ROUND_HALF_UP, Decimal

from unit_converter.entity.registry import UnitRegistry
from unit_converter.entity.unit import ConversionResult


def _round_display(value: float) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


class Converter:
    def convert_all(
        self, unit: str, value: float, registry: UnitRegistry
    ) -> list[ConversionResult]:
        input_unit = registry.get(unit)
        meter_value = value * input_unit.to_meter_factor
        results: list[ConversionResult] = []
        for target in registry.all_units():
            raw = meter_value / target.to_meter_factor
            results.append(
                ConversionResult(
                    input_unit=unit,
                    input_value=value,
                    target_unit=target.name,
                    target_value=_round_display(raw),
                )
            )
        return results
