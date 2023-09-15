from netmiko import ConnectHandler


HOST = "Ix" #host name 
USER = "shinnok" #username to access the router 
PASS = "Teresa27272727" #authentication password 
TYPE = "winntX" #device type 

#using netmiko's CopnnectHandler initiate a connection to the device 
r1 – ConnectHandler (host=HOST, username=USER, password=PASS, device_type=TYPE
