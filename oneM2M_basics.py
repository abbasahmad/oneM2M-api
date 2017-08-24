#!/usr/bin/python

### Ressources types ###
### AE ty=2 ###
### Container ty=3 ###
### ContentInstance ty=4 ###
### Subscription ty=23 ###


#ACP (Additionate for right attribution)
#63 gives CREATE, RETRIEVE, UPDATE, DELETE, DISCOVERY and NOTIFY rights
#Value		Interpretation 	
#1			CREATE 
#2		 	RETRIEVE 
#4 			UPDATE 
#8		 	DELETE 
#16 		NOTIFY 
#32		 	DISCOVERY 


### Notification TYPE for Subscription ###
#Net = notificationEventType 
# 1 	Update_of_Resource
# 2 	Delete_of_Resource 
# 3 	Create_of_Direct_Child_Resource 
# 4 	Delete_of_Direct_Child_Resource 


#	API CALLs EXAMPLES
# python oneM2M_basics.py createACP http://127.0.0.1:8080 egmACP egm:abbas 63 
# python oneM2M_basics.py createAE http://127.0.0.1:8080 egm.smartparking.tropfort ParkingSpot [/in-cse/acp-609336319]
# python oneM2M_basics.py createContainer egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot Spot1
# python oneM2M_basics.py createContentInstance egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1 free
# python oneM2M_basics.py getContentInstanceLatest egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1
# python oneM2M_basics.py createSubscription egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1 ParkingSpotsSubs http://127.0.0.1:6000 1
# python oneM2M_basics.py deleteContentInstanceLatest egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1
# python oneM2M_basics.py deleteContainer egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot/Spot1
# python oneM2M_basics.py deleteAE egm:abbas http://127.0.0.1:8080/in-name/ParkingSpot

import sys
import requests
import json
import random

NUM_ARG=len(sys.argv)
COMMAND=sys.argv[0]


def handleResponse(r):
	print (r.status_code)
	print (r.headers)
	print (r.text)
	return;

##	Create <ACP> 	###
def createACP(url,rn_value,pv_acor_value,pv_acop_value):
	print("Creating <ACP>")
	payload = '{ "m2m:acp": {\
        "rn": "'+rn_value+'",\
          "pv": {\
            "acr": {\
              "acor": ["'+pv_acor_value+'"],\
              "acop": "'+pv_acop_value+'"\
            }\
          },\
          "pvs": {\
            "acr": {\
              "acor": ["'+pv_acor_value+'"],\
              "acop": "'+pv_acop_value+'"\
            }\
          }\
       }\
    }'
	_headers =   {'X-M2M-Origin': 'admin:admin','Content-Type': 'application/json;ty=1'}
	json.dumps(json.loads(payload,strict=False),indent=4)
	r = requests.post(url.strip(),data=payload,headers=_headers)
	handleResponse(r);
	return r;

###	Create an <AE>	###	
def createAE(CSEurl,api_value,rn_value,acpi_value):
	print("Creating <AE> with resourceName and point of access attributes")
	payload = '{ \
	    "m2m:ae": { \
	   "api": "'+api_value+'", \
	    "rr": "true", \
	    "rn": "'+rn_value+'", \
	    "acpi": "'+acpi_value+'" \
	    } \
	}'
	_headers =   {'X-M2M-Origin': '','Content-Type': 'application/json;ty=2'}
	json.dumps(json.loads(payload,strict=False), indent=4)
	r = requests.post(CSEurl.strip(),data=payload,headers=_headers)
	handleResponse(r)
	return r;
	
###	Create a <Container>	###
def createContainer(origin,AEurl,rn_value):
	print("Creating <container>")
	payload = '{ \
	    "m2m:cnt": { \
            "rn": "'+rn_value+'" \
	    } \
	}'
	_headers =   {'X-M2M-Origin': origin,'Content-Type': 'application/json;ty=3'}
	json.dumps(json.loads(payload,strict=False), indent=4)
	r = requests.post(AEurl.strip(),data=payload,headers=_headers)
	handleResponse(r)
	return r;

###	Create a <ContentInstance> with mandatory attributes	###
def createContentInstance(origin,CONurl,con_value):
	print("Creating <contentInstance>")
	payload = '{ \
	    "m2m:cin": { \
	    "con": "'+con_value+'" \
	    } \
	}'
	_headers =   {'X-M2M-Origin': origin,'Content-Type': 'application/json;ty=4'}
	json.dumps(json.loads(payload,strict=False), indent=4)
	r = requests.post(CONurl.strip(),data=payload,headers=_headers)
	handleResponse(r)
	return r;

###	Get latest <ContentInstance>	###
def getContentInstanceLatest(origin,CONurl):
	print("Getting Latest  <contentInstance>")
	_headers =   {'X-M2M-Origin': origin,'Accept': 'application/json'}
	r = requests.get(CONurl.strip(),headers=_headers)
	handleResponse(r)
	return r;

