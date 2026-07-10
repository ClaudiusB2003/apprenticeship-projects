# MCP-Server für ManageEngine ServiceDesk Plus

## Übersicht

Dieses Projekt dokumentiert die Entwicklung eines MCP-Servers (Model Context Protocol) im Rahmen meiner Ausbildung zum Fachinformatiker für Systemintegration.
Der Schwerpunkt liegt auf der Anbindung eines bestehenden Ticketsystems (ManageEngine ServiceDesk Plus) an ein Sprachmodell, sodass Tickets über natürliche Sprache abgefragt, angelegt und bearbeitet werden können. 
Zu Test Zwecken wurde ein lokaler API-Simulator (Mock-Server) entwickelt, um unabhängig vom Produktivsystem entwickeln und testen zu können.

## Repository-Struktur

```text
MCP-Serverprojekt/
├── README.md
│
├── mock_server/            
│   ├── __init__.py
│   └── mock_server.py
│
├── server/                
│   ├── __init__.py
│   └── server.py
│
└── documentation/          
    ├── 01-bibliotheken/
    │   └── README.md
    ├── 02-initialisierung-mcp-server/
    │   └── README.md
    ├── 03-laden-der-konfiguration/
    │   └── README.md
    ├── 04-exception-klasse/
    │   └── README.md
    └── 05-api-funktion/
        └── README.md
```

## Nachgewiesene Fähigkeiten

- Anbindung externer REST-APIs
- Entwicklung und Testen mit Mock-Servern
- Fehlerbehandlung in produktionsnahem Code
- Sicherer Umgang mit Zugangsdaten
- Technische Dokumentation

## Ausblick

Nach Abschluss dieser Beta-Phase folgt die Anbindung an die reale ServiceDesk-Plus-Instanz, inklusive Anpassung der API-Endpunkte, Authentifizierung und Fehlerbehandlung für den Produktivbetrieb.

## Autor

**Claudius B.**
Auszubildender zum Fachinformatiker für Systemintegration
