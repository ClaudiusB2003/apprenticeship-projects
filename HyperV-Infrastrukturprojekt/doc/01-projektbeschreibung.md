# Projektbeschreibung

Ziel ist der Aufbau einer sicheren, vollständig virtualisierten IT-Infrastruktur für ein fiktives mittelständisches Unternehmen. Die Umgebung bildet praxisnahe Enterprise-Strukturen ab und dient als Lern- und Testplattform. Als Host-Maschine wird ein Lenovo SR630 verwendet.

![Lenovo ThinkSystem SR630 V2 8xSFF CTO Server](../images/server-lenovo-sr630.jpeg)

## Virtualisierungsplattform

Als Hypervisor kommt Microsoft Hyper-V auf dem physischen Host-Server zum Einsatz. Alle Server und Clients werden als virtuelle Maschinen (VMs) betrieben.

![Hyper-V Manager Übersicht](../images/hyperv-manager.png)

## Netzwerkkonzept

Das Netzwerk ist in zwei Bereiche aufgeteilt:

- **Management-Netz** (192.168.1.0/24)
- **VLAN-Netz** (172.16.0.0/16): Segmentierung über sechs VLANs (VLAN 10–60)

## Kernkomponenten

| Komponente | Funktion |
|---|---|
| Domain Controller | Active Directory, DNS, DHCP für `claudius.local` |
| Fileserver | Zentrale Dateiablage |
| Webserver | Interner/externer Webdienst |
| Backup-Server | Datensicherung |
| Zabbix (Ubuntu) | Netzwerk- und Systemüberwachung |
| pfSense Firewall | Routing, VLAN-Terminierung, Firewall-Regeln, NAT |
| MGMT-PC | Administration von Workstations im Management-Netz |

---
[⬅ Zurück zur Übersicht](../README.md) · [Weiter: Netzplan ➡](02-netzplan.md)
