"""
Mini-Simulator für die ManageEngine ServiceDesk Plus REST API (v3).

Bildet die für den MCP-Server relevanten Endpunkte nach:
  GET    /api/v3/requests               -> Tickets listen (mit input_data-Filter)
  GET    /api/v3/requests/{id}          -> Einzelnes Ticket
  POST   /api/v3/requests               -> Ticket anlegen
  PUT    /api/v3/requests/{id}          -> Ticket aktualisieren (z.B. Status)
  POST   /api/v3/requests/{id}/notes    -> Notiz hinzufügen


Dann in eurem MCP-Server:
    set SDP_BASE_URL=http://127.0.0.1:9000/api/v3
    set SDP_API_KEY=beliebiger-test-key
"""

import itertools
import json
from datetime import datetime, timezone

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="ServiceDesk Plus Mock")

_id_counter = itertools.count(1001)

# Test Tickets
TICKETS: dict[str, dict] = {
    "1001": {
        "id": "1001",
        "subject": "Drucker im 2. OG druckt nicht",
        "description": "Der Netzwerkdrucker zeigt einen Papierstau-Fehler an, obwohl kein Papier klemmt.",
        "status": {"name": "Open"},
        "priority": {"name": "Normal"},
        "requester": {"email_id": "max.mustermann@example.com", "name": "Max Mustermann"},
        "created_time": {"value": "2026-07-01 09:12:00"},
        "notes": [],
    },
    "1002": {
        "id": "1002",
        "subject": "VPN-Verbindung bricht ständig ab",
        "description": "Seit dem letzten Client-Update trennt sich die VPN-Verbindung alle 10 Minuten.",
        "status": {"name": "In Progress"},
        "priority": {"name": "High"},
        "requester": {"email_id": "erika.beispiel@example.com", "name": "Erika Beispiel"},
        "created_time": {"value": "2026-07-03 14:45:00"},
        "notes": [
            {"description": "Ticket an Netzwerk-Team weitergeleitet.", "show_to_requester": False}
        ],
    },
    "1003": {
        "id": "1003",
        "subject": "Zugriff auf Laufwerk Z: fehlt",
        "description": "Neuer Mitarbeiter hat noch keinen Zugriff auf das Abteilungslaufwerk.",
        "status": {"name": "Closed"},
        "priority": {"name": "Low"},
        "requester": {"email_id": "neu.mitarbeiter@example.com", "name": "Neu Mitarbeiter"},
        "created_time": {"value": "2026-06-20 08:00:00"},
        "notes": [],
    },
}


def _check_auth(technician_key: str | None):
    if not technician_key:
        raise HTTPException(
            status_code=401,
            detail={"response_status": {"status": "failed", "messages": [{"message": "Missing TECHNICIAN_KEY header"}]}},
        )


def _parse_input_data(raw: str | None) -> dict:
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="input_data ist kein gültiges JSON")


@app.get("/api/v3/requests")
def list_requests(input_data: str | None = None, technician_key: str | None = Header(None, alias="TECHNICIAN_KEY")):
    _check_auth(technician_key)
    filters = _parse_input_data(input_data)

    results = list(TICKETS.values())

    search = filters.get("list_info", {}).get("search_criteria")
    if search and search.get("field") == "status.name":
        wanted_status = search.get("value")
        results = [t for t in results if t["status"]["name"].lower() == str(wanted_status).lower()]

    row_count = filters.get("list_info", {}).get("row_count", 10)
    start_index = filters.get("list_info", {}).get("start_index", 0)
    page = results[start_index : start_index + row_count]

    return {
        "requests": page,
        "list_info": {
            "row_count": row_count,
            "start_index": start_index,
            "has_more_rows": start_index + row_count < len(results),
            "total_count": len(results),
        },
        "response_status": {"status": "success"},
    }


@app.get("/api/v3/requests/{ticket_id}")
def get_request(ticket_id: str, technician_key: str | None = Header(None, alias="TECHNICIAN_KEY")):
    _check_auth(technician_key)
    ticket = TICKETS.get(ticket_id)
    if not ticket:
        return JSONResponse(
            status_code=404,
            content={"response_status": {"status": "failed", "messages": [{"message": f"Request {ticket_id} not found"}]}},
        )
    return {"request": ticket, "response_status": {"status": "success"}}


@app.post("/api/v3/requests")
async def create_request(request: Request, technician_key: str | None = Header(None, alias="TECHNICIAN_KEY")):
    _check_auth(technician_key)
    form = await request.form()
    payload = _parse_input_data(form.get("input_data"))

    req_data = payload.get("request", {})
    new_id = str(next(_id_counter))
    ticket = {
        "id": new_id,
        "subject": req_data.get("subject", ""),
        "description": req_data.get("description", ""),
        "status": {"name": "Open"},
        "priority": req_data.get("priority", {"name": "Normal"}),
        "requester": req_data.get("requester", {}),
        "created_time": {"value": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")},
        "notes": [],
    }
    TICKETS[new_id] = ticket
    return {"request": ticket, "response_status": {"status": "success"}}


@app.put("/api/v3/requests/{ticket_id}")
async def update_request(ticket_id: str, request: Request, technician_key: str | None = Header(None, alias="TECHNICIAN_KEY")):
    _check_auth(technician_key)
    ticket = TICKETS.get(ticket_id)
    if not ticket:
        return JSONResponse(
            status_code=404,
            content={"response_status": {"status": "failed", "messages": [{"message": f"Request {ticket_id} not found"}]}},
        )

    form = await request.form()
    payload = _parse_input_data(form.get("input_data"))
    updates = payload.get("request", {})

    if "status" in updates:
        ticket["status"] = updates["status"]
    if "priority" in updates:
        ticket["priority"] = updates["priority"]
    if "subject" in updates:
        ticket["subject"] = updates["subject"]

    return {"request": ticket, "response_status": {"status": "success"}}


@app.post("/api/v3/requests/{ticket_id}/notes")
async def add_note(ticket_id: str, request: Request, technician_key: str | None = Header(None, alias="TECHNICIAN_KEY")):
    _check_auth(technician_key)
    ticket = TICKETS.get(ticket_id)
    if not ticket:
        return JSONResponse(
            status_code=404,
            content={"response_status": {"status": "failed", "messages": [{"message": f"Request {ticket_id} not found"}]}},
        )

    form = await request.form()
    payload = _parse_input_data(form.get("input_data"))
    note = payload.get("request_note", {})
    ticket["notes"].append(note)

    return {"request_note": note, "response_status": {"status": "success"}}


@app.get("/")
def root():
    return {"message": "ServiceDesk Plus Mock läuft. Siehe /docs für die Endpunkte."}