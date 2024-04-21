import random


def generate_matrix():
    return [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]


def print_matrix_with_highlight(matrix, slice_type, index, start, length):
    print("\nMatrix with highlighted section:")
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            highlight = ((slice_type == 'row' and i == index and start <= j < start + length) or
                         (slice_type == 'column' and j == index and start <= i < start + length))
            print(f"**{val}**" if highlight else val, end=' ')
        print()


def get_slice(matrix):
    slice_type = random.choice(['row', 'column'])
    index = random.randint(0, 2)
    start = random.randint(0, 2)
    length = random.randint(1, 3 - start)
    return slice_type, index, start, length


def get_user_input(slice_type, index):
    slice_type_description = 'row' if slice_type == 'row' else 'column'
    example = '1:3 for second to third elements' if slice_type == 'row' else '0:2 for first to second rows'
    prompt = f"Enter the slice indices to extract from {slice_type_description} {index} (e.g., {example}): "
    slice_part = input(prompt)
    return slice_part


def parse_slice(slice_part, index, matrix, slice_info):
    slice_type, idx, start, length = slice_info
    try:
        start_idx, end_idx = map(int, slice_part.split(':'))
        slice_range = slice(start_idx, end_idx)

        if slice_type == 'column':
            selected_slice = [matrix[i][index] for i in range(*slice_range.indices(len(matrix)))]
        else:
            selected_slice = matrix[index][slice_range]

        correct_slice = matrix[idx][start:start + length] if slice_type == 'row' \
            else [matrix[i][idx] for i in range(start, start + length)]

        if selected_slice == correct_slice:
            return True, "Correct! Well done."
        else:
            return False, f"Incorrect slice. Try again. Expected was: {correct_slice}"
    except Exception as e:
        return False, f"Error: {e}. Please check your input format and try again."


def main():
    while True:
        matrix = generate_matrix()
        slice_type, index, start, length = get_slice(matrix)
        print("\nNew game started:")
        print_matrix_with_highlight(matrix, slice_type, index, start, length)

        attempts = 3
        correct = False
        while not correct and attempts > 0:
            slice_part = get_user_input(slice_type, index)
            correct, message = parse_slice(slice_part, index, matrix, (slice_type, index, start, length))
            print(message)
            if not correct:
                attempts -= 1
                if attempts == 0:
                    # Ensuring the correct answer is presented clearly
                    if slice_type == 'row':
                        correct_answer = f"matrix[{index}][{start}:{start + length}]"
                    else:
                        correct_answer = f"matrix[{start}:{start + length}][{index}]"
                    print(f"No more attempts left. The correct answer was: 'matrix{correct_answer}'.")

        if input("Do you want to play again? (yes/no): ").strip().lower() != "yes":
            print("Thanks for playing our game! Goodbye.")
            break


if __name__ == "__main__":
    main()