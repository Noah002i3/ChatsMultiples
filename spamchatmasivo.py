import aminofix as amino, concurrent.futures
import pyfiglet, colorama

print(colorama.Fore.GREEN)
print(pyfiglet.figlet_format("Spam", font="slant"))
print("      [Creditos] [Noah] ")

print(colorama.Fore.GREEN)
client=amino.Client()
client.login(email=input(" - Email: "), password=input(" - Contraseña: "))
coms=client.sub_clients(size=100)
for x, name in enumerate(coms.name, 1):
    print(f"{x}.{name}")
com_Id = coms.comId[int(input("\nSelecciona la comunidad: ")) - 1]
sub_client=amino.SubClient(comId=com_Id, profile=client.profile)
chat=int(input(" - Chats: "))
message= """[bc]🍑 𝗽.⍺𝗋̼⍺𝖉¡𝗌ɘ ٬٬🔥

[Cui] Está comunidad está hecha para ti...~ ven a rolear incluso LEMON!🍋 Que esperas baby?~

[ibc]http://aminoapps.com/invite/WDL30N1FB3"""

titulo = "VEN AMOR 🍑 𝗽.⍺𝗋̼⍺𝖉¡𝗌ɘ ٬٬🔥"

def chatsxd():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
        usersIdxd=sub_client.get_online_users(start=0, size=1000).profile.userId
        userrecent = sub_client.get_all_users(start=0, size=1000, type= "recent").profile.userId
        userrecenteso = sub_client.get_all_users(start=400, size=1000, type= "recent").profile.userId
        userscomplete = [*usersIdxd, *userrecent, *userrecenteso]
        if userscomplete:
            for userId in userscomplete:
                for i in range(chat):
                    try:
                        sub_client.start_chat(userId=userscomplete, message="")
                        chats = sub_client.get_chat_threads(start=0, size=150)
                        for chat_id , title in zip(chats.chatId,chats.title):
                            sub_client.edit_chat(chatId=chat_id,title=titulo,viewOnly=200)
                            sub_client.send_message(chatId=chat_id,message=message)
                    except Exception as e:
                        print(e)
                        pass
                    else:
                        break
                        
 
chatsxd()