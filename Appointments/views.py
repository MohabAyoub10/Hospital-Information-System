from django.shortcuts import render
from .models import *
from Hospital.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework import exceptions
from rest_framework.mixins import ListModelMixin


from pprint import pprint
from .permissions import *
# this is the view for the all  DoctorSchedule


class DoctorScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorScheduleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [CreateDoctorScheduleOrUpdate]
    search_fields = ['day_of_week',
                     'doctor__user__first_name', 'doctor__specialty__specialty']
    filterset_fields = '__all__'
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        doctor = self.request.query_params.get('doctor', None)
        if doctor is not None:
            queryset = DoctorSchedule.objects.select_related(
                'doctor').filter(doctor=doctor)
            return queryset
        else:
            queryset = DoctorSchedule.objects.select_related('doctor').all()
            return queryset


# this is the view for the all  DoctorSlots
class DoctorSlotsViewSet(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DoctorSlotsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [CanAccess]

    def get_queryset(self):
        date = self.request.query_params.get('date')
        schedule = self.request.query_params.get('schedule')
        doctor = self.request.query_params.get('doctor')
        if date is None or schedule is None or doctor is None:
            raise exceptions.ValidationError(
                {'Error': 'Please provide date, schedule and doctor'})
        booked_slots = BookedAppointment.objects.filter(
            date=date, slot__schedule=schedule, doctor=doctor).values_list('slot__pk', flat=True)
        queryset = Slot.objects.filter(schedule=schedule).exclude(
            pk__in=booked_slots).select_related('schedule')
        return queryset


class BookedAppoitnmentViewSet(viewsets.ModelViewSet):
    serializer_class = BookedAppoitnmentSerializer
    pagination_class = pagination.PageNumberPagination
    permission_classes = [BookAppointment]
    sorted_by = '__all__'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['doctor__user__first_name', 'doctor__specialty__specialty', 'patient__user__first_name', 'patient__user__last_name', 'patient__user__national_id', 'patient__user__phone_1',
                     'slot__schedule__day_of_week', 'slot__start_time', 'slot__end_time', 'date', 'type', 'status']
    filterset_fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            return BookedAppointment.objects.select_related('doctor__user', 'doctor__specialty', 'patient__user', 'slot', 'slot__schedule').filter(doctor__user=user)
        elif user.role == 'patient':
            return BookedAppointment.objects.select_related('doctor__user', 'doctor__specialty', 'patient__user', 'slot', 'slot__schedule').filter(patient__user=user)
        elif user.role == 'receptionist':
            return BookedAppointment.objects.select_related('doctor__user', 'doctor__specialty', 'patient__user', 'slot', 'slot__schedule').all()
        else:
            return BookedAppointment.objects.select_related('doctor__user', 'doctor__specialty', 'patient__user', 'slot', 'slot__schedule').all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return CreateAppointmentSerializer
        return BookedAppoitnmentSerializer


class DoctorAppointmentsDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAppointmentSerializer
    queryset = DoctorAppointmentsDetails.objects.select_related(
        'doctor__user').all()
    pagination_class = pagination.PageNumberPagination
    permission_classes = [DoctorAppointmentPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['doctor__user__first_name',
                     'doctor__specialty__specialty', 'date']
    filterset_fields = '__all__'
