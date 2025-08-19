import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base


class IssueStatus(str, enum.Enum):
	NEW = "New"
	IN_PROGRESS = "In Progress"
	RESOLVED = "Resolved"
	CLOSED = "Closed"


class Severity(str, enum.Enum):
	LOW = "Low"
	MEDIUM = "Medium"
	HIGH = "High"
	CRITICAL = "Critical"


class Project(Base):
	__tablename__ = "projects"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(128), unique=True, nullable=False)

	issues = relationship("Issue", back_populates="project", cascade="all, delete-orphan")


class Issue(Base):
	__tablename__ = "issues"

	id = Column(Integer, primary_key=True, index=True)
	project_id = Column(Integer, ForeignKey("projects.id"), nullable=False, index=True)
	title = Column(String(256), nullable=False, index=True)
	description = Column(Text, nullable=True)
	severity = Column(Enum(Severity), nullable=False, default=Severity.MEDIUM)
	status = Column(Enum(IssueStatus), nullable=False, default=IssueStatus.NEW)
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
	updated_at = Column(
		DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
	)

	project = relationship("Project", back_populates="issues")

