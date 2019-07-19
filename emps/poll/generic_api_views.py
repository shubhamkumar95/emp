from rest_framework import generics, viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from poll.models import Question, Choice
from poll.serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class PollListView(generics.GenericAPIView, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    # or pk for looking up primary key. By default set, no need to set.
    # lookup_field = 'pk'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        print(self.request.user)
        serializer.save(created_by=self.request.user)


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

    @action(detail=True, methods=["GET"])
    def choices(self, request, id=None):
        question = self.get_object()
        choices = Choice.objects.filter(poll=question)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=200)
