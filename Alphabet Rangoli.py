def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase

    for i in range(size - 1, -size, -1):
        row = []
        for j in range(abs(i), size):
            row.append(alphabet[j])
        print('-'.join(row[::-1] + row[1:]).center(4 * size - 3, '-'))
