from rest_framework import serializers,fields
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfile
        fields=('display_name',
                'wallet_address',
                'watch_history',
                'like_history',
                'vote_history')


class ProjectFormSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProjectForm
        fields=(
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
        fields=(
        'display_video_name',
            'video_name',
            'project_name',
            'likes',
            'views',
            'votes',
            'video',
                )





