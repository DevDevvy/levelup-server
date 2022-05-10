"""View module for handling requests about events"""
from email.policy import default
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models.game import Game
from levelupapi.models.game_type import Game_type
from levelupapi.models.gamer import Gamer
from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from django.db.models import Count
from django.db.models import Q
class EventView(ViewSet):
    """Level up events"""
    def retrieve(self, request, pk):
        """Handle GET requests for single event
        Returns:
            Response -- JSON serialized event
        """
        try:
            events = Event.objects.annotate(attendees_count=Count('attendees'))
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 



    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized event
        """
        organizer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateEventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organizer=organizer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """
        # pass data through serializer and validate
        event = Event.objects.get(pk=pk)
        serializer = CreateEventSerializer(event, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)



    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        events = Event.objects.annotate(
            attendees_count=Count('attendees'),
            joined=Count(
                'attendees',
                filter=Q(attendees=gamer)
            )
        )
        # check if string is a query ie /events?game=1
        event_game = request.query_params.get('game', None)
        if event_game is not None:
            events = events.filter(game_id=event_game)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    
    
    # deletes event
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        # allows users to sing up using an @action decorator
        # uses post method with detail=true because pk detail needed
    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
    # get the gamer id and the event pk, then add to attendees many to many join table
        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(gamer)
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    # allows user to un-signup
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.remove(gamer)
        return Response({'message': 'Gamer left the party'}, status=status.HTTP_204_NO_CONTENT)
    # Set the `joined` property on every event
    

               


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    attendees_count = serializers.IntegerField(default=None)
    class Meta:
        model = Event
        fields = ('id', 'description', 'game_date', 'time', 'game', 'organizer', 'joined', 'attendees_count')
        depth = 2
        


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'description', 'game_date', 'time', 'game']