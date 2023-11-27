from src.services.database_sevice import DatabaseService
import asyncio


messages_db = DatabaseService('messages')

if asyncio.get_event_loop().is_closed():
        asyncio.set_event_loop(asyncio.new_event_loop())

def crate_chat(event, context):
    datos = event["payload"]
    task = asyncio.ensure_future(messages_db.save(messages_db.collection, datos))
    asyncio.get_event_loop().run_until_complete(task)
    response = {"statusCode": 200, "message": "Chat insertado con exito"}
    return response

def inset_message(event, context):
    datos = event["payload"]
    _id = datos["_id"]
    _message_from_user = datos["_message_from_user"]
    task = asyncio.ensure_future(messages_db.update_one(messages_db.collection, {'_id': _id}, {"$push": {"messages": _message_from_user}} ))
    asyncio.get_event_loop().run_until_complete(task)
    response = {"statusCode": 200, "message": "Mensage insertado con exito"}
    return response