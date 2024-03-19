from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Todo

from .serializers import TodoSerializer
from rest_framework.parsers import JSONParser

# 2 views handle Todo operations

@csrf_exempt
def list_todo(request):
    
    # GET request to retrieve all todo list
    if request.method == 'GET':
        todos = Todo.objects.all()
        # Serialize todo list
        serializer = TodoSerializer(todos, many=True)
        # Return a JSON response with serialized data
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
         # Parse incoming JSON data from the request
        data = JSONParser().parse(request)
        # Serialize the data
        serializer = TodoSerializer(data=data)
        # Check if the data is valid
        if serializer.is_valid():
             # Save the serialized data (create a new todo)
            serializer.save()
             # Return a JSON response with the serialized data and status code 201 (Created)
            return JsonResponse(serializer.data, status=201)
         # If the data is not valid, return a JSON response with validation errors and status code 400 (Bad Request)
        return JsonResponse(serializer.errors, status=400)
    
    
    
    
@csrf_exempt
def todo_detail(request, pk):
    # Retrieve a specific todo based on the pk (primary key)
    todo = get_object_or_404(Todo, pk=pk)

    # Handle GET request to retrieve the details of the specific todo
    if request.method == 'GET':
        # Serialize the todo 
        serializer = TodoSerializer(todo)
        # Return a JSON response with the serialized data
        return JsonResponse(serializer.data)


    # the PUT request to update a specific todo
    elif request.method == 'PUT':
        # Parse incoming JSON data from the request
        data = JSONParser().parse(request)
        # Serialize the data of the todo
        serializer = TodoSerializer(todo, data=data)
        # Check if the data is valid
        if serializer.is_valid():
             # Save the serialized data (update the existing todo)
            serializer.save()
              # Return a JSON response with the serialized data
            return JsonResponse(serializer.data)
        # If the data is not valid, return a JSON response with validation errors and status code 400 (Bad Request)
        return JsonResponse(serializer.errors, status=400)


    # Handle DELETE request to delete a specific todo
    elif request.method == 'DELETE':
          # Delete the todo from the database
        todo.delete()
        # Return a JSON response indicating successful deletion
        return JsonResponse({'message': 'Todo has been deleted successfully!'}, status=204)