from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from django.http import JsonResponse


@api_view(['GET'])
def getRoutes(request):
	routes = [
		{
			'Endpoint': '/notes/',
			'method': 'GET',
			'body': None,
			'description': 'Return an array of notes'
		},
		{
			'Endpoint': '/notes/id',
			'method': 'GET',
			'body': None,
			'description': 'Return a single note object'
		},
		{
			'Endpoint': '/notes/create/',
			'method': 'POST',
			'body': {'body': ""},
			'description': 'Creates new existing note with data sent in post'
		},
		{
			'Endpoint': '/notes/id/update/',
			'method': 'PUT',
			'body': {'body': ""},
			'description': 'Return ann array of notes'
		},
		{
			'Endpoint': '/notes/id/delete/',
			'method': 'DELETE',
			'body': None,
			'description': 'Return ann array of notes'
		}
	]

	return Response(routes)

@api_view(['GET'])
def getNotes(request):
	notes = Note.objects.all()
	objects = {}
	for note in notes:
		objects.add(note)
	return JsonResponse(objects)



@api_view(['GET'])
def getNote(request, id):
	notes = Note.objects.get(id=id)
	serializer = NoteSerializer(notes, many=False)
	return Response(serializer.data)



@api_view(['POST'])
def createNote(request):
	data = request.data


	note = Note.objects.create(body=data['body'])
	serializer = NoteSerializer(note, many=False)
	return Response(serializer.data)



@api_view(['PUT', 'GET'])
def updateNote(request, id):
	data = request.data


	note = Note.objects.get(id=id)
	serializer = NoteSerializer(note, data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



@api_view(['DELETE'])
def deleteNote(request, id):
	Note.objects.get(id=id).delete()
	return Response('Deleted')