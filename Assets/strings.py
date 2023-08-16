# This is a list of strings that are longer, supporting code readability.
import random
from Assets.privatefiles import char_baughl, char_erhice, char_morgan, char_orange, char_tootle, char_ylvie


# List of description strings
desc_campaign = '''In a world, flooded in a natural disaster,
the Prometheus explores the one true sea in search of adventure, land, and, most importantly, gold. The crew must be careful, however: 
The sea has become a perilous plane with dangers at every corner.'''

desc_support = f'''Hi! I\'m the friendly and easy to use <@1078282090673602580>.
To roll a die, simply type it like this: `!roll 3d20+3`
For information on the current campaign, type `!campaign`.
Roll initiative through `!initiative`.
Start the turn timer with `!turn` and end combat with `!turn_end`.
Summon this command with `!support`.'''

desc_timer = ''':flag_ie: / :flag_gb: ............... {}
:flag_de: / :flag_pl: ............... {}'''


# Dict to figure out UUID, characters, and pronouns
dict_char = {
    1066472550797938769: {
        'character': '\U0001F6AC Erhice',
        'pronoun': 'his'
    },
    375041751737434112: {
        'character': '\U0001F34A Orange',
        'pronoun': random.choice(['his', 'her', 'their']) # Any/All, selected at random
    },
    84011476947304448: {
        'character': '\U0001F40D Baughl',
        'pronoun': 'his'
    },
    84898094323335168: {
        'character': '\U0001F422 Tootle',
        'pronoun': 'his'
    },
    242297398058156034: {
        'character': '\U0001F518 Morgan',
        'pronoun': 'her'
    },
    265624837001576448: {
        'character': '\U0001F431 Ylvie',
        'pronoun': 'her'
    },
    738179922933317732: {
        'character': '\U0001F451 Dungeon Master',
        'pronoun': random.choice(['her', 'their']) # She/They, selected at random
    },
    'default': { # If no matching UUID has been found, default to They/Them
        'character': '\U0001F3B2 Player',
        'pronoun': 'their'
    }
}

# Links for images
img_campaign = 'https://cdn.discordapp.com/attachments/876359609034608670/1084211633238315190/flag-pride-jolly-roger.gif'
img_enemy_list = 'https://cdn-icons-png.flaticon.com/512/361/361245.png'
img_support = 'https://static.vecteezy.com/system/resources/previews/001/187/438/original/heart-png.pn'
img_timer = 'https://static.thenounproject.com/png/691206-200.png'

