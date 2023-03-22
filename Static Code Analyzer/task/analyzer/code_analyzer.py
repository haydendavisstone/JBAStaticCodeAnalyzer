with open(input(), 'r') as f:
    lines = [line.rstrip() for line in f]

    for i, l in enumerate(lines):
        if len(l) > 79:
            print(f'Line {i+1}: S001 Too Long')
