from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Patient
from .serializers import PatientSerializer, RegistrationSerializer, UserLoginSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]

class RegistrationApiView(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            if user is None:
                raise ValueError("User object is None after serializer.save()")
    
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://doctor-appointment-vef1.onrender.com/activate/{uid}/{token}"
            email_subject = "Activate your account"
            email_body = render_to_string('email.html', {
                'user': user,
                'confirm_link': confirm_link
            })
            
            email = EmailMultiAlternatives(
                email_subject, 
                '', 
                from_email='contact@helphash.org',
                to=[user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check Your Mail for Confirmation", status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True  
            user.save()
            return HttpResponse('Your account has been activated successfully!')
        else:
            return HttpResponse('Activation link is invalid!', status=status.HTTP_400_BAD_REQUEST)

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                token, created = Token.objects.get_or_create(user=user) 
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'Error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserLogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response("You have been logged out successfully")