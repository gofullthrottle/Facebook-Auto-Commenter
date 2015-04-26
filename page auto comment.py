import fb 
from facepy import GraphAPI 

import time


token="CAACEdEose0cBAJfGtXJvZAUMsuGr5ZBXw4FZAozj4jHNggbymdPwWf0EQUmaaivmjcRpZAySL1qZAT9s4b0IKRrQuurMYfTZBIuvUdJZCf3ZAbiMlJZAHxCJDmJZBXGWh5uH1Cau2uuLHd9yG6AfdJpJvFFtLZBL3E6b2wcx0OlxmzylDGqwNxoWGJ1hf9l7lPYGgisrDTv6jQn5SJZCxWaZBaiO65erQM9vleNQZD"#Insert access token here.  
facebook=fb.graph.api(token)
graph1 = GraphAPI(token)


vid=340022612868386 
query=str(vid)+"/posts?fields=id&limit=5000000000"
r=graph1.get(query)



idlist=[x['id'] for x in r['data']]
print("There are "+ str(len(idlist)) +" commentable posts.")

char1='y'
count=0
if char1=='y':
    nos=input("Enter number of posts to be commented on: ")
    if nos<=len(idlist):
       for indid in idlist[len(idlist)-(nos):len(idlist)-1]:
    	  count=count+1
          facebook.publish(cat="comments",id=indid,message="Haii")
	  time.sleep(6)
	  
          
          print("Complaint number:"+str(count)+" on www.facebook.com/"+str(indid).split('_')[0]+"/posts/"+str(indid).split('_')[1])	  
    else: 
          print("Not that many commentable posts available. ")
else :
  print("No complaints made.")