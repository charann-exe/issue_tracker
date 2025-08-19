## Code Review Summary

### Overview
Reviewed `src/app` for clarity, separation of concerns, and basic validation.

### Findings
- Models use enums for `status` and `severity` improving type safety.
- Startup `create_all` simplifies demo but should be replaced with migrations in production.
- Workflow rule enforced at the API layer; could be refactored into a domain service for reuse.

### Actions
- Accepted as-is for demo. Noted improvement items for future iterations.

