
    

from rest_framework import status
from .serializers import FlowerSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Flowers
from joblib import load
from rest_framework.response import Response

# Load the model
model = load('./mymodels/model.joblib')

class FlowerList(ModelViewSet):
    queryset = Flowers.objects.all()
    serializer_class = FlowerSerializer

    def create(self, request,*args,**kwargs):
        print('start')
        # Print the data received from the frontend
        print("Data received from frontend:", request.data)

        # Extract data for prediction
        data_to_predict = [
            float(request.data['sepal_length']),
            float(request.data['sepal_width']),
            float(request.data['petal_length']),
            float(request.data['petal_width'])
        ]
       

        # Make prediction using the loaded model
        prediction = model.predict([data_to_predict])
        print("Prediction:", prediction)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Serialize prediction and return response
        prediction_serializable = prediction.tolist()
        return Response({'prediction': prediction_serializable}, status=status.HTTP_201_CREATED)
        