#working with dictionaries
from pyscript import display, document

def game_details(e):
    document.getElementById('result').innerHTML = " "
    favorite_game = document.getElementById('dictionary').value

    game_developers = {
        'genshin':'Hoyoverse',
        'valorant':'Riot Games',
        'fnaf':'Scott Cawthon',
        'minecraft':'Notch'
    } #specifying dicts
    # game_developers['genshin_impact'] = 'Hoyoverse' # adding a new element
    
    game_checker = favorite_game in game_developers

    display_message = ('Sorry your game is not in our system', f'{game_developers[favorite_game]}')

    display(display_message[game_checker], target='result')



    # lists_with_tuples = [(1, 'a'), (2 , 'b'), (3, 'c')]
    # tuples_with_strings = ('ab', 'cd', 'ef')
    # lists_with_strings = ['ax', 'by', 'cz']

    # display(dict(lists_with_tuples), target='result')
    # display(dict(tuples_with_strings), target='result')
    # display(dict(lists_with_strings), target='result')

    # keywords = ['Lindsay', 'JM', 'Jay', 'Mace']
    # values = ['esguerra', 'pinsay', 'estrada', 'panela']

    # students_nicknames = dict(zip(keywords, values))
    # display(students_nicknames, target='result')

    # philadelphia = {
    #     'c': 'Joel Embiid',
    #     'pf': 'LeBron James',
    #     'sg':' VJ Edgecomb',
    #     'pg': 'Tyrese Maxer',
    #     'sf': 'Jaylen Brown'
    # }
    # philadelphia['pg'] = 'Stephen Curry'
    # del philadelphia['sg']
    # display(philadelphia, target='result')

    # dict1 = {'x':1, 'y':2, 'z':3}
    # dict2 = {'a':4, 'b':5, 'c':6}

    # display( dict1 | dict2, target='result')
    # merged_dictionary = {**dict1, **dict2}

    # display(merged_dictionary, target='result')

    # display(len(merged_dictionary), target='result')

    # ai = {
    #     'tony stark': 'creator',
    #     'J.A.R.V.I.S': 'AI1',
    #     'F.R.I.D.A.Y': 'AI2',
    #     'E.D.I.T.H': 'AI3'
    # }

    # display('Vision' in ai, target='result')
    # display(ai.get('J.A.R.V.I.S'), target='result')
    # display(ai.keys(), target='result')
    # display(ai.values(), target='result')
    # display(ai['tony stark'], target='result')


    
