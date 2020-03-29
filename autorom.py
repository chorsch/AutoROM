import requests
from bs4 import BeautifulSoup
import os
import ale_py


install_dir = ale_py.__file__
install_dir = install_dir[:-11] + "ROM/"

game_list = ["Adventure", "AirRaid", "Alien", "Amidar", "Assault", "Asterix", "Asteroids", "Atlantis",
"BankHeist", "BattleZone", "BeamRider", "Berzerk", "Bowling", "Boxing", "Breakout","Carnival",
"Centipede", "ChopperCommand","CrazyClimber","Defender","DemonAttack","DonkeyKong",
"DoubleDunk","ElevatorAction","Enduro", "FishingDerby","Freeway","Frogger","Frostbite",
"Galaxian","Gopher","Gravitar","Hero","IceHockey","JamesBond","JourneyEscape","Kaboom",
"Kangaroo","KeystoneKapers","Kingkong","Koolaid","Krull","KungFuMaster","LaserGates",
"LostLuggage","MontezumaRevenge","MrDo","MsPacman","NameThisGame","Phoenix","Pitfall",
"Pong","Pooyan","PrivateEye","QBert", "RiverRaid","RoadRunner","RoboTank","Seaques",
"SirLancelot","Skiing","Solaris","SpaceInvaders","StarGunner","Tennis",
"Tetris","TimePilot","Trondead","Turmoil","Tutankham","UpNDown","Venture",
"VideoPinball","WizardOfWor","YarsRevenge","Zaxxon"]

total_sublink_list = []

# top_url = "https://www.gamulator.com/roms/atari-2600"
# for payload_val in range(1,7):
#     payload = {"currentpage":str(payload_val)}
#     r = requests.get(top_url, params=payload)
#     soup = BeautifulSoup(r.content, "html5lib")
#     links = soup.findAll("a")
#     links = filter(lambda x: x.get("class") == None, links)
#     links = filter(lambda x: x.get("href").startswith("/roms/atari-2600"), links)
#     links = filter(lambda x: x.find_all("picture") == [],links)
#     for l in links:
#         sub_href = l["href"]
#         sub_href = sub_href[16:]
#         new_url = top_url + sub_href+"/download"
#         sub_url = requests.get(new_url)
#         sub_soup = BeautifulSoup(sub_url.content, "html5lib")
#         sub_links = sub_soup.find_all("a")
#         sub_links = filter(lambda  x: x.get("href").startswith("https://downloads"), sub_links)
#         # should only be 1 link
#         # for s in sub_links:
#         #     download_link = s.get("href")
#         #     download_req = requests.get(download_link)
#         #     file_title = root_dir + sub_href
#         #     open(file_title,"wb").write(download_req.content)
#         for s in sub_links:
#             total_sublink_list.append(s.get("href"))
#     print("Scraped page ", payload_val)

link_file = open("links.txt", "r")
extension_map = {}
for l in link_file:
    mod_link = l.strip()
    total_sublink_list.append(mod_link)
    extension_type = mod_link[-4:]
    extension_map[mod_link] = extension_type

def simplifyUrl(u):
    n = u[37:]
    return n.replace(" ","")

simplified_map = map(simplifyUrl, total_sublink_list)
total_sublink_dict = dict(zip(list(simplified_map), total_sublink_list))
final_map = {}
for g in game_list:
    found = False
    for t in total_sublink_dict:
        if t.startswith(g):
            final_map[g] = total_sublink_dict[t]
            found = True
            break
    # if not found:
    #     print("Could not find URL for ", g)

print("Before installing the ROMs, please respond Y or N to the following agreements.")
ans = input("I have a license to download and own ROMs for the Atari 2600 (Y or N)")
if ans != "Y" and ans != "y":
    quit()
ans = input("I have a license to a proper emulator (Y or N)")
if ans != "Y" and ans != "y":
    quit()
ans = input("I will not distribute the ROMs (Y or N)")
if ans != "Y" and ans != "y":
    quit()
ans = input("The following directory will be created: " + install_dir + " (Y or N)")
if ans != "Y" and ans != "y":
    quit()
os.mkdir(install_dir)
for game_name in final_map:
    download_page = requests.get(final_map[game_name])
    file_title = install_dir + game_name + extension_map[final_map[game_name]]
    open(file_title,"wb").write(download_page.content)
    print("Installed ",game_name)
