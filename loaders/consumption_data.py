from typing import List
from pydantic import BaseModel, Field


class LineReport(BaseModel):
    currW: float = Field(..., description="Current power in watts.")
    actPower: float = Field(..., description="Actual power in watts.")
    apprntPwr: float = Field(..., description="Apparent power in watts.")
    reactPwr: float = Field(..., description="Reactive power in watts.")
    whDlvdCum: float = Field(..., description="Cumulative delivered energy in watt-hours.")
    whRcvdCum: float = Field(..., description="Cumulative received energy in watt-hours.")
    varhLagCum: float = Field(..., description="Cumulative lagging reactive energy in var-hours.")
    varhLeadCum: float = Field(..., description="Cumulative leading reactive energy in var-hours.")
    vahCum: float = Field(..., description="Cumulative apparent energy in volt-ampere hours.")
    rmsVoltage: float = Field(..., description="RMS voltage in volts.")
    rmsCurrent: float = Field(..., description="RMS current in amperes.")
    pwrFactor: float = Field(..., description="Power factor.")
    freqHz: float = Field(..., description="Frequency in hertz.")


class CumulativeReport(BaseModel):
    currW: float = Field(..., description="Current power in watts.")
    actPower: float = Field(..., description="Actual power in watts.")
    apprntPwr: float = Field(..., description="Apparent power in watts.")
    reactPwr: float = Field(..., description="Reactive power in watts.")
    whDlvdCum: float = Field(..., description="Cumulative delivered energy in watt-hours.")
    whRcvdCum: float = Field(..., description="Cumulative received energy in watt-hours.")
    varhLagCum: float = Field(..., description="Cumulative lagging reactive energy in var-hours.")
    varhLeadCum: float = Field(..., description="Cumulative leading reactive energy in var-hours.")
    vahCum: float = Field(..., description="Cumulative apparent energy in volt-ampere hours.")
    rmsVoltage: float = Field(..., description="RMS voltage in volts.")
    rmsCurrent: float = Field(..., description="RMS current in amperes.")
    pwrFactor: float = Field(..., description="Power factor.")
    freqHz: float = Field(..., description="Frequency in hertz.")


class ConsumptionDeviceReport(BaseModel):
    createdAt:int = Field(..., description="The creation timestamp as a Unix timestamp.", alias="createdAt")
    reportType: str = Field(..., description="The type of the report.")
    cumulative: CumulativeReport = Field(..., description="Cumulative measurements.")
    lines: List[LineReport] = Field(..., description="Measurements per line.")


# Example of using the model with provided data
example_data = [
    {
        "createdAt": 1719183438,
        "reportType": "total-consumption",
        "cumulative": {
            "currW": 123.45,
            "actPower": 1234.45,
            "apprntPwr": 1234.45,
            "reactPwr": -12.34,
            "whDlvdCum": 123456789.123,
            "whRcvdCum": 0.000,
            "varhLagCum": 123456789.123,
            "varhLeadCum": 1234567.123,
            "vahCum": 12345678912.123,
            "rmsVoltage": 123.456,
            "rmsCurrent": -3.45,
            "pwrFactor": 0.12,
            "freqHz": 60.00,
        },
        "lines": [
            {
                "currW": 123.45,
                "actPower": 1234.45,
                "apprntPwr": 1234.45,
                "reactPwr": -12.34,
                "whDlvdCum": 123456789.123,
                "whRcvdCum": 0.000,
                "varhLagCum": 123456789.123,
                "varhLeadCum": 1234567.123,
                "vahCum": 12345678912.123,
                "rmsVoltage": 123.456,
                "rmsCurrent": -3.45,
                "pwrFactor": 0.12,
                "freqHz": 60.00,
            },
            {
                "currW": 123.45,
                "actPower": 1234.45,
                "apprntPwr": 1234.45,
                "reactPwr": -12.34,
                "whDlvdCum": 123456789.123,
                "whRcvdCum": 0.000,
                "varhLagCum": 123456789.123,
                "varhLeadCum": 1234567.123,
                "vahCum": 12345678912.123,
                "rmsVoltage": 123.456,
                "rmsCurrent": -3.45,
                "pwrFactor": 0.12,
                "freqHz": 60.00,
            },
        ],
    },
    {
        "createdAt": 1719183438,
        "reportType": "net-consumption",
        "cumulative": {
            "currW": 123.45,
            "actPower": 1234.45,
            "apprntPwr": 1234.45,
            "reactPwr": -12.34,
            "whDlvdCum": 123456789.123,
            "whRcvdCum": 0.000,
            "varhLagCum": 123456789.123,
            "varhLeadCum": 1234567.123,
            "vahCum": 12345678912.123,
            "rmsVoltage": 123.456,
            "rmsCurrent": -3.45,
            "pwrFactor": 0.12,
            "freqHz": 60.00,
        },
        "lines": [
            {
                "currW": 123.45,
                "actPower": 1234.45,
                "apprntPwr": 1234.45,
                "reactPwr": -12.34,
                "whDlvdCum": 123456789.123,
                "whRcvdCum": 0.000,
                "varhLagCum": 123456789.123,
                "varhLeadCum": 1234567.123,
                "vahCum": 12345678912.123,
                "rmsVoltage": 123.456,
                "rmsCurrent": -3.45,
                "pwrFactor": 0.12,
                "freqHz": 60.00,
            },
            {
                "currW": 123.45,
                "actPower": 1234.45,
                "apprntPwr": 1234.45,
                "reactPwr": -12.34,
                "whDlvdCum": 123456789.123,
                "whRcvdCum": 0.000,
                "varhLagCum": 123456789.123,
                "varhLeadCum": 1234567.123,
                "vahCum": 12345678912.123,
                "rmsVoltage": 123.456,
                "rmsCurrent": -3.45,
                "pwrFactor": 0.12,
                "freqHz": 60.00,
            },
        ],
    },
]


reports = [ConsumptionDeviceReport(**report) for report in example_data]

for report in reports:
    print(report.model_dump_json(indent=4))
