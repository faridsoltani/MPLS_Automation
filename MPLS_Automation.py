#MPLS Automation Code 
Router_LSR_ID=input("Enter Router LSR-ID : ")
print("Here is your code : ")
print("""
mpls lsr-id {0}
mpls
mpls ldp
q
mpls ldp 
q
save 
y

""".format(Router_LSR_ID))
input("Press enter to exit")
