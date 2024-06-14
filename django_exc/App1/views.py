from  .serializers import ExcelSerializer
from .models import ExcelData
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import datetime
import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.db.models import Count


def check_is_present_in_model(data):

        first_name = data[1]
        last_name = data[2]
        gender = data[3]
        country = data[4]
        age = data[5]
        da = data[6].tolist()
        
        duplicate = []

        for i in range(1,len(data)):

            # date_obj = datetime.datetime.strptime(da[i], "%d/%m/%Y")

            formatted_date_str = datetime.datetime.strftime(da[i],"%Y-%m-%d")

            # print(da[i])
            # date = datetime.datetime.strptime(f"{da[i]} 00:00:00", "%d/%m/%Y %H:%M:%S")
            # print(da.iloc[1])
            # print(date)
            data = ExcelData.objects.filter(first_name=first_name[i], last_name=last_name[i], gender=gender[i], country=country[i], age=age[i], date=formatted_date_str).values()
            # print(data)
            
            if data.exists():
                 
                for i in data:
                     
                    # print(i['first_name'])
                     
                    uplicate_data = {
                    "duplicate Data ": {
                        'first_name': i["first_name"],
                        'last_name': i["last_name"],
                        'gender': i["gender"],
                        'country': i["country"],
                        'age': i["age"],
                        'date': i["date"]

                    },
                    }

                duplicate.append(uplicate_data)
                 
                
            else:
                 obj = ExcelData(first_name=first_name[i], last_name=last_name[i], gender=gender[i], country=country[i], age=age[i], date=formatted_date_str)
                 obj.save()
    
        # return duplicate

        # print(Count(duplicate))
        return duplicate
        Count(duplicate)
        # return "ok"


class CreateAPI(APIView):

    def post(self, request):

        data_request = request.data
        file = request.FILES['excel']
        

        # excel = data_request.get("excel")

        excel_data = pd.read_excel(file, header=None)

        data = check_is_present_in_model(excel_data)

        # print(type(count))

        return JsonResponse(data = data, safe=False)
        # return Response(data={"msg":"ok"})