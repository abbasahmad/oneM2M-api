
### Ressources types ###
### AE ty=2 ###
### Container ty=3 ###
### ContentInstance ty=4 ###
### Subscription ty=23 ###

###ACP (Additionate for right attribution)
###63 gives CREATE, RETRIEVE, UPDATE, DELETE, DISCOVERY and NOTIFY rights
###Value		Interpretation 	
###1			CREATE 
###2		 	RETRIEVE 
###4 			UPDATE 
###8		 	DELETE 
###16 		NOTIFY 
###32		 	DISCOVERY 


### Notification TYPE for Subscription ###
###Net = notificationEventType 
### 1 	Update_of_Resource
### 2 	Delete_of_Resource 
### 3 	Create_of_Direct_Child_Resource 
### 4 	Delete_of_Direct_Child_Resource 


###	API CALLs EXAMPLES
### python oneM2M_basics.py createACP http://127.0.0.1:8080 egmACP egm:abbas 63 
### python oneM2M_basics.py createAE http://127.0.0.1:8080 egm.smartparking.tropfort ParkingSpot [/in-cse/acp-609336319]
### python oneM2M_basics.py createContainer egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot Spot1
### python oneM2M_basics.py createContentInstance egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1 free
### python oneM2M_basics.py getContentInstanceLatest egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1
### python oneM2M_basics.py createSubscription egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1 ParkingSpotsSubs http://127.0.0.1:6000 1
### python oneM2M_basics.py deleteContentInstanceLatest egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1
### python oneM2M_basics.py deleteContainer egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1
### python oneM2M_basics.py deleteAE egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot