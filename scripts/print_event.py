import json
from random import randint

def load_json(file):
    "Load raw JSON data."
    
    with open(f'../data/raw/{file}.json','r') as f:
        return json.loads(
            f.read().replace('\\\\','\\').encode('utf-8')
            )
    
england = load_json('events_England')
event_num = randint(0,len(england))

with open('../figures/ExampleEvent.json', 'w') as f:
    txt = '{\n'
    event = england[event_num]
    for key in event.keys():
        txt = f"{txt}\t'{key}' : {event[key]},\n"
    txt = txt + "}"
    f.write(txt)
