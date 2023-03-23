def length_check(line, line_num):
    if len(line) > 79:
        print(f'Line {line_num}: S001 Too Long')


def indentation_check(line, line_num):
    while line:
        if line[0] == ' ':
            indent = line[:4]

            if indent == '    ':
                line = line[4:]
            else:
                print(f'Line {line_num}: S002 Indentation is not a multiple of four')
                break
        else:
            return


def semicolon_check(line, line_num):

    if not line:
        return

    if '#' in line:
        stripped = line.split('#', 1)[0].strip()
    else:
        stripped = line

    if stripped[-1:] == ';':
        print(f'Line {line_num}: S003 Unnecessary semicolon')

    return


def comment_space_check(line, line_num):
    if not line or '#' not in line:
        return

    split_line = line.split('#', 1)[0]

    if not split_line.endswith('  ') and split_line:
        print(f'Line {line_num}: S004 At least two spaces required before inline comments')


def todo_check(line, line_num):
    if not line or '#' not in line:
        return

    comment = line.split('#', 1)[1].lower()

    if 'todo' in comment:
        print(f'Line {line_num}: S005 TODO found')

def blank_lines_check(line, line_num, blank_lines):
    if not line:
        return blank_lines + 1
    if blank_lines > 2:
        print(f'Line {line_num}: S006 More than two blank lines used before this line')
        return 0
    return blank_lines



def main():
    with open(input(), 'r') as f:
        lines = [line.rstrip() for line in f]

        blank_lines = 0

        for i, line in enumerate(lines):

            line_num = i+1

            length_check(line, line_num)
            indentation_check(line, line_num)
            semicolon_check(line, line_num)
            comment_space_check(line, line_num)
            todo_check(line, line_num)
            blank_lines = blank_lines_check(line, line_num, blank_lines)


if __name__ == '__main__':
    main()



