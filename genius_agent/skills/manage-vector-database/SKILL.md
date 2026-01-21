---
name: vector-search
description: Capabilities for managing a vector database.
---

### Overview
This skill allows you to manage a vector database.

### Capabilities
- **create_collection**: Creates a new collection or retrieves an existing one in the vector database.
- **vector_search**: Retrieves and gathers related knowledge from the vector database instance using the question variable.
- **add_documents**: Adds documents to an existing collection in the vector database.
- **delete_collection**: Deletes a collection from the vector database.
- **list_collections**: Lists all collections in the vector database.

### Common Tools
- `vector_search`: Primary tool for finding relevant context using semantic search.
- `add_documents`: Use to ingest documents.
- `list_collections`: Check available collections.

### Usage Rules
- Use `vector_search` to find relevant documents before answering a user query.
- Use `add_documents` to store new information found during research.
- Manage collections with `create_collection` and `list_collections`.
