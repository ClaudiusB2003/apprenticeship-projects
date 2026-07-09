import json
import os

import httpx
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

SDP_BASE_URL = os.environ.get("SDP_BASE_URL", "").rstrip("/")
SDP_API_KEY = os.environ.get("SDP_API_KEY", "")


class SdpError(Exception):
    """Fehler bei der Kommunikation mit ServiceDesk Plus."""


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


@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool
async def list_tickets(status: str = "Open", limit: int = 10) -> list[dict]:
    """Listet Tickets aus ServiceDesk Plus, gefiltert nach Status."""
    payload = {
        "list_info": {
            "row_count": min(limit, 100),
            "search_criteria": {"field": "status.name", "condition": "is", "value": status},
        }
    }
    try:
        result = await sdp_request("GET", "requests", payload)
    except SdpError as e:
        return [{"error": str(e)}]
    return result.get("requests", [])


@mcp.tool
async def get_ticket(ticket_id: str) -> dict:
    """Ruft die Details eines Tickets anhand seiner ID ab."""
    try:
        return await sdp_request("GET", f"requests/{ticket_id}")
    except SdpError as e:
        return {"error": str(e)}


@mcp.tool
async def create_ticket(subject: str, description: str, requester_email: str) -> dict:
    """Erstellt ein neues Ticket in ServiceDesk Plus."""
    payload = {
        "request": {
            "subject": subject,
            "description": description,
            "requester": {"email_id": requester_email},
        }
    }
    try:
        return await sdp_request("POST", "requests", payload)
    except SdpError as e:
        return {"error": str(e)}


@mcp.tool
async def add_note(ticket_id: str, note: str, is_public: bool = True) -> dict:
    """Fügt einem Ticket eine Notiz hinzu."""
    payload = {"request_note": {"description": note, "show_to_requester": is_public}}
    try:
        return await sdp_request("POST", f"requests/{ticket_id}/notes", payload)
    except SdpError as e:
        return {"error": str(e)}


@mcp.tool
async def update_ticket_status(ticket_id: str, status: str) -> dict:
    """Ändert den Status eines Tickets (z.B. 'In Progress', 'Resolved', 'Closed')."""
    payload = {"request": {"status": {"name": status}}}
    try:
        return await sdp_request("PUT", f"requests/{ticket_id}", payload)
    except SdpError as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()