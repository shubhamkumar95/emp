from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from poll.serializers import QuestionSerializer
from .models import Question


class PollAPIView(APIView):
    def get(self, request):
        print(request.query_params)
        print(type(request), "<class 'rest_framework.request.Request'>")
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollDetailView(APIView):
    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except Question.DoesNotExist as e:
            return Response({"error": "Given object not found"}, status=status.
                            HTTP_404_NOT_FOUND)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        instance = self.get_object(id)
        data = request.data
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)