# Vietnamese Syllables Generator
#
# Author: Phạm Thành Long
# Website: https://luom.tv/
#
# Generating a list of theoretically Vietnamese syllables
# based on the Quốc ngữ writing system.
# 
# TODO: "ơ" with schwa sound "u" and non-zero ending sounds
#

from icu import Collator, Locale # pip install --no-binary=:pyicu: pyicu

collator = Collator.createInstance(Locale('vi_VN.UTF-8'))

# Defining sound blocks

blocks = {
    # A
    'v_a1': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['', 'o'],
        'nuclear': ['a', 'a', 'a', 'a', 'a', 'a'],
        'ending':  ['', 'c', 'ch', 'i', 'm', 'n', 'ng', 'nh', 'o', 'p', 't', 'u', 'y']
    },
    # Ă
    'v_a2': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['', 'o'],
        'nuclear': ['a', 'a', 'a', 'a', 'a', 'a'],
        'ending':  ['c', 'm', 'n', 'ng', 'p', 't']
    },
    # Â 
    'v_a3': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['', 'u'],
        'nuclear': ['a', 'a', 'a', 'a', 'a', 'a'],
        'ending':  ['c', 'm', 'n', 'ng', 'p', 't', 'u', 'y']
    },
    # E
    'v_e1': {
        'initial': ['', 'b', 'ch', 'd', 'd', 'g', 'gh', 'gi', 'h', 'k', 'kh', 'l', 'm', 'n', 'ng', 'ngh', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['', 'o'],
        'nuclear': ['e', 'e', 'e', 'e', 'e', 'e'],
        'ending':  ['', 'c', 'm', 'n', 'ng', 'o', 'p', 't']
    },
    # Ê  
    'v_e2': {
        'initial': ['', 'b', 'ch', 'd', 'd', 'g', 'gh', 'gi', 'h', 'k', 'kh', 'l', 'm', 'n', 'ng', 'ngh', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['', 'u'],
        'nuclear': ['e', 'e', 'e', 'e', 'e', 'e'],
        'ending':  ['', 'ch', 'm', 'n', 'nh', 'p', 't', 'u']
    },
    # I
    'v_i': {
        'initial': ['', 'b', 'ch', 'd', 'd', 'g', 'gh', 'h', 'k', 'kh', 'l', 'm', 'n', 'ngh', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['i', 'i', 'i', 'i', 'i', 'i',],
        'ending':  ['', 'ch', 'm', 'n', 'nh', 'p', 't', 'u']
    },
    # O
    'v_o1': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['o', 'o', 'o', 'o', 'o', 'o'],
        'ending':  ['', 'c', 'i', 'm', 'n', 'ng', 'p', 't']
    },
    # OO
    'v_oo1': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
        'ending':  ['c', 'ng']
    },
    # Ô
    'v_o2': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['o', 'o', 'o', 'o', 'o', 'o'],
        'ending':  ['', 'c', 'i', 'm', 'n', 'ng', 'p', 't']
    },
    # ÔÔ
    'v_oo2': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
        'ending':  ['ng']
    },
    # Ơ1 (kết hợp với âm đệm zero)
    # ngoài trường hợp âm đầu "q" thì thực tế không thấy trường hợp có cả âm đệm lẫn âm cuối không zero
    'v_o3': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['o', 'o', 'o', 'o', 'o', 'o'],
        'ending':  ['', 'c', 'i', 'm', 'n', 'ng', 'p', 't']
    },
    # Ơ2 (kết hợp với âm đệm /-w-/, âm cuối zero)
    'v_o4': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['u'],
        'nuclear': ['o', 'o', 'o', 'o', 'o', 'o'],
        'ending':  ['']
    },
    # U
    'v_u1': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['u', 'u', 'u', 'u', 'u', 'u'],
        'ending':  ['', 'c', 'i', 'm', 'n', 'ng', 'p', 't']
    },
    # Ư
    'v_u2': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['u', 'u', 'u', 'u', 'u', 'u'],
        'ending':  ['', 'c', 'i', 'm', 'n', 'ng', 'p', 't', 'u']
    },
    # Y1
    'v_y1': {
        'initial': ['', 'b', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'q', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['u'],
        'nuclear': ['y', 'y', 'y', 'y', 'y', 'y'],
        'ending':  ['', 'ch', 'm', 'n', 'nh', 'p', 't', 'u']
    },
    # Y2 (ngoại lệ, cho một số từ Hán-Việt)
    'v_y2': {
        'initial': [''],
        'schwa':   [''],
        'nuclear': ['y', 'y', 'y', 'y', 'y', 'y'],
        'ending':  ['']
    },
    # IA (gi được khai thành g)
    'v_ia': {
        'initial': ['', 'b', 'ch', 'd', 'd', 'g', 'gh', 'h', 'k', 'kh', 'l', 'm', 'n', 'ngh', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['ia', 'ia', 'ia', 'ia', 'ia', 'ia'],
        'ending':  ['']
    },
    # IÊ (gi được khai thành g)
    'v_ie': {
        'initial': ['b', 'ch', 'd', 'd', 'g', 'gh', 'h', 'k', 'kh', 'l', 'm', 'n', 'ngh', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['ie', 'ie', 'ie', 'ie', 'ie', 'ie'],
        'ending':  ['c', 'm', 'n', 'ng', 'p', 't', 'u']
    },
    # UA
    'v_ua': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['ua', 'ua', 'ua', 'ua', 'ua', 'ua'],
        'ending':  ['']
    },
    # UÔ
    'v_uo': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['uo', 'uo', 'uo', 'uo', 'uo', 'uo'],
        'ending':  ['c', 'i', 'm', 'n', 'ng', 'p', 't']
    },
    # ƯA
    'v_wa': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['ua', 'ua', 'ua', 'ua', 'ua', 'ua'],
        'ending':  ['']
    },
    # ƯƠ
    'v_wo': {
        'initial': ['', 'b', 'c', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   [''],
        'nuclear': ['uo', 'uo', 'uo', 'uo', 'uo', 'uo'],
        'ending':  ['c', 'i', 'm', 'n', 'ng', 'p', 't', 'u']
    },
    # YA
    'v_ya': {
        'initial': ['', 'b', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'q', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['u'],
        'nuclear': ['ya', 'ya', 'ya', 'ya', 'ya', 'ya'],
        'ending':  ['']
    },
    # YÊ1
    'v_ye1': {
        'initial': ['', 'b', 'ch', 'd', 'd', 'g', 'gi', 'h', 'kh', 'l', 'm', 'n', 'ng', 'nh', 'p', 'ph', 'q', 'r', 's', 't', 'th', 'tr', 'v', 'x'],
        'schwa':   ['u'],
        'nuclear': ['ye', 'ye', 'ye', 'ye', 'ye', 'ye'],
        'ending':  ['c', 'm', 'n', 'ng', 'p', 't']
    },
    # YÊ2 (ngoại lệ)
    'v_ye2': {
        'initial': [''],
        'schwa':   [''],
        'nuclear': ['ye', 'ye', 'ye', 'ye', 'ye', 'ye'],
        'ending':  ['c', 'm', 'n', 'ng', 'p', 't', 'u']
    }
}

# Initial sounds which not followed by 'o' or 'u' (/-w-/ phoneme)
initial_not_followed_by_w = ['c', 'k', 'gh', 'ngh', 'qu']  # and 'b', 'm', 'ph', 'v' in some theory

# Ending sounds in tone 5 or tone 6 syllables only
ending_in_tone56_only = ['p', 't', 'c', 'ch']

# "Schwa" sounds
schwa_chars = ['o', 'u']

# e, ê nuclear
e_ee = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']

# Syllable list initiated with "quốc"
syllables = ['quốc']

# Generating syllables
for key in blocks:
    sounds = blocks[f'{key}']
    for i in sounds['initial']:
        for w in sounds['schwa']:
            if (i in initial_not_followed_by_w and w in schwa_chars):
                continue
            for k, n in enumerate(sounds['nuclear']):
                if i in ['ng', 'g'] and w == '' and n in e_ee:
                    continue
                for e in sounds['ending']:
                    if (k < 4 and e in ending_in_tone56_only):
                        continue
                    syllables.append(i + w + n + e)
                    #print(i + w + n + e)

# Sorting syllables
syllables = sorted(syllables, key=collator.getSortKey)

# Check for duplicates
duplicates = []
for i, w in enumerate(syllables):
    if syllables[i] == syllables[i-1]:
        #print('\t', i, syllables[i], end="")
        duplicates.append(syllables[i-1])
        syllables.pop(i-1)

# Write to file
filename = 'LuomTV-Vietnamese-Syllables-Auto-Generated.txt'
with open(filename, 'w') as f:
    f.writelines("%s\n" % l for l in syllables)
    
f.close()

# Display all
#for syllable in syllables:
#    print(syllable)

print('Duplicated syllable(s): ', duplicates)
print('\nNumber of generated syllables: ', len(syllables))
print('\nSaved in:', filename)