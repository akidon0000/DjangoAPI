from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.models import User
from polls.serializers import UserSerializer

@api_view(['GET', 'POST'])
def user_list(request, format=None):

    if request.method == 'GET':
        #UserをMySQLから全件取得
        polls = User.objects.all()
        serializer = UserSerializer(polls, many=True)
        #Jsonで返してくる
        return Response(serializer.data)




    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #登録成功するとJsonデータが帰ってくる  ##status 200番台は処理が成功した
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def user_detail(request, pk, format=None):
    try:
        polls = User.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(polls)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        snippet.delete()
        ## HttpResponseをResponseに変更
        return Response(status=status.HTTP_204_NO_CONTENT)