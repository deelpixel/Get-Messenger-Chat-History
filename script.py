import facebook

ACCESS_TOKEN = "PASTE_ACCESS_TOKEN_HERE"

api = facebook.GraphAPI( ACCESS_TOKEN )
args = {'fields' : 'from,message,created_time'}
conv = api.get_object( 'me/conversations')

noOfChats = len(conv['data'])

for i in range(0, noOfChats):
    msg = api.get_object( conv['data'][i]['id']+'/messages')
    for el in msg['data']:
        content = api.get_object( el['id'], **args)
        resp = {
            'from': content['from']['name'],
            'message': content['message'],
            'created_time': content['created_time']
        }
        print(resp)