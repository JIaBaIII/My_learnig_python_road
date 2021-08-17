def make_txt_black(fn):
    def wrapped():
        return "\033[30m" + fn() + "\033[0m"
    return wrapped


def make_txt_red(fn):
    def wrapped():
        return "\033[31m" + fn() + "\033[0m"
    return wrapped


def make_txt_green(fn):
    def wrapped():
        return "\033[32m" + fn() + "\033[0m"
    return wrapped


def make_txt_yellow(fn):
    def wrapped():
        return "\033[33m" + fn() + "\033[0m"
    return wrapped


def make_txt_blue(fn):
    def wrapped():
        return "\033[34m" + fn() + "\033[0m"
    return wrapped


def make_txt_purple(fn):
    def wrapped():
        return "\033[35m" + fn() + "\033[0m"
    return wrapped


def make_txt_light_blue(fn):
    def wrapped():
        return "\033[36m" + fn() + "\033[0m"
    return wrapped


def make_txt_white(fn):
    def wrapped():
        return "\033[37m" + fn() + "\033[0m"
    return wrapped


def make_txt_bold(fn):
    def wrapped():
        return "\033[1m" + fn() + "\033[0m"
    return wrapped


def make_txt_faded(fn):
    def wrapped():
        return "\033[2m" + fn() + "\033[0m"
    return wrapped


def make_txt_italics(fn):
    def wrapped():
        return "\033[3m" + fn() + "\033[0m"
    return wrapped


def make_txt_underlined(fn):
    def wrapped():
        return "\033[4m" + fn() + "\033[0m"
    return wrapped


def make_txt_0(fn):
    def wrapped():
        return "\033[0m" + fn() + "\033[0m"
