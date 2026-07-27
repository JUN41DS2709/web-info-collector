import requests as req 
import time


#input from user 

print("WEBUFO - WEB INFO COLLECTOR\n")
url = input("Enter a url : ") 


session = req.session()
start = time.time()
r = session.get(url)
end = time.time()
print("provided url : " , url)
print("status code : ",  r.status_code)
print(f'Response Time: {end - start:.2f} seconds')
headers = r.headers
try : 
    print(f"Date : {headers['Date']}")
    print(f"Server : {headers['server']}") 
    print(f"Content-Type : {headers['Content-Type']}")
    print(f"Content-Length : {headers['Content-Length']}")
    print(f"Content-Encoding : {headers['Content-Encoding']}")
    print(f"Connection : {headers['Connection']}")
    print(f"Cache-Control : {headers['Cache-Control']}")
except KeyError:
    print("No Such headers ! host is using customized headers..")
else:
 for key , value  in headers.items():
    print(key , ":" ,value)


print("here is all the information enjoy")
