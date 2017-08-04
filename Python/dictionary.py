city_info = {'new_york' : { 'mayor' : "Bill DeBlasio",
                            'population' : 8406000,
                            'website' : "http://www.nyc.gov"
                            },
             'los_angeles' : { 'mayor' : "Eric Garcetti",
                            'population' : 3884307,
                            'website' : "http://www.lacity.org"
                            },
             'miami' : { 'mayor' : "Tomas Regalado",
                            'population' : 417650,
                            'website' : "http://www.miamigov.com"
                            },
             'chicago' : { 'mayor' : "Rahm Emanuel",
                            'population' : 2719000,
                            'website' : "http://www.cityofchicago.org/"
                            }
        }

#for city in city_info:
#    print "The mayor of {} is {}".format(city, city_info[city]['mayor'])
#    print "The population of {} is {}".format(city, city_info[city]['population'])
#    print "The website of {} is {}".format(city, city_info[city]['website'])
#    print "---------------------"

for cityName in city_info:
    for info in city_info[cityName]:
        print "The " + info + " of " + cityName + " is {}".format(city_info[cityName][info])
    print "---------------------"
