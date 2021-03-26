
FB_SETTINGS="facebookkeys.txt"
from facebook import Facebook

def desktop_app():


    # Get api_key and secret_key from a file
    fbs = open(FB_SETTINGS).readlines()
    facebook = Facebook(fbs[0].strip(), fbs[1].strip())

    facebook.auth.createToken()
    # Show login window
    facebook.login()

    # Login to the window, then press enter
    #print 'After logging in, press enter...'
    #raw_input()

    facebook.auth.getSession()
    return facebook

def test_users(facebook):
    info = facebook.users.getInfo([facebook.uid], ['name', 'birthday', 'affiliations', 'sex'])[0]

    for attr in info:
        print '%s: %s' % (attr, info[attr])

    friends = facebook.friends.get()
    #print friends friens es una lista de codigo de usuarios
    #friends = facebook.users.getInfo(friends[0:5], ['name', 'birthday', 'relationship_status'])
    friends = facebook.users.getInfo(friends, ['name', 'birthday', 'relationship_status'])

    for friend in friends:
        if 'Jelika' in friend['name']:
            print friend['name'], 'has a birthday on', friend['birthday'], 'and is', friend['relationship_status']
            #print friend
        else:
            #print friend['name'], 'has no birthday and is', friend['relationship_status']
            pass
            

    arefriends = facebook.friends.areFriends([friends[0]['uid']], [friends[1]['uid']])

    photos = facebook.photos.getAlbums(friends[1]['uid'])
    print photos

def get_messages(facebook,uid,limit,offset):
    
    inbox=Facebook.message.getThreadsInFolder(0,uid,limit,offset)
    return inbox
    