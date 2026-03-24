import subprocess
import time
import json

# bot 1
idtest = 1480115319698886750
placetest = 'test'
place1 = 'KMWQ'
place2 = 'MXDAY'
place3 = 'WUSWI'
bot1_config = {
    "place": placetest,
    "channel_idbg": idtest,
    "channel_idsign": idtest,
    "channel_idplat": idtest,
    "channel_idconsumable": idtest,
    "channel_idblock": idtest,
    "channel_idguild": idtest,
    "channel_test": idtest,
    "channel_iddoor": idtest,
    "channel_cooktools": idtest,
    "channel_winterfest": idtest,
    "channel_ubiweek": idtest,
    "channel_carni": idtest,
    "channel_valentine": idtest,
}
# bot1_config = {
#     "place": place1,
#     "channel_idbg": 782718523629633567,
#     "channel_idsign": 846661246303469598,
#     "channel_idplat": 846673193426354176,
#     "channel_idconsumable": 847201895873118218,
#     "channel_idblock" : 1104057271215984741,
#     "channel_idguild"   : 762435449909542942,
#     "channel_test"  : idtest,
#     "channel_iddoor" :846671811223355402,
#     "channel_cooktools" :737429783201447937,
#     "channel_winterfest" :784189920742342688,
#     "channel_ubiweek":997609617410490418,
#     "channel_carni":712744557519044719,
#     "channel_valentine":806455698014732318,

# }

#  Bot 2
bot2_config = {
    "place": place2,
    "channel_idbg": 782718523629633567,
    "channel_idsign": 846661246303469598,
    "channel_idplat": 846673193426354176,
    "channel_idconsumable": 847201895873118218,
    "channel_idblock" : 1104057271215984741,
    "channel_idguild"   : 900847998320406599,
    "channel_iddoor" :846671811223355402,
    "channel_test"  : 1384782210090926226,
    "channel_cooktools" :737429783201447937,
    "channel_winterfest" :784189920742342688,
    "channel_ubiweek":997609617410490418,
    "channel_carni":712744557519044719,
    "channel_valentine":806455698014732318,
    "channel_idclash":762435449909542942,

}

bot3_config = {
    "place": place3,
    "channel_idbg": 782718523629633567,
    "channel_idsign": 846661246303469598,
    "channel_idplat": 846673193426354176,
    "channel_idconsumable": 847201895873118218,
    "channel_idblock" : 1104057271215984741,
    "channel_idguild"   : 762435449909542942,
    "channel_iddoor" :846671811223355402,
    "channel_test"  : 1384782210090926226,
    "channel_cooktools" :737429783201447937,
    "channel_winterfest" :784189920742342688,
    "channel_ubiweek":997609617410490418,
    "channel_carni":712744557519044719,
    "channel_valentine":806455698014732318,

}
def run_bot(filename, config_dict):
    config_json = json.dumps(config_dict)
    subprocess.Popen(["python", filename, config_json])
# tskip = 2
# tskipx = 3

# skip =int(input("c"))

# if skip == tskip :
#         run_bot("tesa copy.py", bot2_config)
#         time.sleep( 10 * 60 )
#         run_bot("tesa copy 2.py", bot3_config)

# elif skip == tskipx :
#         run_bot("tesa copy 2.py", bot3_config)


# else :

print("Menyalakan bot1.py...")
run_bot("tesa.py", bot1_config)

# print("Menunggu 30 menit untuk bot2...")
# time.sleep( 10 * 60 )

# print("Menyalakan bot2.py...")
# run_bot("tesa copy.py", bot2_config)

# print("Menunggu 30 menit untuk bot2...")
# time.sleep( 10 * 60 )
# print("Menyalakan bot3.py...")
# run_bot("tesa copy 2.py", bot3_config)
# print("Semua bot berjalan.")
