from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


class NoPostViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    pass