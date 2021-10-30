def tipe(x):
    if x == 'Boating' | x== 'Boat' |x == 'Unprovoked' |x == 'Invalid' |x == 'Questionable' |x== 'Sea Disaster':
        return 'Unprovoked'
    else:
        return 'Provoked'


def surf(x):
    return re.sub('`.+urf.+','Surf',x)
    