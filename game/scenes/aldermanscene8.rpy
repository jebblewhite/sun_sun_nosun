label aldermanscene8: 

if game.coup == 'Alderman':
    call aldermanscene8alderman
elif game.coup == 'Alina':
    call aldermanscene8alina
elif game.coup == 'Not Involved':
    call aldermanscene8notinvolved
else:
    "You shouldn't be here"

return
