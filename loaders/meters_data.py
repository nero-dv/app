from pydantic import BaseModel, Field
from typing import List


class ElectricalMeasurement(BaseModel):
    eid: int = Field(..., description="The unique identifier for the device.")
    state: str = Field(..., description="The state of the device.")
    measurementType: str = Field(..., description="The measurement type of the device.")
    phaseMode: str = Field(..., description="The phase mode of the device.")
    phaseCount: int = Field(..., description="The number of phases.")
    meteringStatus: str = Field(..., description="The metering status of the device.")
    statusFlags: List[str] = Field(..., description="List of status flags for the device.")

    class Config:
        schema_extra = {
            "example": {
                "eid": 123456789,
                "state": "enabled",
                "measurementType": "production",
                "phaseMode": "split",
                "phaseCount": 2,
                "meteringStatus": "normal",
                "statusFlags": [],
            }
        }


# Example of using the model with provided data
example_data = [
    {
        "eid": 123456789,
        "state": "enabled",
        "measurementType": "production",
        "phaseMode": "split",
        "phaseCount": 2,
        "meteringStatus": "normal",
        "statusFlags": [],
    },
    {
        "eid": 123456781,
        "state": "enabled",
        "measurementType": "total-consumption",
        "phaseMode": "split",
        "phaseCount": 2,
        "meteringStatus": "normal",
        "statusFlags": [],
    },
]

electrical_measurements = [ElectricalMeasurement(**report) for report in example_data]

for measurement in electrical_measurements:
    print(measurement.model_dump_json(indent=4))
