QUESTION = 'Sure.'
YELL = 'Whoa, chill out!'
ANYTHING_ELSE = 'Whatever.'
NOTHING = 'Fine. Be that way!'
YELL_QUESTION = 'Calm down, I know what I\'m doing!'


def response(hey_bob):
    if is_empty(hey_bob):
        return NOTHING

    if is_question(hey_bob):
        if is_yelling(hey_bob):
            return YELL_QUESTION
        else:
            return QUESTION

    else:
        if is_yelling(hey_bob):
            return YELL
        else:
            return ANYTHING_ELSE


def is_empty(string):
    return len(string.strip()) == 0


def is_question(string):
    return string.strip().endswith('?')


def is_yelling(string):
    return string.isupper()