def encodify(letter, k):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alphabet = {}
        for i in range(len(letters)):
            index = i + 1 + k
            if index > 26:
                index = index%26
            alphabet[letters[i]] = index
        return alphabet[letter]

def matrixify(message, width, k):
    height = len(message) / width
    if height%1 != 0:
        height += 1
    height = int(height)
    matrix = [[0] * width for i in range(height)]

    coded_message = letters_to_numbers(message, width, k)

    for i in range(height):
        for j in range(width):
            next_letter = i*(width)+j
            if next_letter > len(message)-1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = encodify(message[next_letter], k)
    return matrix



print(encodify('y', 3))
