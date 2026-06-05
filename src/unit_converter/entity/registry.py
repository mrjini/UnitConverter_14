from unit_converter.entity.unit import Unit


class UnitRegistry:
    def __init__(self) -> None:
        self._units: dict[str, Unit] = {}
        self._order: list[str] = []

    def register(self, unit: Unit) -> None:
        self._units[unit.name] = unit
        if unit.name not in self._order:
            self._order.append(unit.name)

    def get(self, name: str) -> Unit:
        return self._units[name]

    def all_units(self) -> list[Unit]:
        return [self._units[name] for name in self._order]

    def has(self, name: str) -> bool:
        return name in self._units
