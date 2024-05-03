from django.shortcuts import render
from rest_framework import viewsets
from .models import Character
from .serializers import CharacterSerializer

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import boto3
from botocore.exceptions import NoCredentialsError
import logging

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


@api_view(['GET'])
def generate_presigned_url(request):
    # Generate a pre-signed URL for the client to upload a file directly to S3
    # The client will then use this URL to perform the actual upload
    logger = logging.getLogger(__name__)

    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )
    file_name = request.headers.get('File_name')
    file_type = request.headers.get('File_type')
    logger.info(file_name)
    logger.info(file_type)


    if not file_name or not file_type:
        return Response({'error': 'Missing file name or file type'}, status=400)

    try:
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': file_name,  # Key is the filename that will be used to save the file in S3
                'ContentType': file_type,  # The content type of the file to be uploaded
                'ACL': 'public-read'  # Optionally set the ACL
            },
            ExpiresIn=3600  # Link expires in 1 hour
        )
        return Response({'presigned_url': presigned_url})
    except NoCredentialsError:
        return Response({'error': 'Error generating presigned URL'}, status=500)