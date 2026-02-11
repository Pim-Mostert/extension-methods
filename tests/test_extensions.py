from extensionmethods import extension


def test_extension():
    # Assign
    @extension
    def double(x: int) -> int:
        return x * 2

    # Act
    output = 7 | double()

    # Assert
    assert output == 7 * 2


@extension
def add(x: int, to_add: int) -> int:
    """
    Adds to the input.
    """
    return x + to_add


output = 7 | add(11)


def test_extension_single_parameter():
    # Assign
    @extension
    def add(x: int, to_add: int) -> int:
        return x + to_add

    # Act
    output = 7 | add(11)

    # Assert
    assert 7 + 11 == output


def test_extension_two_parameters():
    # Assign
    @extension
    def add_then_multiply(x: int, to_add: int, to_multiply: int) -> int:
        return (x + to_add) * to_multiply

    # Act
    output = 7 | add_then_multiply(11, 3)

    # Assert
    assert (7 + 11) * 3 == output
