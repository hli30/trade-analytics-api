from csv import reader
from io import StringIO
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import History
from .serializers import HistorySerializer

class TradeHistoryUploadView(APIView):
    def post(self, request):
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            return Response({'error': 'Wrong file type'}, status=status.HTTP_400_BAD_REQUEST)
        
        csv_decoded = csv_file.read().decode('UTF-8')
        io_string = StringIO(csv_decoded)
        next(io_string) # skip header
        csv_reader = reader(io_string, delimiter=',', quotechar='|')

        data = []
        for row in csv_reader:
            data.append(
                {
                    'symbol': row[0],
                    'asset_type': row[1],
                    'description': row[2],
                    'action': row[3],
                    'quantity': row[4],
                    'price': row[5]
                }
            )
        
        serializer = HistorySerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TradeHistoryListView(ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        return History.objects.filter(user_id=self.request.user.id)
