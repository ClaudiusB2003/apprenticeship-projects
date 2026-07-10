# MCP-Server für ManageEngine ServiceDesk Plus

## Übersicht
Dieses Projekt dokumentiert die Entwicklung eines MCP-Servers (Model Context Protocol) im Rahmen meiner Ausbildung zum Fachinformatiker für Systemintegration.
Der Schwerpunkt liegt auf der Anbindung eines bestehenden Ticketsystems (ManageEngine ServiceDesk Plus) an ein Sprachmodell, sodass Tickets über natürliche Sprache abgefragt, angelegt und bearbeitet werden können. Zusätzlich wurde ein lokaler API-Simulator (bzw. mock-server) entwickelt, um unabhängig vom Produktivsystem entwickeln und testen zu können.

## Projektziele
- Entwicklung eines MCP-Servers zur Anbindung einer REST-API
- Anbindung von ManageEngine ServiceDesk Plus über dessen REST-API
- Aufbau eines lokalen API-Mocks zum gefahrlosen Testen
- Sichere Handhabung von Zugangsdaten (API-Key über Umgebungsvariablen)
- Erstellung einer nachvollziehbaren Projektdokumentation

## Verwendete Technologien und Konzepte
- Model Context Protocol (MCP) / FastMCP
- Python (asynchrone Programmierung, REST-Anbindung mit httpx)
- ManageEngine ServiceDesk Plus REST-API
- FastAPI (für den lokalen API-Simulator)
- Umgang mit Umgebungsvariablen und Secrets

## Repository-Struktur
```text
MCP-Serverprojekt/
├── README.md
├── mock_server/
│   ├── mock_server.py
│   └── 
├── server/
│   ├── server.py
│   └── 
├── documentation/
│   ├── 
```

## Nachgewiesene Fähigkeiten
- Anbindung externer REST-APIs
- Entwicklung und Testen mit Mock-Servern
- Fehlerbehandlung in produktionsnahem Code
- Sicherer Umgang mit Zugangsdaten
- Technische Dokumentation

## Autor
**Claudius B.**
Auszubildender zum Fachinformatiker für Systemintegration
