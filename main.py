import json
import uuid
from db_models.mongo_setup import global_init
from db_models.models.cache_model import Cache
import init
from transcribe_searvice import transcribe
import globals
import requests

global_init()

def save_to_db(db_object, result_to_save):
    print("*****************SAVING TO DB******************************")
    if db_object.text:
        db_object.text = db_object.text + ' ' + result_to_save
    else:
        db_object.text = result_to_save
    db_object.save()
    print("*****************SAVED TO DB******************************")

def update_state(file_name):
    payload = {
        'topic_name': globals.RECEIVE_TOPIC,
        'client_id': globals.CLIENT_ID,
        'value': file_name
    }
    try:
        requests.request("POST", globals.DASHBOARD_URL,  data=payload)
    except: 
        print("EXCEPTION IN UPDATE STATE API CALL......")


if __name__ == "__main__":
    print('main fxn')
    print("Connected to Kafka at " + globals.KAFKA_HOSTNAME + ":" + globals.KAFKA_PORT)
    print("Kafka Consumer topic for this Container is " + globals.RECEIVE_TOPIC)
    for message in init.consumer_obj:
        message = message.value
        db_key = str(message)
        print(db_key, 'db_key')
        try:
            db_object = Cache.objects.get(pk=db_key)
        except:
            print("EXCEPTION IN GET PK... continue")
            continue

        file_name = db_object.file_name
        
        print("#############################################")
        print("########## PROCESSING FILE " + file_name)
        print("#############################################")

       
        with open(file_name, 'wb') as file_to_save:
            file_to_save.write(db_object.file.read())
        try:
            audio_result = transcribe(file_name)
        except:
            print("ERROR IN TRANSCRIBE")
            continue
        
        to_save = audio_result
        print("to_save audio", to_save)
        save_to_db(db_object, to_save)
        print(".....................FINISHED PROCESSING FILE.....................")
        update_state(file_name)