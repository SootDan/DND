# This is a list of strings that are longer, supporting code readability.
import random

# When user types !support
support = f'''Hi! I\'m the friendly and easy to use <@1078282090673602580>.
To roll a die, simply type it like this: `!roll 3d20+3`
For information on the current campaign, type `!campaign`.
Roll initiative through `!initiative`.
Start the turn timer with `!turn` and end combat with `!turn_end`.
Summon this command with `!support`.'''

# Part of !campaign embed
campaign_desc = '''In a world, flooded in a natural disaster,
the Prometheus explores the one true sea in search of adventure, land, and, most importantly, gold. The crew must be careful, however: 
The sea has become a perilous plane with dangers at every corner.'''

# Dict to figure out UUID, characters, and pronouns
char_dict = {
    1066472550797938769: {
        'character': '🏹 Erhice',
        'pronoun': 'his'
    },
    375041751737434112: {
        'character': '🍊 Orange',
        'pronoun': random.choice(['his', 'her', 'their']) # Any/All, selected at random
    },
    84011476947304448: {
        'character': '🐍 Baughl',
        'pronoun': 'his'
    },
    84898094323335168: {
        'character': '🐢 Tootle',
        'pronoun': 'his'
    },
    242297398058156034: {
        'character': '🛡️ Morgan',
        'pronoun': 'her'
    },
    265624837001576448: {
        'character': '🐱 Ylvie',
        'pronoun': 'her'
    },
    738179922933317732: {
        'character': '👑 Dungeon Master',
        'pronoun': random.choice(['her', 'their']) # She/They, selected at random
    },
    'default': { # If no matching UUID has been found, default to They/Them
        'character': '🎲 Player',
        'pronoun': 'their'
    }
}
