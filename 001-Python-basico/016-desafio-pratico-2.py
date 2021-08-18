from datetime import datetime

now = datetime.now()
hour = f'{now.hour}:{now.minute}:{now.second}'

if now.hour > 0 and now.hour < 11:
    print(f'Bom dia! são exatamente: {hour}')
elif now.hour > 11 and now.hour < 17:
    print(f'Boa tarde! são exatamente: {hour}')
else:
    print(f'Boa noite! são exatamente: {hour}')
