from rest_framework import serializers,fields
from .models import *

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
            'video',
                )

