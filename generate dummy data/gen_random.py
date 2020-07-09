import requests
import time
import string
import random
import datetime


URL_post = "http://35.241.91.76:8000/api/myapp/"


for i in range(10):
    user_id = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 4))
    name = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 4))
    tz = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 4))

    User_data = {
                    'id': user_id ,
                    'real_name': name,
                    'tz':tz,
                    'activity_periods':[{
                        	  "start_time": "Feb 1 2020  1:33PM",
					          "end_time": "Feb 1 2020 1:54PM"
				        },
				        {
					          "start_time": "Mar 1 2020  11:11AM",
					          "end_time": "Mar 1 2020 2:00PM"
				        }
                    ]
                }
    r = requests.post(url = URL_post, json = User_data)
    print(User_data)
    print(r)
    #print(i+1)
