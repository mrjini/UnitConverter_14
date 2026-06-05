"""CONV-01~03: meter/feet/yard 입력 기본 변환 (entity Logic Track)."""

import pytest


def test_conv_01_meter_input_basic_conversion():
    """CONV-01: meter 입력 기본 변환."""
    # Given: Registry에 meter, feet, yard 등록 (to_meter_factor: 1.0, 1/3.28084, 1/1.09361)
    # When: Converter.convert_all("meter", 2.5, registry)
    # Then: meter=2.5, feet=8.2, yard=2.7 (display 1자리, round half up)
    pytest.fail("RED: Test ID CONV-01 — meter 2.5 입력 시 전 단위 display 1자리 변환")


def test_conv_02_feet_input_conversion():
    """CONV-02: feet 입력 변환."""
    # Given: Registry 기본 3단위 (meter, feet, yard)
    # When: Converter.convert_all("feet", 8.2, registry)
    # Then: meter=2.5, feet=8.2, yard=2.7 (meter 경유, display 1자리)
    pytest.fail("RED: Test ID CONV-02 — feet 8.2 입력 시 meter 경유 전 단위 변환")


def test_conv_03_yard_input_conversion():
    """CONV-03: yard 입력 변환."""
    # Given: Registry 기본 3단위 (meter, feet, yard)
    # When: Converter.convert_all("yard", 2.7, registry)
    # Then: meter=2.5, feet=8.2, yard=2.7 (전 단위 출력, display 1자리)
    pytest.fail("RED: Test ID CONV-03 — yard 2.7 입력 시 meter 경유 전 단위 변환")
