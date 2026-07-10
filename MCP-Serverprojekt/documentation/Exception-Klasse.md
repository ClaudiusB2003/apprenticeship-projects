# Exception Klasse
```python
class SdpError(Exception):
    """Fehler bei der Kommunikation mit ServiceDesk Plus."""
```

## Erklärung
- Zur Fehlerbehandlung der ServiceDeskPlus API, wird eine eigene Fehlerklasse erstellt
- gibt aussagekräftige Fehlermeldungen zurück 

z.B. 

API-Fehler (401) 

Verbindung fehlgeschlagen