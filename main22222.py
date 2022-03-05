
from flask import Flask, request, redirect
from bs4 import BeautifulSoup
import queueManager
import json



app = Flask(__name__)

championNames = {
    "annie":"1","olaf":"2","galio":"3","twisted fate":"4","xin zhao":"5","urgot":"6",
    "leblanc":"7","vladimir":"8","fiddlesticks":"9","kayle":"10","master yi":"11","alistar":"12",
    "ryze":"13","sion":"14","sivir":"15","soraka":"16","teemo":"17","tristana":"18",
    "warwick":"19","nunu":"20","miss fortune":"21","ashe":"22","tryndamere":"23","jax":"24",
    "morgana":"25","zilean":"26","singed":"27","evelynn":"28","twitch":"29","karthus":"30",
    "cho\'gath":"31","amumu":"32","rammus":"33","anivia":"34","shaco":"35","dr. mundo":"36",
    "sona":"37","kassadin":"38","irelia":"39","janna":"40","gangplank":"41","corki":"42",
    "karma":"43","taric":"44","veigar":"45","trundle":"48","swain":"50","caitlyn":"51",
    "blitzcrank":"53","malphite":"54","katarina":"55","nocturne":"56","maokai":"57",
    "renekton":"58","jarvan iv":"59","elise":"60","orianna":"61","wukong":"62","brand":"63",
    "lee sin":"64","vayne":"67","rumble":"68","cassiopeia":"69","skarner":"72","heimerdinger":"74",
    "nasus":"75","nidalee":"76","udyr":"77","poppy":"78","gragas":"79","pantheon":"80","ezreal":"81",
    "mordekaiser":"82","yorick":"83","akali":"84","kennen":"85","garen":"86","leona":"89","malzahar":"90",
    "talon":"91","riven":"92","kog\'maw":"96","shen":"98","lux":"99","xerath":"101","shyvana":"102",
    "ahri":"103","graves":"104","fizz":"105","volibear":"106","rengar":"107","varus":"110","nautilus":"111",
    "viktor":"112","sejuani":"113","fiora":"114","ziggs":"115","lulu":"117","draven":"119","hecarim":"120",
    "kha\'zix":"121","darius":"122","jayce":"126","lissandra":"127","diana":"131","quinn":"133","syndra":"134",
    "aurelion sol":"136","kayn":"141","zoe":"142","zyra":"143","kai\'sa":"145","gnar":"150","zac":"154",
    "yasuo":"157","vel\'koz":"161","taliyah":"163","camille":"164","braum":"201","jhin":"202","kindred":"203",
    "jinx":"222","tahm kench":"223","lucian":"236","zed":"238","kled":"240","ekko":"245","vi":"254",
    "aatrox":"266","nami":"267","azir":"268","thresh":"412","illaoi":"420","rek\'sai":"421",
    "ivern":"427","kalista":"429","bard":"432","rakan":"497","xayah":"498","ornn":"516","pyke":"555"
}



# @app.route('/style.css', methods=['GET'])
# def css():
#     style = open('style.css', 'r').read()
#     return f'<styles>{style}</styles>'

@app.route('/', methods=['GET', 'POST'])
def index():

        #read html and css, and then inject css inside html
        style = open('style.css', 'r').read()
        html = BeautifulSoup(
            
            open('index.html', 'r').read(), 
            features="html.parser"
        )
        
        style_inject = html.new_tag('style')
        style_inject.string = style
        
        html.head.style.replace_with(style_inject)
        return f'{html}'
    


@app.route('/start_queue', methods=['POST'])
def start_queue():
    
#def champ_names_treatment():
    if request.method == "POST":
############################################################### pick prio

        #get champ name from form
        get_pick_priority1 = str(request.form['pick-prio1']).lower()
        get_pick_priority2 = str(request.form['pick-prio2']).lower()
        get_pick_priority3 = str(request.form['pick-prio3']).lower()

        #match champ name with respective id
        get_pick_priority1 = championNames.get(f'{get_pick_priority1}')
        get_pick_priority2 = championNames.get(f'{get_pick_priority2}')
        get_pick_priority3 = championNames.get(f'{get_pick_priority3}')

        #checking if pick prio is None 
        if get_pick_priority1 == None:
            get_pick_priority1 = 0
        else:
            get_pick_priority1 = int(get_pick_priority1)

        if get_pick_priority2 == None:
            get_pick_priority2 = 0
        else:
            get_pick_priority3 = int(get_pick_priority3)

        if get_pick_priority3 == None:
            get_pick_priority3 = 0
        else:
            get_pick_priority3 = int(get_pick_priority3)
############################################################### ban prio        
        
        #get champ name from form
        get_ban_priority1 = str(request.form['ban-prio1']).lower()
        get_ban_priority2 = str(request.form['ban-prio2']).lower()
        get_ban_priority3 = str(request.form['ban-prio3']).lower()

        #match champ name with respective id
        get_ban_priority1 = championNames.get(f'{get_ban_priority1}')
        get_ban_priority2 = championNames.get(f'{get_ban_priority2}')
        get_ban_priority3 = championNames.get(f'{get_ban_priority3}')

        #checking if ban prio is None 
        if get_ban_priority1 == None:
            get_ban_priority1 = 0
        else:
            get_ban_priority1 = int(get_ban_priority1)

        if get_ban_priority2 == None:
            get_ban_priority2 = 0
        else:
            get_ban_priority3 = int(get_ban_priority3)

        if get_ban_priority3 == None:
            get_ban_priority3 = 0
        else:
            get_ban_priority3 = int(get_ban_priority3)
##############################################################

        #dump all data from forms inside config.json
        global config
        config = json.load(open('config.json', 'r'))
        config.update({

            "pick_prio_id1": get_pick_priority1,
            "pick_prio_id2": get_pick_priority2,
            "pick_prio_id3": get_pick_priority3,
            
            "ban_prio_id1": get_ban_priority1,
            "ban_prio_id2": get_ban_priority2,
            "ban_prio_id3": get_ban_priority3
        })
        
        json.dump(config, open('config.json', 'w'), indent=4)


        print(get_pick_priority1)
        queueManager.run()
        return redirect('/')



if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000)
# try:
#     pass
#     #print(get_pick_priority)
# except:
#     #print('nao deu')
#     pass
