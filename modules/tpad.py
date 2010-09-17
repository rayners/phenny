
import typepad
from oauth.oauth import OAuthConsumer,OAuthToken
import urllib2
import re

def setup(self):
    tp_key = self.config.tpad_consumer_key
    tp_sec = self.config.tpad_consumer_secret
    tp_app = self.config.tpad_application_id
    stabbers_key = self.config.tpad_user_key
    stabbers_sec = self.config.tpad_user_secret
    self.typepad_consumer = OAuthConsumer(tp_key, tp_sec)
    self.typepad_app = typepad.Application.get_by_id(tp_app)
    self.typepad_token = OAuthToken(stabbers_key, stabbers_sec)
    typepad.client.add_credentials(self.typepad_consumer, self.typepad_token)
    self.typepad_user = typepad.User.get_self()
    blogs = self.typepad_user.blogs
    self.typepad_blog = blogs[0]

def f_post(phenny, input):
    content = input.group(2)
    content = content + "\n\n" + " -- " + input.nick
    post = typepad.Post(title='', content=content)
    phenny.typepad_blog.post_assets.post(post)
    permalink = post.permalink_url
    phenny.say(permalink)
f_post.commands = ['tp_post']
f_post.thread = False

def f_fav(phenny, input):
    url = input.group(2)
    d = urllib2.urlopen(url)
    text = d.read()
    m = re.search(r'asset_xid:\s+"([^"]+)"', text)
    id = m.group(1)
    asset = typepad.Asset.get_by_url_id(id)
    fave = typepad.Favorite(author=phenny.typepad_user, in_reply_to=asset.asset_ref)
    phenny.typepad_user.favorites.post(fave)
    phenny.say('Faved!')
f_fav.commands = ['tp_fav']
f_fav.thread = False

