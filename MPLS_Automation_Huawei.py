#MPLS Automation Code 
Router_LSR_ID=input("Enter Router LSR-ID : ")
mpls_interface_0=input("Enter Interfaces that you want to contribute in MPLS : ")
mpls_interface_1=input("Enter Interfaces that you want to contribute in MPLS : ")
mpls_interface_2=input("Enter Interfaces that you want to contribute in MPLS : ")
print("(c)2022 Farid Soltani Tehran, Iran. All rights reserved. \n Here is your code : ")
print("""
mpls lsr-id {0}
mpls
q
mpls ldp
interface {1}
mpls
mpls ldp
interface {2}
mpls
mpls ldp
interface {3}
mpls
mpls ldp











""".format(Router_LSR_ID,mpls_interface_0,mpls_interface_1,mpls_interface_2))
input("Press enter to exit")
