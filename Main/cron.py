from .models import *
def reset_battery():
    # your functionality goes here
    
        users=UserProfile.objects.filter()
        for u in users:
            user=UserProfile.objects.filter(wallet_address=u)
            battery=list(user.values('battery'))[0]['battery']
            package=list(user.values('package'))[0]['package']
            print(package)
            if package=='Diamond':
                battery=(battery+70)
                print(battery)
            elif package=='Gold':
                battery=(battery+60)%100
            elif package=='Silver':
                battery=(battery+50)%100

            if battery>100:
                    battery=100
            print(battery)
            user.update(battery=battery)
        
        