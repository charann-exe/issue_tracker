## Software Requirements Specification (SRS)

### 1. Purpose
Define functional and non-functional requirements for a minimal Issue Tracking System.

### 2. Scope
Provide REST endpoints to manage projects and issues with a simple defect workflow.

### 3. Definitions
- Issue: A trackable unit of work/bug with severity and status.
- Workflow: New → In Progress → Resolved → Closed.

### 4. Functional Requirements
- FR1: The system shall allow creation and listing of projects.
- FR2: The system shall allow creation, listing, viewing, and updating issues within a project.
- FR3: The system shall restrict reopening of Closed issues.

### 5. Non-Functional Requirements
- NFR1: API shall respond under 500ms for typical operations.
- NFR2: Automated tests shall cover core flows.
- NFR3: Persistence via SQLite.

### 6. Constraints
- Single-user demo scope. No authentication.

### 7. Assumptions
- Consumers are trusted; no advanced validation beyond schema constraints.

