import re

def tipe(x):
    if x == 'Boating' | x== 'Boat' |x == 'Unprovoked' |x == 'Invalid' |x == 'Questionable' |x== 'Sea Disaster':
        return 'Unprovoked'
    else:
        return 'Provoked'


def surf(x):
    return re.sub('.*urf.*|.*Paddl.*|.*board.*|.*Board.*|.*surf.*|.+Surf.*','Surfing',x)

def dive(x):
    return re.sub('.*Dive|.*iv.*|Scuba|nork','Diving',x)

def swim(x):
    return re.sub('Swim.*|.*swim.*|Swimming|Wad|Bath.*|float.*|Float.*|\sSwim.*','Swimming',x)

def fish(x):
    return re.sub('fish.*|Fish.*|.*fish','Fishing',x)

def boat(x):
    return re.sub('.*boat.*|.*Boat.*|Canoe.*|Sailing','Boat',x)

def other(x):
    return re.sub('.*[^Surf][^Diving][^Swimming][^Fishing][^Boat].*','Other',x)

def white(x):
    return re.sub('.*White.*|.*white.*','White Shark',x)
def tiger(x):
    return re.sub('.*Tiger.*|.*tiger.*','Tiger Shark',x)
def lemon(x):
    return re.sub('.*Lemon.*|.*lemon.*','Nurse Shark',x)
def bull(x):
    return re.sub('.*Bull.*|.*bull.*','Bull Shark',x)
def mako(x):
    return re.sub('.*Mako.*|.*mako.*','Mako Shark',x)
def blue(x):
    return re.sub('.*Blue.*|.*blue.*','Blue Shark',x)
def blacktip(x):
    return re.sub('.*blacktip.*|.*Blacktip.*','Blacktip reef Shark',x)
def hammerhead(x):
    return re.sub('.*Hammerhead.*|.*hammerhead.*','Hammerhead Shark',x)
def nurse(x):
    return re.sub('.*Nurse.*|.*nurse.*','Nurse Shark',x)
def whaler(x):
    return re.sub('.*Whaler.*|.*whaler.*','Bronze Whaler Shark',x)
def caribbean(x):
    return re.sub('.*Caribbean.*|.*caribbean.*','Caribbean Reef Shark',x)
def raggedtooth(x):
    return re.sub('.*Raggedtooth.*|.*raggedtooth.*','Raggedtooth Shark',x)
def spinner(x):
    return re.sub('.*Spinner.*|.*spinner.*','Spinner Shark',x)
def age(x):
    return re.sub('.*[a-zA-Z!@#$%^&*()_+\-=\[\]{};\\|,.<>\/?].*|.*\s.*','0',x)