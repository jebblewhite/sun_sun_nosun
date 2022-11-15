label crierscene9:

if game.creaturefate == 'Alive':
    call crierscene9alive
elif game.creaturefate == 'Dead':
    call crierscene9dead
elif game.creaturefate == 'Exile':
    call crierscene9exile
else:
    "You shouldn't be here"
return