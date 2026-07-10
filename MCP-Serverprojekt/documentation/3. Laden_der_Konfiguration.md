# Laden der Konfiguration
```python
SDP_BASE_URL = os.environ.get("SDP_BASE_URL", "").rstrip("/")
SDP_API_KEY = os.environ.get("SDP_API_KEY", "")
```

## Erklärung
- SDP_Base_URL: URL der ServiceDeskPlus API
- SDP_API_Key: API Schlüssel zur Authentifizierung 
- ermöglicht mehr Sicherheit und Testung des Servers in unterschiedlichen Umgebungen
