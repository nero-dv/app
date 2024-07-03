from pydantic import BaseModel, Field
from datetime import datetime

class DeviceReport(BaseModel):
    serialNumber: str
    lastReportDate: datetime = Field(..., alias="lastReportDate")
    devType: int
    lastReportWatts: int
    maxReportWatts: int


# Example of using the model with provided data
example_data = [
    {
        "serialNumber": "123456789123",
        "lastReportDate": 123456789123,
        "devType": 1,
        "lastReportWatts": 33,
        "maxReportWatts": 456,
    },
    {
        "serialNumber": "123456789123",
        "lastReportDate": 123456789123,
        "devType": 1,
        "lastReportWatts": 35,
        "maxReportWatts": 456,
    },
    {
        "serialNumber": "123456789123",
        "lastReportDate": 123456789123,
        "devType": 1,
        "lastReportWatts": 36,
        "maxReportWatts": 456,
    },
]

# Convert epoch timestamp to datetime object
for report in example_data:
    report["lastReportDate"] = datetime.fromtimestamp(report["lastReportDate"])

device_reports = [DeviceReport(**report) for report in example_data]

for report in device_reports:
    print(report.model_dump_json(indent=4))
