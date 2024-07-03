from typing import List
from pydantic import BaseModel, Field


class ChannelReport(BaseModel):
    eid: int = Field(..., description="The unique identifier for the channel.")
    timestamp: int = Field(..., description="The timestamp as a Unix timestamp.")
    actEnergyDlvd: float = Field(..., description="Active energy delivered in watt-hours.")
    actEnergyRcvd: float = Field(..., description="Active energy received in watt-hours.")
    apparentEnergy: float = Field(..., description="Apparent energy in volt-ampere hours.")
    reactEnergyLagg: float = Field(..., description="Reactive energy lagging in var-hours.")
    reactEnergyLead: float = Field(..., description="Reactive energy leading in var-hours.")
    instantaneousDemand: float = Field(..., description="Instantaneous demand in watts.")
    activePower: float = Field(..., description="Active power in watts.")
    apparentPower: float = Field(..., description="Apparent power in volt-amperes.")
    reactivePower: float = Field(..., description="Reactive power in var.")
    pwrFactor: float = Field(..., description="Power factor.")
    voltage: float = Field(..., description="Voltage in volts.")
    current: float = Field(..., description="Current in amperes.")
    freq: float = Field(..., description="Frequency in hertz.")


class DeviceReport(BaseModel):
    eid: int = Field(..., description="The unique identifier for the device.")
    timestamp: int = Field(..., description="The timestamp as a Unix timestamp.")
    actEnergyDlvd: float = Field(..., description="Active energy delivered in watt-hours.")
    actEnergyRcvd: float = Field(..., description="Active energy received in watt-hours.")
    apparentEnergy: float = Field(..., description="Apparent energy in volt-ampere hours.")
    reactEnergyLagg: float = Field(..., description="Reactive energy lagging in var-hours.")
    reactEnergyLead: float = Field(..., description="Reactive energy leading in var-hours.")
    instantaneousDemand: float = Field(..., description="Instantaneous demand in watts.")
    activePower: float = Field(..., description="Active power in watts.")
    apparentPower: float = Field(..., description="Apparent power in volt-amperes.")
    reactivePower: float = Field(..., description="Reactive power in var.")
    pwrFactor: float = Field(..., description="Power factor.")
    voltage: float = Field(..., description="Voltage in volts.")
    current: float = Field(..., description="Current in amperes.")
    freq: float = Field(..., description="Frequency in hertz.")
    channels: List[ChannelReport] = Field(..., description="List of channel reports.")

example_data = [
    {
        "eid": 123456789,
        "timestamp": 1720024407,
        "actEnergyDlvd": 12345678.123,
        "actEnergyRcvd": 0.001,
        "apparentEnergy": 12345678.123,
        "reactEnergyLagg": 1234567.123,
        "reactEnergyLead": 0.031,
        "instantaneousDemand": 123.456,
        "activePower": 123.456,
        "apparentPower": 456.123,
        "reactivePower": 345.123,
        "pwrFactor": 0.789,
        "voltage": 240.123,
        "current": 6.123,
        "freq": 60.000,
        "channels": [
            {
                "eid": 123456787,
                "timestamp": 1720024407,
                "actEnergyDlvd": 12345678.123,
                "actEnergyRcvd": 0.001,
                "apparentEnergy": 12345678.123,
                "reactEnergyLagg": 1234567.123,
                "reactEnergyLead": 0.031,
                "instantaneousDemand": 123.456,
                "activePower": 123.456,
                "apparentPower": 456.123,
                "reactivePower": 345.123,
                "pwrFactor": 0.789,
                "voltage": 240.123,
                "current": 6.123,
                "freq": 60.000,
            },
            {
                "eid": 123456786,
                "timestamp": 1720024407,
                "actEnergyDlvd": 12345678.123,
                "actEnergyRcvd": 0.001,
                "apparentEnergy": 12345678.123,
                "reactEnergyLagg": 1234567.123,
                "reactEnergyLead": 0.031,
                "instantaneousDemand": 123.456,
                "activePower": 123.456,
                "apparentPower": 456.123,
                "reactivePower": 345.123,
                "pwrFactor": 0.789,
                "voltage": 240.123,
                "current": 6.123,
                "freq": 60.000,
            },
            {
                "eid": 123456785,
                "timestamp": 1720024407,
                "actEnergyDlvd": 12345678.123,
                "actEnergyRcvd": 0.001,
                "apparentEnergy": 12345678.123,
                "reactEnergyLagg": 1234567.123,
                "reactEnergyLead": 0.031,
                "instantaneousDemand": 123.456,
                "activePower": 123.456,
                "apparentPower": 456.123,
                "reactivePower": 345.123,
                "pwrFactor": 0.789,
                "voltage": 240.123,
                "current": 6.123,
                "freq": 60.000,
            },
        ],
    },
    {
        "eid": 123456781,
        "timestamp": 1720024407,
        "actEnergyDlvd": 12345678.123,
        "actEnergyRcvd": 0.001,
        "apparentEnergy": 12345678.123,
        "reactEnergyLagg": 1234567.123,
        "reactEnergyLead": 0.031,
        "instantaneousDemand": 123.456,
        "activePower": 123.456,
        "apparentPower": 456.123,
        "reactivePower": 345.123,
        "pwrFactor": 0.789,
        "voltage": 240.123,
        "current": 6.123,
        "freq": 60.000,
        "channels": [
            {
                "eid": 123456782,
                "timestamp": 1720024407,
                "actEnergyDlvd": 12345678.123,
                "actEnergyRcvd": 0.001,
                "apparentEnergy": 12345678.123,
                "reactEnergyLagg": 1234567.123,
                "reactEnergyLead": 0.031,
                "instantaneousDemand": 123.456,
                "activePower": 123.456,
                "apparentPower": 456.123,
                "reactivePower": 345.123,
                "pwrFactor": 0.789,
                "voltage": 240.123,
                "current": 6.123,
                "freq": 60.000,
            },
            {
                "eid": 123456783,
                "timestamp": 1720024407,
                "actEnergyDlvd": 12345678.123,
                "actEnergyRcvd": 0.001,
                "apparentEnergy": 12345678.123,
                "reactEnergyLagg": 1234567.123,
                "reactEnergyLead": 0.031,
                "instantaneousDemand": 123.456,
                "activePower": 123.456,
                "apparentPower": 456.123,
                "reactivePower": 345.123,
                "pwrFactor": 0.789,
                "voltage": 240.123,
                "current": 6.123,
                "freq": 60.000,
            },
            {
                "eid": 123456784,
                "timestamp": 1720024407,
                "actEnergyDlvd": 12345678.123,
                "actEnergyRcvd": 0.001,
                "apparentEnergy": 12345678.123,
                "reactEnergyLagg": 1234567.123,
                "reactEnergyLead": 0.031,
                "instantaneousDemand": 123.456,
                "activePower": 123.456,
                "apparentPower": 456.123,
                "reactivePower": 345.123,
                "pwrFactor": 0.789,
                "voltage": 240.123,
                "current": 6.123,
                "freq": 60.000,
            },
        ],
    },
]

reports = [DeviceReport(**report) for report in example_data]

for report in reports:
    print(report.model_dump_json(indent=4))
