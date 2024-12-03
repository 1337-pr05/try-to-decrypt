import requests
import math

cipher_text = {
                                        # id : "cipher=text"
    # "easy"
        1:"131017171A48221A1D170F",
        2:"4A3E374A4973483F3D3E4A",
        3:"0A0B1339150B1139070A0B13390510",
        4:"0C02D8010D0C02D8010606D8101402FCD80F0603D8FC0600DA",
        5:"90DE633F425148DE51546CDE725466DE3F2A6936DE4263CCDEAB362A3372DE39545DDE633F36DE51366F63DE545136D8",
        6:"4D586CFC2DB449D47B0CF99C3BC46CFC7B0C",
    
    # "medium"
        7:"21052F151200271512413E35101A152F3511",
        8:"eaidagdagenpmgodlceijmgoefodlceijcnllonmgodlcfilfgamgodnnflgfgafilmgofildihdagmgoefodlccnlcnledddagmgoedddagfobdagedd",
        9:"6224F12C1C3FAA5AA54836B3C446D6415E74",
        10:"261129152E152B",
        11:"90DE633F425148DE51546CDE725466DE3F2A6936DE4263CCDEAB362A3372DE39545DDE633F36DE51366F63DE545136D8",
        12:"3785824AD56B2531A7150DF44C21434A61E63F040A42F2012BC2F43F0AD535D24D46013213866D7E0",
    
    # "hard"
        13:"59656A6B6F9F656A67746767",
        14:"6F5657A6606B7D9C7480649D7A6B757D9C70816B6CB4",
        15:"574168755997984F7A7E76AD6954A662538F764F7A5C4F876544",
        16:"32632E3149844B82115794BA78AD87C36DA01148707080C65459255C2C6487B02851",
        17:"5D2EAF346C9271B7489BBA3A52326752248C2255826771378D741E48205A",
        18:"35445FA0D18F47618981AE5D3A98A5138EAE2A303A5D688B6C4461703B902F308F5F125F7725",
        
    # "too_much"
        19:"5F70017FDD92B75AA6668648B404223663157787B35686FA165A8193E5075777F",
        20:"8221E4F2173368D6B6B6E5050935D986A8C4CA764CF8A8C4B734E99807140B19DB691998095CC4E3D6C60D6E91",
        21:"333131353156333131323231305230363135315631333151342F3430313131323154342F",
        22:"00100401400A0120A101C0310F503706004E05B0870A00880D80ED0BE1262890FD16816A1453453721963ED1D11F04624D9",
        23:"E3F59F001361B62958E551B9702F2C6B25F9E3FC350062295A1A20182041493C447BA0767A393A1F278DB14268565F51575C65212A8386494B383F7375676845472F30494C737A406890988B8D50577A835960476B6F73686E6367668B787A494C33357EA4555E191C18216A6F353A173E2026474A8A8C3F481416759D"     
    
}


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
def intro():
    print("1 : For find the key - mapping")                
    print("2 : For decypher text")    
    print("3 : EXIT")  
    
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
    print("\t--------------------------------------------------------FETCHING THE KEYS----------------------------------------")
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
       
    decyper(id)  
    #print(key_mapp)

def decyper(id):
    keys = list(key_mapp.keys())
    value = list(key_mapp.values())    
    cypertext = cipher_text[id]
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

    while(True):
        intro()
        choice = int(input("enter the choice : "))
        if(choice == 1):
            key_maps()
        elif(choice==2):
            id = int(input("Enter the id (Remember Input the ID who's keys are mapped)"))
            decyper()       
        elif(choice == 3):
            break    




















