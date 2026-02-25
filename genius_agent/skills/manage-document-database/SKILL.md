---
name: manage-document-database
description: Manage the DocumentDB instance, including creating collections, inserting documents, and searching.
tags: [manage-document-database]
---

### Overview
This skill provides capabilities to interact with the Document Database (MongoDB-compatible). It allows for granular control over collections and documents, as well as powerful search capabilities using MongoDB's query language.

### Capabilities
- **Collection Management**: Create, list, drop, and rename collections.
- **Document Management**: Insert, update, replace, and delete documents.
- **Search**: Find documents using flexible queries.
- **Aggregation**: Perform complex data aggregations.

### Tools
- `find`: Search for documents in a collection.
- `insert_one` / `insert_many`: Add documents to a collection.
- `update_one` / `update_many`: Modify existing documents.
- `delete_one` / `delete_many`: Remove documents.
- `create_collection`: Create a new collection.
- `list_collections`: See available collections.

### Usage
- Use `find` when you need to retrieve specific documents based on metadata or content fields.
- Use `insert_one` when adding a single new record manually.
- Use `update_one` to correct or append information to an existing document.
- Use `list_collections` to explore what data is available.
