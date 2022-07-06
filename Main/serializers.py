from rest_framework import serializers,fields
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfile
        fields=('id',
                'wallet_address',
                'watch_history')


class ProjectFormSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProjectForm
        fields=('id',
            'wallet_address', 
            'project_name',
            'description',
            'project_category', 
            'token_name',
            'token_symbol', 
            'project_url',
            'project_address', 
            'tokenomics', 
            'soft_cap',
            'hard_cap',
            'total_token_supply',
            'total_market_cap',
            'taxes',
            'liquidity_percentage',
            'lockup_time',
            'project_to_launch',
            'project_launch_platform',
            
                )

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Video
        fields=('id',
        'display_video_name',
            'video_name',
            'project_name',
            'likes',
            'views',
            'votes',
            'video',
                )





