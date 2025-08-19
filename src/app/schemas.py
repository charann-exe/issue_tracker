from typing import Optional
from pydantic import BaseModel, Field
from .models import IssueStatus, Severity


class ProjectCreate(BaseModel):
	name: str = Field(min_length=2, max_length=128)


class ProjectRead(BaseModel):
	id: int
	name: str

	class Config:
		from_attributes = True


class IssueCreate(BaseModel):
	title: str = Field(min_length=2, max_length=256)
	description: Optional[str] = None
	severity: Severity = Severity.MEDIUM


class IssueUpdate(BaseModel):
	title: Optional[str] = Field(default=None, min_length=2, max_length=256)
	description: Optional[str] = None
	severity: Optional[Severity] = None
	status: Optional[IssueStatus] = None


class IssueRead(BaseModel):
	id: int
	project_id: int
	title: str
	description: Optional[str]
	severity: Severity
	status: IssueStatus

	class Config:
		from_attributes = True

