# Netzplan

## Management-Netz

| | |
|---|---|
| **Subnetz IPv4** | 192.168.1.0 / 255.255.255.0 (/24) |
| **Subnetz IPv6** | fd12:3456:789a:1::/64 |
| **Standard-Gateway IPv4** | 192.168.1.254 (pfSense MGMT-Interface) |
| **Standard-Gateway IPv6** | fd12:3456:789a:1::ffff (pfSense MGMT-Interface) |
| **DNS-Server** | 192.168.1.1 (Domain Controller) |

## VLAN-Segmentierung / DHCP-Adressierung

> **Hinweis:** Die ersten 10 Adressen jedes Subnetzes sowie die letzte Adresse (.254, Routed VLAN Interface auf pfSense) sind reserviert.

| VLAN-ID | Abteilung | Subnetz | Nutzbare Hosts |
|---|---|---|---|
| VLAN 10 | HR | 172.16.10.0 /24 | 172.16.10.11 – .253 |
| VLAN 20 | IT | 172.16.20.0 /24 | 172.16.20.11 – .253 |
| VLAN 30 | Verwaltung | 172.16.30.0 /24 | 172.16.30.11 – .253 |
| VLAN 40 | Marketing | 172.16.40.0 /24 | 172.16.40.11 – .253 |
| VLAN 50 | Produktion | 172.16.50.0 /24 | 172.16.50.11 – .253 |
| VLAN 60 | Gäste | 172.16.60.0 /24 | 172.16.60.11 – .253 |

### DHCP-Übersicht

![DHCP-Übersicht](../images/dhcp-overview.png)

### DHCP-Pool (für VLAN10)

![DHCP-Pool für VLAN10](../images/dhcp-pool-vlan10.png)

### DHCP-Optionen (für VLAN10)

![DHCP-Optionen für VLAN10](../images/dhcp-options-vlan10.png)

## Routed VLAN Interfaces

| VLAN | Interface-IP |
|---|---|
| HR (VLAN 10) | 172.16.10.254 /24 |
| IT (VLAN 20) | 172.16.20.254 /24 |
| Verwaltung (VLAN 30) | 172.16.30.254 /24 |
| Marketing (VLAN 40) | 172.16.40.254 /24 |
| Produktion (VLAN 50) | 172.16.50.254 /24 |
| Gäste (VLAN 60) | 172.16.60.254 /24 |

![Routed VLAN Interfaces – Konfiguration 1](../images/routed-vlan-interfaces-1.png)
![Routed VLAN Interfaces – Konfiguration 2](../images/routed-vlan-interfaces-2.png)

## Topologie

![Netzwerktopologie](../images/topologie.jpeg)

---
[⬅ Zurück: Projektbeschreibung](01-projektbeschreibung.md) · [Übersicht](../README.md) · [Weiter: VM-Dokumentation ➡](03-vm-dokumentation.md)
