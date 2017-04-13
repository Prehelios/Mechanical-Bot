import mechanicalsoup


print ("\n")
print ("\t#####################################################################")
print ("\t#                                                                   #")                                 
print ("\t#             TBOTBOTBOT      BOTBOT    OTBOTBOTBOTB                #")     
print ("\t#             TBOTBOTBOTB    TBOTBOTB   OTBOTBOTBOTB                #")                                                       
print ("\t#             TBOTB   OTB   OTBO  OTBO  OTB  BOT  TB                #")                                                                                                                                                            
print ("\t#               OTB   OTB   OTB    TBO       BOT                    #")                                                                      
print ("\t#               OTBOTBOTB  BOTB    TBOT      BOT                    #")                                                                              
print ("\t#               OTBOTBOTBO BOTB    TBOT      BO                     #")                                                     
print ("\t#               OTBOTBOTBOT OTB    TBO       BOT                    #")                                             
print ("\t#               OTB    TBOT OTB    TBO       BOT                    #")
print ("\t#               OTBOTBOTBOT OTBO  OTBO       BOT                    #")     
print ("\t#             TBOTBOTBOTBO   TBOTBOTB      OTBOTBO                  #")
print ("\t#             TBOTBOTBOTB     BOTBOT       OTBOTBO                  #")
print ("\t#                                                                   #")
print ("\t#                 Initiation à l'automatisation                     #")
print ("\t#                                                                   #")
print ("\t#####################################################################")

u = input("Entrez votre pseudo : ")
p = input("Entrez votre mot de passe : ")

browser = mechanicalsoup.Browser()

URL = 'https://github.com/login'

user = {
    "username": u,
    "password": p
}

page_formulaire = browser.get(URL)

formulaire = page_formulaire.soup.select("form")[0]

formulaire.select("#login_field")[0]['value'] = user['username']
formulaire.select("#password")[0]['value'] = user['password']

page_accueil = browser.submit(formulaire, URL)

print(str(page_accueil.text))

print ("\t#####################################################################")
print ("\t#####################################################################")
print ("\t#####################################################################")

page_informations = browser.get("https://github.com/settings/profile")

print (page_informations.soup.title.text)