###	Create <Subscription> with mandatory attributes	###
def createSubscription(origin,CONurl,rn_value,nu_value,net_value):
	print("Creating <Subscription> with mandatory attributes")
	payload = '{ \
	"m2m:sub": { \
		"rn": "'+rn_value+'", \
		 "enc": {\
			"net": "'+net_value+'" \
		} ,\
		"nu": "'+nu_value+'", \
		"nct": "1" \
		} \
	}'
	_headers =   {'X-M2M-Origin': origin,'Content-Type': 'application/json;ty=23'}
	json.dumps(json.loads(payload,strict=False),indent=4)
	r = requests.post(CONurl.strip(),data=payload,headers=_headers)
	handleResponse(r)
	return r;

###	Delete Latest <ContentInstance>	###
def deleteContentInstanceLatest(origin,CONurl):
	print("Deleting Latest  <contentInstance>")
	_headers =   {'X-M2M-Origin': origin}
	r = requests.delete(CONurl.strip(),headers=_headers)
	handleResponse(r)
	return r;
	
###	Delete <Container>	###
def deleteContainer(origin,CONurl):
	print("deleting  <Container>")
	_headers =   {'X-M2M-Origin': origin}
	r = requests.delete(CONurl.strip(),headers=_headers)
	handleResponse(r)
	return r;
	
###	Delete  <AE>	###
def deleteAE(origin,AEurl):
	print("Deleting  <AE>")
	_headers =   {'X-M2M-Origin': origin}
	r = requests.delete(AEurl.strip(),headers=_headers)
	handleResponse(r)
	return r;

def main():
	if(sys.argv[1]=="createACP") :
		if NUM_ARG==6:
			url=sys.argv[2]
			rn_value=sys.argv[3]
			pv_acor_value=sys.argv[4]
			pv_acop_value=sys.argv[5]
			createACP(url,rn_value,pv_acor_value,pv_acop_value)
		else :
			print ('Usage: '+COMMAND+' createACP [CSE_URL] [ACP_NAME] [ACOR] [ACOP]')		
	elif(sys.argv[1]=="createAE") :
			if NUM_ARG==6:
				url=sys.argv[2]
				api_value=sys.argv[3]
				rn_value=sys.argv[4]
				acpi_value=sys.argv[5]
				createAE(url,api_value,rn_value,acpi_value)
			else :
				print ('Usage: '+COMMAND+' createAE [AE_URL] [API_NAME] [AE_RESOURCE_NAME] [DYNAMIC_ACPI]')
	elif(sys.argv[1]=="createContainer") :
		if NUM_ARG==5:
			origin=sys.argv[2]
			url=sys.argv[3]
			rn_value=sys.argv[4]
			createContainer(origin,url,rn_value)
		else :
			print ('Usage: '+COMMAND+' createContainerrn [ORIGIN]  [AE_URL] [CON_RESOURCE_NAME]')
	elif(sys.argv[1]=="createContentInstance") :
		if NUM_ARG==5:
			origin=sys.argv[2]
			url=sys.argv[3]
			con_value= sys.argv[4]
			createContentInstance(origin,url,con_value)
		else :
			print ('Usage: '+COMMAND+' createContentInstance [ORIGIN] [URL]  [CONTENT]')
	elif(sys.argv[1]=="getContentInstanceLatest") :
		if NUM_ARG==4:
			origin=sys.argv[2]
			url=sys.argv[3]+'/la'
			getContentInstanceLatest(origin,url)
		else :
			print ('Usage: '+COMMAND+' getContentInstanceLatest [ORIGIN] [URL]  ')
	elif(sys.argv[1]=="createSubscription") :
		if NUM_ARG==7:
			origin=sys.argv[2]
			url=sys.argv[3]
			rn_value=sys.argv[4]
			nu_value=sys.argv[5]
			net_value=sys.argv[6]
			createSubscription(origin,url,rn_value,nu_value,net_value)
		else :
			print ('Usage: '+COMMAND+' createSubscription [ORIGIN]  [URL] [SUBSCRIPTION_NAME] [NOTIFICATION_URL] [NET] ')
	elif(sys.argv[1]=="deleteContentInstanceLatest") :
		if NUM_ARG==4:
			origin=sys.argv[2]
			url=sys.argv[3]+'/la'
			deleteContentInstanceLatest(origin,url)
		else :
			print ('Usage: '+COMMAND+' deleteContentInstanceLatest [ORIGIN] [URL]  ')
	elif(sys.argv[1]=="deleteContainer") :
		if NUM_ARG==4:
			origin=sys.argv[2]
			url=sys.argv[3]
			deleteContainer(origin,url)
		else :
			print ('Usage: '+COMMAND+' deleteContainer [ORIGIN] [URL]  ')
	elif(sys.argv[1]=="deleteAE") :
		if NUM_ARG==4:
			origin=sys.argv[2]
			url=sys.argv[3]
			deleteAE(origin,url)
		else :
			print ('Usage: '+COMMAND+' deleteAE [ORIGIN] [URL]')
	else:
		print ('Bad command')
		sys.exit(2)
		
if __name__ == "__main__":
    main()
