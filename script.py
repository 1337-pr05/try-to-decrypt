import requests
import math
key_mapp = {"A":"","B":"","C":"","D":"","E":""
            ,"F":"","G":"","H":"","I":"","J":""
            ,"K":"","L":"","M":"","N":"","O":""
            ,"P":"","Q":"","R":"","S":"","T":""
            ,"U":"","V":"","W":"","X":"","Y":""
            ,"Z":"","a":"","b":"","c":"","d":""
            ,"e":"","f":"","g":"","h":"","i":""
            ,"j":"","k":"","l":"","m":"","n":""
            ,"o":"","p":"","q":"","r":"","s":""
            ,"t":"","u":"","v":"","w":"","x":""
            ,"y":"","z":"","-":"","_":"",".":""
            ,",":"",";":"",":":"","?":""," ":""
            ,"0":"","1":"","2":"","3":"","4":""
            ,"5":"","6":"","7":"","8":"","9":""}
def progres_bar(progress,total):
    percent = 100 * (progress / float(total))
    bar  = "#" * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%",end='\r')

def key_maps():   
    total = 70
    j=0
    url = 'http://api.trytodecrypt.com/encrypt'
    id = int(input("enter the id : "))
    key = input("enter the api-key : ")
    print("--------------------------------------------------------FETCHING THE KEYS----------------------------------------")
    progres_bar(0,total)
    for i in key_mapp.keys():
        j+=1
        params = {
             'key': f'{key}',
             'id': f'{id}',
             'text': f'{i}'
         }
        response = requests.get(url, params=params)
        key_mapp[i] = response.text
        progres_bar(j,total)
       
    print()  
    #print(key_mapp)

def decyper():
    keys = list(key_mapp.keys())
    value = list(key_mapp.values())    
    cypertext = input("enter the cypher text : ")
    ln_ = len(key_mapp['a'])
    j=0
    cypertext = ' '.join(cypertext[i:i+ln_] for i in range(0, len(cypertext), ln_))
    cypher=cypertext.split()
    decyphertext =''
    for i in cypher:
        for j in value:
            if(i==j):
                decyphertext += keys[value.index(j)]

    print("The decypher text : ",decyphertext)
    choice = int(input("do want to print the reverse of it too 1/0 : "))
    if(choice):
        cypher = cypher[::-1]
        decyphertext =''
        for i in cypher:
            for j in value:
                if(i==j):
                    decyphertext += keys[value.index(j)]

    print("The decypher text : ",decyphertext)
        
                    
if __name__ == "__main__":
    print("1 : For find the key _ mapping")               
    print("2 : For decypher text")    
    print("3 : EXIT")  
    while(True):
        choice = int(input("enter the choice : "))
        if(choice == 1):
            key_maps()
            decyper()
        elif(choice==2):
            decyper()       
        elif(choice == 3):
            break    




















