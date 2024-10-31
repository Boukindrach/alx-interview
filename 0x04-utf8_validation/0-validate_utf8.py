#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: List of integers where each integer represents 1 byte of data

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    def get_num_of_ones(byte):
        mask = 1 << 7
        ones = 0
        while byte & mask:
            ones += 1
            mask >>= 1
        return ones
    i = 0
    while i < len(data):
        current_byte = data[i] & 255

        num_ones = get_num_of_ones(current_byte)

        if num_ones == 0:
            i += 1
        elif num_ones in [2, 3, 4]:
            if i + num_ones - 1 >= len(data):
                return False

            for j in range(i + 1, i + num_ones):
                next_byte = data[j] & 255
                if get_num_of_ones(next_byte) != 1 or (next_byte >> 6) != 2:
                    return False
            i += num_ones
        else:
            return False

    return True
