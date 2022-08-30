#MPLS Automation Code 
mpls_router_id=input("Enter MPLS Router-ID Interface (The default is loopback 0) : ")
mpls_interface_0=input("Enter Interfaces that you want to contribute in MPLS : ")
mpls_interface_1=input("Enter Interfaces that you want to contribute in MPLS : ")
mpls_interface_2=input("Enter Interfaces that you want to contribute in MPLS : ")
print("(c)2022 Farid Soltani Tehran, Iran. All rights reserved. \n Here is your code : \n")
print("ip cef")   #should be run because MPLS uses FIB table
print("""                             
mpls ldp router-id {0}
interface {1}
mpls ip
interface {2}
mpls ip
interface {3}
mpls ip
""".format(mpls_router_id,mpls_interface_0,mpls_interface_1,mpls_interface_2))
input("Press enter to exit")
