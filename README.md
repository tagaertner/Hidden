Your goal is to find a hidden message in a data structure.

The data structure will be a ragged matrix, represented by a tuple of tuples of strings. Each string will be a single character, but each inner tuple may have a different length. For example:

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)

Your function will receive a `matrix` and a positive integer, `n`. The integer `n` represents how frequently to select characters from the matrix.

Your code should iterate over the matrix row-wise and create a string containing every `n`th character from the iteration. For example, with the above matrix, `matrix_1` and an `n` of 2, the first character of the result string should be 'u', then 'r', then ' ', then 'd', and so on.

For this example of `matrix_1` and `n = 2`, the secret message is 'ur doing great'. See the tests in the [`main.py`](main.py) file for more examples.