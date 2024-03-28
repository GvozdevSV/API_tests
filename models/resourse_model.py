
from pydantic import BaseModel, RootModel




class Resource(BaseModel):
    projectRoleId: int = 1
    userId: int = 1
    isProjectManager: bool = True

class Model(BaseModel):
    code: str = 'ATP'
    name: str = 'AutoTestProject'
    startDate: str = '01.10.2022'
    endDate: str = '01.10.2029'
    status: str = 'ACTIV'
    selfAdding: bool = True
    laborReasons: bool = False
    mandatoryAttachFiles: bool = False
    resources: list = [Resource().model_dump()]
    automaticLaborReports: bool = False

print(Model(endDate='01.10.2023').model_dump())
#print(Resource().model_dump())

assert {"projectRoleId": 1, "userId": 1, "isProjectManager": True} == Resource().model_dump()