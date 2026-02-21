full_dot = '●'
empty_dot = '○'

def create_character (name, strength, intelligence, charisma):
   
    #name
    if not isinstance (name, str):
        return 'The character name should be a string'
    elif len(name) < 1:
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'
    else:
        'You\'re good to go'

    #stats
    status = [strength, intelligence, charisma]

    if not all (isinstance (stats,int)for stats in status):
        return 'All stats should be integers'
    elif any (stats < 1 for stats in status):
        return 'All stats should be no less than 1'
    elif any (stats > 4 for stats in status):
        return 'All stats should be no more than 4'
    elif sum(status) != 7:
        return 'The character should start with 7 points'


    dots = [stats*full_dot + (10 - stats)*empty_dot for stats in status]
    return (
        f'{name}'
        f'\nSTR {dots[0]}'
        f'\nINT {dots[1]}'
        f'\nCHA {dots[2]}'
    )

print(create_character('ren', 4, 2, 1))