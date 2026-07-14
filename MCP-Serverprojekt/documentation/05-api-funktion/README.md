# Die Zentrale API Funktion

Die Funktion "sdp_request", ist für sämtliche Kommunikation mit der API zuständig. 
Sie kümmert sich dabei um:

- Authentifizierung 
- URL Erstellung
- GET-, POST- und PUT Anfragen
- Fehlerbehandlung
- Rückgabe der Antworten in JSON Format

```python
async def sdp_request(method: str, endpoint: str, input_data: dict | None = None) -> dict:
    if not SDP_BASE_URL or not SDP_API_KEY:
        raise SdpError(
            "SDP_BASE_URL und/oder SDP_API_KEY sind nicht gesetzt. "
            "Bitte als Umgebungsvariablen konfigurieren."
        )

    headers = {"TECHNICIAN_KEY": SDP_API_KEY}
    url = f"{SDP_BASE_URL}/{endpoint.lstrip('/')}"

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            if method == "GET":
                params = {"input_data": json.dumps(input_data)} if input_data else {}
                resp = await client.get(url, headers=headers, params=params)
            else:
                data = {"input_data": json.dumps(input_data)} if input_data else {}
                resp = await client.request(method, url, headers=headers, data=data)
            resp.raise_for_status()
            return resp.json()
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json()
        except ValueError:
            detail = e.response.text
        raise SdpError(f"API-Fehler ({e.response.status_code}) bei {endpoint}: {detail}") from e
    except httpx.RequestError as e:
        raise SdpError(f"Verbindung zu ServiceDesk Plus fehlgeschlagen: {e}") from e
```


