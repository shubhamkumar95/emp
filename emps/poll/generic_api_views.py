from rest_framework import generics
from rest_framework import mixins
from poll.models import Question
from poll.serializers import QuestionSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class PollListView(generics.GenericAPIView, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # or pk for looking up primary key. By default set, no need to set.
    # lookup_field = 'pk'

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
