# Programming Assignment 1: SDN
## Einfacher Router und Firewall

### Mininet Topologie
2 Hosts pro Subnetz (h1 und h2 bzw. h3 und h4), 1 Switch pro Subnetz  (sw1 und sw2), 1 Host als Router zwischen den beiden Subnetzen (router, vgl. Grafik)

![Topologie](/lab1/topo.png)

### Router
Der Router ist ein Host mit aktiviertem IP-Forwarding.

### Switches
Die Switches implementieren die Funktion der Firewall und das Forwarding in den Subnetzen bzw. zum Router.

### Firewall
Die Firewall lässt grundsätzlich alles durch, was nicht durch einen Eintrag in der Flow-Tabelle blockiert wird.
Um die Kommunikation zwischen zwei Hosts in den beiden Subnetzen zu blockieren, muss eine entsprechende Regel in den beiden Switches hinterlegt werden.

`firewall.addFirewallRule(ofp_datapath,{'src':'10.0.0.2','dst':'10.0.1.2'})`
