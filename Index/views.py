
from django.http import JsonResponse,HttpResponse
from .models import KingQueenData,IMEIs,King,Queen,Miss,Mister,Cos,MisterMissData,PopMiss,PopMister,APP
from .serializers import KingQueenSerial,ImeiSerial,KingSerial,QueenSerial,MissSerial,MisterSerial,CosSerial,MisterMissSerial,PMissSerial,PMisterSerial,AppSerial
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
import json
def PopularData(request):
    if(request.method=="GET"):
        data1=KingQueenData.objects.all()
        data2=MisterMissData.objects.all()
        q1=data1.values()
        q2=data2.values()
        main=list(chain(q1,q2))

        return JsonResponse(main,safe=False)



class KingQueenDataAPI(APIView):
    permission_classes = [HasAPIKey]
    def dispatch(self, request, *args, **kwargs):
        return super(KingQueenDataAPI, self).dispatch(request, *args, **kwargs)
    def get(self, request, format=None):
        snippets = KingQueenData.objects.all()

        serializer = KingQueenSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KingQueenSerial(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MisterMissDataAPI(APIView):
    permission_classes = [HasAPIKey]
    def dispatch(self, request, *args, **kwargs):
        return super(MisterMissDataAPI, self).dispatch(request, *args, **kwargs)
    def get(self, request, format=None):
        snippets = MisterMissData.objects.all()

        serializer = MisterMissSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MisterMissSerial(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt,name="dispatch")
class ImeiAPI(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets = IMEIs.objects.all()
        serializer = ImeiSerial(snippets, many=True)


        return Response(serializer.data)

    def put(self, request, format=None):
        imei = request.data['imei']
        objects = IMEIs.objects.filter(imei=imei)

        serializer = ImeiSerial(objects[0], data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #react native must request a post method including a post imei
    # this is for the very first app boot certification
    def post(self, request, format=None):
        imei=request.data['imei']
        objects = IMEIs.objects.filter(imei=imei)

        if(len(objects) !=0 ):
            data = {
                "Voted": True
            }
            return JsonResponse(data)
        else:
            serializer = ImeiSerial(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt,name="dispatch")
class KingAPI(APIView):

    #multiple press on vote button will be certified by react native

    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets =King.objects.all()
        serializer = KingSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KingSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppAPI(APIView):
    def get(self,request,format=None):
        snippet=APP.objects.order_by('-pk')[0]
        serializer = AppSerial(snippet, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt,name="dispatch")
class QueenAPI(APIView):

    #multiple press on vote button will be certified by react native

    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets =Queen.objects.all()
        serializer = QueenSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QueenSerial(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt,name="dispatch")
class MissAPI(APIView):

    #multiple press on vote button will be certified by react native

    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets =Miss.objects.all()
        serializer = MissSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MissSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt,name="dispatch")
class MisterAPI(APIView):

    #multiple press on vote button will be certified by react native

    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets =Mister.objects.all()
        serializer = MisterSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MisterSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt,name="dispatch")
class CosAPI(APIView):

    #multiple press on vote button will be certified by react native

    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets =Cos.objects.all()
        serializer = CosSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CosSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt,name="dispatch")
class PopMisterAPI(APIView):

    #multiple press on vote button will be certified by react native

    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets =PopMister.objects.all()
        serializer = PMisterSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PMisterSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt,name="dispatch")
class PopMissAPI(APIView):

    #multiple press on vote button will be certified by react native

    permission_classes = [HasAPIKey]

    def get(self, request, format=None):
        snippets =PopMiss.objects.all()
        serializer = PMissSerial(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PMissSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def ReqAPI(request):
    # main()
    api_key, key = APIKey.objects.create_key(name="this_is_my_voting_api_keyword_pls_dont_mess")
    data={
        "key" : str(key)
    }
    return JsonResponse(data)

@method_decorator(csrf_exempt,name="dispatch")
class CheckMultiple(APIView):
    permission_classes = [HasAPIKey]

    def dispatch(self, request, *args, **kwargs):
        return super(CheckMultiple, self).dispatch(request, *args, **kwargs)

    def get(self, request, format=None):


        return Response({'some': 'data'})

    def post(self, request, format=None):
        imei=request.data['imei']
        objects = IMEIs.objects.filter(imei=imei)
        if(len(objects) !=0 ):
            target=objects[0]
            serializer = ImeiSerial(target)
            return Response(serializer.data)
        else:
            return Response({'vote': False})
        return Response({'error':'this is error '})


def Result(request):
    KQ=[[],[]]
    MM=[[],[]]
    POP=[[],[]]
    king_obj=King.objects.all()
    queen_obj=Queen.objects.all()
    mister_obj=Mister.objects.all()
    miss_obj=Miss.objects.all()
    pop_mister=PopMister.objects.all()
    pop_miss=PopMiss.objects.all()
    for i in king_obj:
        KQ[0].append(i.king)

    for i in queen_obj:
        KQ[1].append(i.queen)


    for i in mister_obj:
        MM[0].append(i.mister)

    for i in miss_obj:
        MM[1].append(i.miss)



    for i in pop_mister:
        POP[0].append(i.pmis)

    for i in pop_miss:
        POP[1].append(i.pmiss)

    kings = {i: KQ[0].count(i) for i in KQ[0]}
    queens = {i: KQ[1].count(i) for i in KQ[1]}

    misters= {i: MM[0].count(i) for i in MM[0]}
    misses={i: MM[1].count(i) for i in MM[1]}

    MrPop={i: POP[0].count(i) for i in POP[0]}
    MissPop={i: POP[1].count(i) for i in POP[1]}

    data={
        "kings":kings,
        "queens":queens,
        "misters":misters,
        "misses":misses,
        "mrPOP":MrPop,
        "msPOP":MissPop
    }

    return JsonResponse(data)