# 5.1 Prüfung der Konfiguration

Um die Konfiguration zu prüfen, wird eine asynchrone Funktion erstellt, welche als Grundlage für die Kommunikation mit einer externen API dient.
Vor dem Start, prüft Sie ob alle Zugangsdaten vorhanden sind.

```python
async def sdp_request(method: str, endpoint: str, input_data: dict | None = None) -> dict:
    if not SDP_BASE_URL or not SDP_API_KEY:
        raise SdpError(
            "SDP_BASE_URL und/oder SDP_API_KEY sind nicht gesetzt. "
            "Bitte als Umgebungsvariablen konfigurieren."
        )
```

Wenn die Umgebungsvariablen fehlen, bricht die Funktion den Code mit einer klaren Fehlermeldung ab.
