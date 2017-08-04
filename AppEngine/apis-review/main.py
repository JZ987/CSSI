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
import json
import urllib
import urllib2
import os
import jinja2
import logging

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/flag_input.html')
        self.response.write(template.render())

    def post(self):
        # Step 1: Get the user input from the form
        countries = self.request.get('country').replace(",", " ").split()
        # Step 2: Create the URL (Hint: this is a different kind of URL: no query string!)
        dictionary = {"countries":{}}
        for country in countries:
            base_url = "https://restcountries.eu/rest/v2/name/{}?".format(country)
            url_params = {"fullText" : "true"}
            data_source = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
            # Step 3: Query the API and parse the data from JSON to python
            data_dictionary = json.loads(data_source)
            # Step 4: Use the returned data to get the url of the flag image
            # Hint: Put the API request URL into the browser to see what the data looks like.
            flag_url = data_dictionary[0]['flag']
            # Step 5: Render the flag_output template.
            dictionary['countries'][country] = flag_url
        logging.info(dictionary)
        template = jinja_environment.get_template('templates/flag_output.html')
        self.response.write(template.render(dictionary))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
