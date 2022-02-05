def ask_ok(prompt, retries = 4, reminder = 'please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes','yep'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries= retries -1
        if retries <0:
            raise ValueError('Invalid user response')
        print (reminder)

ask_ok("Is it alright with you?", 2)


# keyword arguments
def parrot(voltage, state= 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print('-- This parrot wouldn\'t', action, end = ' ')
    print('If you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print('-- it\'s ', state, '!')