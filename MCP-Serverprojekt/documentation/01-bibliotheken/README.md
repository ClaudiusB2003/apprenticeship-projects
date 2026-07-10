# Importieren der benötigten Bibliotheken
```python
import json
import os

import httpx
from fastmcp import FastMCP
```

## JSON
- wandelt Python-Dictionaries in JSON Format um
--> JSON Format wird von API erwartet

## os
- ermöglicht Änderungen im Datei Verzeichnis

## httpx
- ermöglicht API-Anfragen an ServiceDesk Plus

## FastMCP
- stellt MCP-Server bereit
- ermöglicht Abruf von Funktionen über KI Agenten, welche mit "@mcp.tool" makiert sind

