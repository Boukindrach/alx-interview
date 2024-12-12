#!/usr/bin/python3
"""Something"""


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_round(n):
    """
    Play a single round of the prime game.
    Returns True if Maria wins, False if Ben wins.
    """

    available = set(range(1, n + 1))

    maria_turn = True

    while True:
        primes = [num for num in available if is_prime(num)]

        if not primes:
            return not maria_turn

        chosen_prime = min(primes)

        to_remove = set()
        for num in available:
            if num % chosen_prime == 0:
                to_remove.add(num)

        available -= to_remove

        maria_turn = not maria_turn


def isWinner(x, nums):
    """
    Determine the overall winner of x rounds of prime game.

    :param x: Number of rounds
    :param nums: List of n values for each round
    :return: Name of the player who won the most rounds, or None
    """

    if not x or not nums or len(nums) != x:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
