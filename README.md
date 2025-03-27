# Cursor Firecrawl Integration

This project integrates [Firecrawl](https://github.com/mendableai/firecrawl) web scraping capabilities with the Cursor MCP server to enhance AI assistance through improved web content processing.

## Overview

The integration enables Cursor's AI assistant to:
- Scrape web content efficiently using Firecrawl's advanced capabilities
- Convert web pages into clean, LLM-ready markdown format
- Extract structured data from websites
- Process multiple URLs in batch mode
- Handle dynamic web content and JavaScript-rendered pages

## Features

- **Clean Data Extraction**: Convert web content into markdown or structured data
- **Batch Processing**: Handle multiple URLs simultaneously
- **Custom Actions**: Support for complex web interactions
- **Structured Data Extraction**: Extract specific data using predefined schemas
- **Integration with Cursor MCP**: Seamless communication between Firecrawl and Cursor

## Prerequisites

- Python 3.8+
- Node.js 16+
- Firecrawl API key (obtain from [firecrawl.dev](https://firecrawl.dev))
- Cursor MCP server access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/GGEDeveloper/cursor-firecrawl-integration.git
cd cursor-firecrawl-integration
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies:
```bash
npm install
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Firecrawl API key and other configuration
```

## Project Structure

```
cursor-firecrawl-integration/
├── src/
│   ├── python/
│   │   ├── scraper.py
│   │   └── cursor_integration.py
│   └── node/
│       ├── server.js
│       └── api_handler.js
├── tests/
├── config/
├── examples/
└── docs/
```

## Usage

1. Start the integration server:
```bash
python src/python/main.py
```

2. Configure Cursor MCP to use the integration:
```javascript
// Configuration example will be provided
```

## Development

### Setting up the Development Environment

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

### Running Tests

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Firecrawl](https://github.com/mendableai/firecrawl) for the excellent web scraping capabilities
- Cursor team for the MCP server platform

## Support

For support, please:
1. Check the [documentation](docs/)
2. Open an issue in the repository
3. Contact the maintainers