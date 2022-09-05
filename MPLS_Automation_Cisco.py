#MPLS Automation Code 

###variables===================================================================================###
condition_mpls_interface="y"
list_mpls_interface=[]
###variables===================================================================================###




###inputs===================================================================================###
mpls_router_id=input("Enter MPLS Router-ID Interface (The default is loopback 0) : ")
mpls_password=input("Enter MPLS password (Leave blank if you dont want) : ")
session_protection=input("Do you want to enable session protection? (y/n)")
optimize_ldp_host_routes=input("Do you want to optimize LDp with host-routes? (y/n)")
mpls_label_range=input("Do you want to change mpls label range? (y/n)")
session_protection=input("Do you want to enable session protection? (y/n)")
if mpls_label_range=="y":
    mpls_label_range_from=input("Do you want to change mpls label range start from? ")
    mpls_label_range_to=input("Do you want to change mpls label range end with? ")
sync_igp_ldp=input("Do you want to enable syncronization between your igp and mpls? (y/n)")
if sync_igp_ldp=="y":
    sync_igp_ldp_protocol=input("Do you have ospf or isis?")
    if sync_igp_ldp_protocol=="ospf":
        sync_igp_ldp_protocol_ospf_id=input("What is the proccess id ?")
    else:
        sync_igp_ldp_protocol_isis_id=input("What is the proccess id ??")
while condition_mpls_interface!="n":
    mpls_interface_=input("Enter Interface that you want to contribute in MPLS : ")
    list_mpls_interface.append(mpls_interface_)
    condition_mpls_interface=input("Do You have more? (y/n)")
    if condition_mpls_interface!="y" and condition_mpls_interface!="n":
        print("Please Enter just y or n ")
###inputs===================================================================================###



###codes===================================================================================###
print("(c)2022 Farid Soltani Tehran, Iran. All rights reserved. \n Here are your codes : \n")
print("ip cef")   #should be run because MPLS uses FIB table
if mpls_router_id:
    print("mpls ldp router-id", mpls_router_id)
if mpls_password:
    print("mpls ldp password required \nmpls ldp password fallback",mpls_password) 
if session_protection=="y":
    print("mpls ldp session protection") 
if optimize_ldp_host_routes=="y":
    print("optimize ldp host-routes \n allocate global host-routes ") 
if mpls_label_range=="y":
    print(" mpls label range " , mpls_label_range_from ,  mpls_label_range_to)
for i in list_mpls_interface:
    print("interface", i , "\n  mpls ip",)
if sync_igp_ldp=="y":
    if sync_igp_ldp_protocol=="ospf":
        print("router ospf", sync_igp_ldp_protocol_ospf_id , "\n mpls ldp sync") 
    else:
        print("router isis", sync_igp_ldp_protocol_isis_id , "\n mpls ldp sync") 

###codes===================================================================================###
 


































































q=input("Press q to exit")
while q!="q":
    q=input("Press q to exit")

