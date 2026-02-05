from extension_methods.extensions import extension


def test_extension():
    # Assign
    input = 7

    # Act
    @extension(to=int)
    def double(x: int) -> int:
        return x * 2

    output = input | double()

    # Assert
    assert 2 * input == output
