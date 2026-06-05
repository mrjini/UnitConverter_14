"""CONV-01~03: meter/feet/yard 입력 기본 변환 (entity Logic Track)."""

from unit_converter.entity.converter import Converter
from unit_converter.entity.registry import UnitRegistry
from unit_converter.entity.unit import Unit


def _make_default_registry() -> UnitRegistry:
    registry = UnitRegistry()
    registry.register(Unit("meter", 1.0))
    registry.register(Unit("feet", 1 / 3.28084))
    registry.register(Unit("yard", 1 / 1.09361))
    return registry


def _to_dict(results):
    return {r.target_unit: r.target_value for r in results}


def test_conv_01_meter_input_basic_conversion():
    """CONV-01: meter 입력 기본 변환."""
    # Given: Registry에 meter, feet, yard 등록 (to_meter_factor: 1.0, 1/3.28084, 1/1.09361)
    registry = _make_default_registry()
    # When: Converter.convert_all("meter", 2.5, registry)
    results = Converter().convert_all("meter", 2.5, registry)
    # Then: meter=2.5, feet=8.2, yard=2.7 (display 1자리, round half up)
    assert _to_dict(results) == {"meter": 2.5, "feet": 8.2, "yard": 2.7}


def test_conv_02_feet_input_conversion():
    """CONV-02: feet 입력 변환."""
    # Given: Registry 기본 3단위 (meter, feet, yard)
    registry = _make_default_registry()
    # When: Converter.convert_all("feet", 8.2, registry)
    results = Converter().convert_all("feet", 8.2, registry)
    # Then: meter=2.5, feet=8.2, yard=2.7 (meter 경유, display 1자리)
    assert _to_dict(results) == {"meter": 2.5, "feet": 8.2, "yard": 2.7}


def test_conv_03_yard_input_conversion():
    """CONV-03: yard 입력 변환."""
    # Given: Registry 기본 3단위 (meter, feet, yard)
    registry = _make_default_registry()
    # When: Converter.convert_all("yard", 2.7, registry)
    results = Converter().convert_all("yard", 2.7, registry)
    # Then: meter=2.5, feet=8.1, yard=2.7 (meter 경유, display 1자리)
    assert _to_dict(results) == {"meter": 2.5, "feet": 8.1, "yard": 2.7}
