import facebook

ACCESS_TOKEN = "<your-page-access-token>"
# PAGE_ID = "<page-id>"
api = facebook.GraphAPI( ACCESS_TOKEN )
args = {'fields' : 'message'}
conv = api.get_object( 'me/conversations')
msg = api.get_object( conv['data'][0]['id']+'/messages')
for el in msg['data']:
    content = api.get_object( el['id'], **args)
    print(content)