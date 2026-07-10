# Die Zentrale API Funktion

```python
async def sdp_request(...)
```

Die Funktion "sdp_request", ist für sämtliche Kommunikation mit der API zuständig. 
Sie kümmert sich dabei um:

- Authentifizierung 
- URL Erstellung
- GET-, POST- und PUT Anfragen
- Fehlerbehandlung
- Rückgabe der Antworten in JSON Format

