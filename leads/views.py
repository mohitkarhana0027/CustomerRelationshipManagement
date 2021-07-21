from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .constants import CLAIM
from .serializers import LeadCreateSerializer, LeadListSerializer
from .models import Lead
from .models import FRESH

# Create your views here.


class LeadCreateView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LeadCreateSerializer

    def post(self, request):
        try:
            serializer = LeadCreateSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'message': 'lead created successfully !', 'error': None},
                                status=status.HTTP_200_OK)
            return Response({'success': False, 'message': 'lead creation failed !', 'error': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'success': False, 'message': 'lead creation failed !', 'error': error.args[0]},
                            status=status.HTTP_400_BAD_REQUEST)


class LeadListView(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=FRESH, is_active=True).order_by('-id')
        return queryset


class LeadClaimView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadListSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        request-body :
        {
            "lead":1
        }
        """
        try:
            data = request.data
            user = request.user
            lead_obj = Lead.objects.get(id=data.get('lead'))
            if lead_obj.status == FRESH:
                lead_obj.claim_by = user
                lead_obj.status = CLAIM
                lead_obj.save()
                return Response({'success': True, 'message': 'lead claimed successfully !', 'error': None},
                                status=status.HTTP_200_OK)
            return Response({'success': True, 'message': 'lead already claimed !', 'error': None},
                            status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'success': False, 'message': 'lead creation failed !', 'error': e.args[0]},
                            status=status.HTTP_400_BAD_REQUEST)