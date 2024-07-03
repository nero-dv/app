from pydantic import BaseModel, Field


class EnergyMetrics(BaseModel):
    wattHoursToday: int = Field(..., description="Energy produced today in watt-hours.")
    wattHoursSevenDays: int = Field(
        ..., description="Energy produced over the past seven days in watt-hours."
    )
    wattHoursLifetime: int = Field(..., description="Total energy produced in the lifetime in watt-hours.")
    wattsNow: int = Field(..., description="Current power production in watts.")


example_data = [
    {
        "wattHoursToday": 12345,
        "wattHoursSevenDays": 123456,
        "wattHoursLifetime": 123456789,
        "wattsNow": 456,
    }
]


reports = [EnergyMetrics(**report) for report in example_data]

for report in reports:
    print(report.model_dump_json(indent=4))
