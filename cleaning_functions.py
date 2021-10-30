def tipe(x):
    if x['Type'] == 'Boating' | x['Type'] == 'Boat' |x['Type'] == 'Unprovoked' |x['Type'] == 'Invalid' |x['Type'] == 'Questionable' |x['Type'] == 'Sea Disaster':
        return 'Unprovoked'
    else:
        return 'Provoked'

def surf(x):
    return re.sub('`.+urf.+','Surf',x)