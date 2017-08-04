#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib
import urllib2
import json
import jinja2
import os
import logging
from google.appengine.api import users

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
        hello = {"greeting" : greeting}
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render(hello))

    def post(self):
        search = self.request.get('search')
        if search != "":
            giphy_data_source = urllib2.urlopen("http://api.giphy.com/v1/gifs/search?q=%s&api_key=dc6zaTOxFJmzC&limit=10" % search)
            parsed_giphy_dictionary = json.loads(giphy_data_source.read())
            gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        else:
            giphy_data_source = urllib2.urlopen("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC")
            parsed_giphy_dictionary = json.loads(giphy_data_source.read())
            gif_url = parsed_giphy_dictionary['data']['image_url']
        gif_dict = {"url": gif_url}
        template = jinja_environment.get_template('templates/result.html')
        self.response.write(template.render(gif_dict))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
