from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# from v1.{{ app_name }}.models.model_name import Model
# from v1.{{ app_name }}.serializers.model_name import ModelSerializerList
# from v1.{{ app_name }}.serializers.model_name import ModelSerializerCreate
# from v1.utils.views.mixins import MultiSerializerViewSetMixin
# from v1.utils.views.paginators import NumPagesPagination


# # v1/admin/{{ app_name }}/
# class ModelView(
#     MultiSerializerViewSetMixin,
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     viewsets.GenericViewSet,
# ):
#     queryset = Model.objects.all()
#     permission_classes = [IsAuthenticated]
#     pagination_class = NumPagesPagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filter_class = None
#     search_fields = []
#     authentication_classes = [JSONWebTokenAuthentication]
#     serializer_action_classes = {
#         'create': ModelSerializerCreate,
#         'list': ModelSerializerList,
#     }
