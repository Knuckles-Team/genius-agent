---
name: web-scraping
description: Web scraping and crawling capabilities for gathering information from websites.
---

### Overview
This skill provides capabilities to crawl websites, extract content, and process web pages using the Crawl4AI Library MCP server.

### Capabilities
- **crawl**: Perform multi-URL crawling to process multiple pages at once.
- **md**: Generate markdown from web content. Use this to read the text content of a page.
- **html**: Extract preprocessed HTML from a webpage.
- **screenshot**: Capture a screenshot of a webpage.
- **pdf**: Generate a PDF document from a webpage.
- **execute_js**: Run custom JavaScript on a web page.
- **ask**: Query the Crawl4AI library context for information about the crawl or library usage.


### Common Tools
- `crawl`: Use for processing multiple URLs or entire sites.
- `md`: Primary tool for reading web page content as Markdown.
- `screenshot`: Use when visual context is needed.

### Usage Rules
- Use `md` when you need to read the content of a specific page to answer a user's question.
- Use `crawl` if the user provides multiple URLs or asks to crawl a site.
- Use `execute_js` if the page requires interaction or dynamic content loading that isn't handled automatically.
