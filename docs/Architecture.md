## Architecture

### High-level
- Layered design: API layer (FastAPI) → Service/CRUD layer → Persistence (SQLAlchemy/SQLite).
- Entities: `Project`, `Issue` with enumerations `IssueStatus`, `Severity`.

### Data Model
- Project (id, name)
- Issue (id, project_id, title, description, severity, status, timestamps)

### Key Decisions
- Use SQLite for easy local and CI persistence.
- Create tables at startup for simplicity.
- Keep business rules minimal but demonstrable (cannot reopen Closed issues).

