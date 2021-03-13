import sys
commands = ("plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "line-break")


def done(result_string):
    file = open('output.md', 'w', encoding='utf-8')
    file.write(result_string)
    file.close()
    sys.exit()


def help_message():
    print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
Special commands: !help !done""")


def unknown_formatting_message():
    print("Unknown formatting type or command")


def check_command(command):
    return command in commands


def get_text(message="Text:"):
    return input(message)


def bold():
    return f"**{get_text()}**"


def italic():
    return f"*{get_text()}*"


def inline_cod():
    return f"`{get_text()}`"


def line_break():
    return "\n"


def plain_text():
    return get_text()


def header():
    level = int(get_text("Level:"))
    return f"{'#' * level} {get_text()}\n"


def link():
    label = get_text("Label:")
    url = get_text("URL:")
    return f"[{label}]({url})"


def md_list(list_type="unordered"):
    while True:
        rows_num = int(input("Number of rows:"))
        if rows_num > 0:
            break
        print("The number of rows should be greater than zero")

    rows = [input(f'Row #{idx + 1}: ') for idx in range(rows_num)]
    if list_type == "unordered":
        rows = map(lambda item: f"* {item}", rows)
    else:
        rows = map(lambda item, idx: f"{idx}. {item}", rows, range(1, len(rows) + 1))

    return "\n".join(rows) + "\n"


def unordered_list():
    return md_list("unordered")


def ordered_list():
    return md_list("ordered")


def concat_text(operator, result_string):
    return f"{result_string}{operator()}"


def create_unordered_list_item(string):
    return f"* {string}"


operators = {
    "header": header,
    "plain": plain_text,
    "link": link,
    "bold": bold,
    "italic": italic,
    "inline-code": inline_cod,
    "line-break": line_break,
    "unordered-list": unordered_list,
    "ordered-list": ordered_list
}


def markdown():
    run = True
    result_string = ""
    while run:
        command = input("Choose a formatter:").strip()
        if command == "!done":
            done(result_string)
        if command == "!help":
            help_message()
        elif not check_command(command):
            unknown_formatting_message()
        else:
            result_string = concat_text(operator=operators[command], result_string=result_string)
            print(result_string)


markdown()
