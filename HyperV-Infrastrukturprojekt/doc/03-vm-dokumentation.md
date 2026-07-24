# VM-Dokumentation

> ⚠️ Die unten aufgeführten Zugangsdaten stammen aus einer rein virtuellen Testumgebung. Vor einer Veröffentlichung in einem öffentlichen Repository sollten sie durch Platzhalter ersetzt werden.

## Domain Controller

| | |
|---|---|
| **Hostname** | dc.claudius.local |
| **Domäne** | claudius.local |
| **IPv4** | 192.168.1.1 /24 |
| **IPv6** | fd12:3456:789a:1::1 /64 |
| **Gateway** | 192.168.1.254 |
| **DNS** | 192.168.1.1 (local host) |
| **Username** | Administrator |
| **Passwort** | `Domain12345#` |
| **DSRM-Passwort** | `IchbineinDC123#` |
| **Rollen** | Active Directory DS, DNS-Server, DHCP-Server |

## Fileserver

| | |
|---|---|
| **IPv4** | 192.168.1.2 /24 |
| **IPv6** | fd12:3456:789a:1::2 /64 |
| **Gateway** | 192.168.1.254 |
| **DNS** | 192.168.1.1 |
| **Username** | Administrator |
| **Passwort** | `Fileserver12345#` |
| **Rollen** | Dateiserver (Freigaben, NTFS-Berechtigungen) |

## Webserver

| | |
|---|---|
| **IPv4** | 192.168.1.3 /24 |
| **IPv6** | fd12:3456:789a:1::3 /64 |
| **Gateway** | 192.168.1.254 |
| **DNS** | 192.168.1.1 |
| **Username** | Administrator |
| **Passwort** | `Webserver12345#` |
| **Rollen** | Webdienst (intern/extern via Port-Forwarding) |

## Backup-Server

| | |
|---|---|
| **IPv4** | 192.168.1.4 /24 |
| **IPv6** | fd12:3456:789a:1::4 /64 |
| **Gateway** | 192.168.1.254 |
| **DNS** | 192.168.1.1 |
| **Username** | Administrator |
| **Passwort** | `Backupserver12345#` |
| **Rollen** | Datensicherung |

## Zabbix Monitoring (Ubuntu)

| | |
|---|---|
| **IPv4** | 192.168.1.5 /24 |
| **Gateway** | 192.168.1.254 |
| **DNS** | 192.168.1.1 |
| **Root-Login** | `root` / `zabbix` |
| **Web-GUI Login** | `Admin` / `zabbixadmin12345` |
| **Web-GUI URL** | http://192.168.1.5/zabbix |
| **Rollen** | Monitoring-Dashboard |

## Firewall

Als Firewall-Lösung dient die Open-Source-Lösung **pfSense**.

![pfSense Dashboard](../images/pfsense-dashboard.jpeg)

| | |
|---|---|
| **Hostname** | fw01.claudius.local |
| **Admin-Username** | admin |
| **Admin-Passwort** | `pfsenseadmin` |
| **MGMT-Interface** | 192.168.1.254 /24 |
| **Aufgaben** | Routing, VLAN-Terminierung, Firewall-Regelwerk, DHCP-Relay, NAT, WAN-Verbindung, VPN-Tunnel |

### DHCP-Relay-Konfiguration (gleich für jedes Routed VLAN Interface)

![DHCP-Relay-Konfiguration](../images/dhcp-relay-konfiguration.jpeg)

### Firewall-Regeln

![Firewall-Regeln](../images/firewall-regeln.png)

### IPsec-Tunnel

![IPsec-Tunnel](../images/ipsec-tunnel.png)

## MGMT-PC

| | |
|---|---|
| **IPv4** | 192.168.1.253 /24 |
| **Username** | MGMT |
| **Passwort** | `MGMT12345#` |
| **Zweck** | Lokale Administrations-Workstation im Management-Netz |

---
[⬅ Zurück: Netzplan](02-netzplan.md) · [Übersicht](../README.md) · [Weiter: Host-Maschine ➡](04-host-maschine.md)
