from mininet.topo import Topo
from mininet.node import Node
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCIntf
from mininet.node import RemoteController


class CustomTopo(Topo):

  __LINK_BANDWIDTH = 1

  def __init__(self):
      Topo.__init__(self)

  def build(self):

    sw1 = self.addSwitch('sw1', dpid='0000000000000001')

    #sw2 = self.addSwitch('sw2',dpid='0000000000000001')

    router = self.addHost('router', ip='10.0.0.1/24', mac='ba:de:af:fe:01')

    h1 = self.addHost('h1', ip='10.0.0.2/24', defaultRoute='via 10.0.0.1', mac='ba:de:af:fe:00:02')
    
    h2 = self.addHost('h2', ip='10.0.0.3/24', defaultRoute='via 10.0.0.1', mac='ba:de:af:fe:00:03')

    #h3 = self.addHost('h3', ip='192.168.128.2/24', defaultRoute='via 192.168.128.1', mac='ba:de:af:fe:00:04')
    
    #h4 = self.addHost('h4', ip='192.168.128.3/24', defaultRoute='via 192.168.128.1', mac='ba:de:af:fe:00:05')
    
 

    #for node1, node2 in [(h1, sw1), (h2, sw1)]: 
     # self.addLink(node1, node2,
      #             cls1=TCIntf, cls2=TCIntf,
      #             intfName1=node1 + '-' + node2,
      #             intfName2=node2 + '-' + node1,
      #             params1={'bw': self.__LINK_BANDWIDTH},
      #             params2={'bw': self.__LINK_BANDWIDTH},)


    self.addLink(sw1, h1, 11, 1)
    self.addLink(sw1, h2, 12, 1)

    #Connect Router with Switches
    self.addLink (router, sw1, 1, 1, intfName1='router-eth1', params1={'ip':'10.0.0.1/24'})
    #self.addLink (router, sw2, 2, 1, intfName1='router-eth2', params1={'ip':'192.168.128.1/24'})


def run():
  topo = CustomTopo()
  net = Mininet(topo=topo,
                controller=RemoteController('ofp-c1',
                                            ip='127.0.0.1',
                                            port=6633))
  net.start()
  CLI(net)    
  net.stop()


if __name__ == '__main__':
  run()
