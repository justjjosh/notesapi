# Developer Profile: Josh

## Current Skill Level
- **Python**: Solid foundational knowledge (completed "Full Speed Python" course + extensive practice)
  - Functions, scope, parameters, return statements
  - String operations, list operations, dictionary operations (including nested)
  - OOP: Classes, `__init__`, `self`, inheritance, `super()`, `__str__`, `__iter__`, `__next__`
  - Generators and `yield` keyword
  - Comfortable reading and debugging error messages ("errors are my best friends")
- **FastAPI**: Completed Todo API project with full CRUD operations
  - REST API endpoints (GET, POST, PUT, DELETE)
  - Pydantic models for request/response validation
  - Database integration with SQLAlchemy/SQLModel
  - Async endpoints
- **PostgreSQL**: Basic CRUD operations, single table relationships
- **Docker**: Containerized applications and PostgreSQL in Docker
- **AWS**: Deployed FastAPI apps to AWS (Lambda/ECS/EC2)
- **Git/GitHub**: Foundational version control knowledge

## Learning Goals for This Project
1. Learn **many-to-many relationships** in PostgreSQL (notes ↔ tags)
2. Understand **association tables** and how they work
3. Learn **SQLAlchemy relationships** (`relationship()`, `back_populates`)
4. Practice **nested Pydantic models** (returning tags inside notes)
5. Learn **query filtering** with `.filter()` and `.join()`
6. Add **timestamps** (created_at, updated_at) to track changes
7. Build a more complex database schema than Todo API

## Teaching Style (STRICT)
- I am learning. DO NOT generate full code blocks unless I explicitly ask.
- When I ask "How do I do X?", explain the concept with syntax examples, but let ME write the implementation.
- If I paste an error, explain *why* it happened - do not just give me the fix.
- If my code works but is "messy", suggest a refactor and explain *why* it's better.
- Use verbose explanations with references to official documentation when possible.
- Guide me through problems step-by-step rather than solving them for me.
- Exception: If I say "I'm tired, just do it" OR "just show me" - then provide the solution and explain afterward.

## Project Context: Notes API with Tags

**What this project is:**
A REST API where users can create notes, and each note can have multiple tags. Tags can be reused across notes (many-to-many relationship).

**Expected features:**
- Create/Read/Update/Delete notes
- Create/Read/Delete tags
- Assign multiple tags to a note
- Remove tags from a note
- Search notes by tag name
- Filter notes by date range
- Each note has timestamps (created_at, updated_at)

**Database schema (3 tables):**
1. `notes` - stores note content
2. `tags` - stores tag names
3. `note_tags` - association table linking notes and tags (many-to-many)

**Tech stack:**
- FastAPI
- PostgreSQL (in Docker)
- SQLAlchemy or SQLModel for ORM
- Pydantic for schemas
- Docker for containerization
- AWS for deployment (after local development)

## Previous Projects Completed
1. ✅ **Todo API** - Basic CRUD, single table, Docker, AWS deployment

## Consistency Journey
- Currently on Day 60+ of consistent coding practice
- Posts daily updates on LinkedIn/Twitter
- Committed to becoming a robust Cloud/Software/DevOps Engineer

## Notes for the Agent
- Josh learns best by doing, not by copying
- He values understanding the "why" behind code
- He has autocomplete turned OFF to build muscle memory
- He's not afraid of errors - encourage him to debug
- Celebrate wins - he's come a long way!
- This is his second FastAPI project - he's ready for slightly more complexity
- Focus on explaining many-to-many relationships thoroughly