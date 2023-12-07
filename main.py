
FOLDER = {}


def input_error(func):
    def wrapper(args):
        try:
            return func(*args)
        except TypeError as err:
            return f'Incorrect input: {err}'
        except KeyError as err:
            return f'User not found: {err}'
        except ValueError as err:
            return f'User already exists: {err}'
        except IndexError as err:
            return f'Index error catched: {err}'
    return wrapper


@input_error
def add_user_handler(name, phone):
    if name in FOLDER.keys():
        raise ValueError
    FOLDER[name] = phone
    return f'User {name} was added!'


@input_error
def change_phone_handler(name, phone):
    if name not in FOLDER.keys():
        raise KeyError
    FOLDER[name] = phone
    return 'Phone number changed!'


@input_error
def find_phone_handler(name):
    return FOLDER[name]


@input_error
def show_all_handler():
    return FOLDER


COMMANDS = {
    'add': add_user_handler,
    'change': change_phone_handler,
    'phone': find_phone_handler,
    'show all': show_all_handler,
}


def get_hendler(command):
    return COMMANDS[command]


def main():
    while True:
        user_input = input('>>> ').strip().lower()

        if user_input == 'hello':
            print('How can I help you?')
            continue

        if user_input in ('good bye', 'close', 'exit', '.'):
            print('Good bye!')
            break

        if user_input == 'show_all':
            res = get_hendler(user_input)
            print(res())
            continue

        command, *args = user_input.split(' ')

        if command not in COMMANDS.keys():
            print('Wrong command! Try again)')
            continue

        handler_func = get_hendler(user_input)
        print(handler_func(args))


if __name__ == '__main__':
    main()
