from numpy import record
from rest_framework.views import APIView
# from django.http import JsonResponse
from rest_framework.response import Response
import advertools as adv 
import pandas as pd
from datetime import datetime
import random
import string
from django.http import JsonResponse
import json


class OnpageCrawl(APIView):
    
    def post(self, request):

        # get user url
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        url = body['url']
        
        # create unique file name to store json list file
        date = datetime.now().strftime("%d/%m/%Y%H%M%S")
        def rand_str(size):      
        # Takes random choices from
        # ascii_letters and digits
            generate_pass = ''.join([random.choice(
                                string.ascii_letters + string.digits)
                                for n in range(size)])
            return generate_pass
        # Driver Code 
        random_str = str(rand_str(4))
        raw_output_file = url + date + random_str
        # using regex to remove characters
        remove_characters = "//.-:_"
        output_file = raw_output_file
        for character in remove_characters:
            output_file = output_file.replace(character, "")
        add_extension_to_output_file = output_file + ".jl"
        final_output_file = str(add_extension_to_output_file)

        # crawl url using advtools
        adv.crawl(url, final_output_file, follow_links=False)
        
        # crawl_df = pd.read_json('httpswwwmediumcom07082022164637uWoR.jl', lines=True)
        df = pd.read_json('httpswwwmediumcom07082022164637uWoR.jl', lines=True)

        

        # s1 = json.dumps(d1)
        # d2 = json.loads(s1)
        # data = crawl_df.head()

        # crawl_df = pd.read_json('my_output.jl', lines=True)
        # crawl_df.to_json('final_output.json')
        
        return JsonResponse(json.loads(json.dumps(df.to_json())), safe=False)