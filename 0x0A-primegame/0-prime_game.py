#!/usr/bin/python3
'''
0. Prime Game
'''


def isWinner(x, nums):
    '''
    number of rounds and nums is an array of n
    '''
    def is_prime(num):
        '''nnmnbbhhhh
        '''
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        '''
        fgghuyuuuuu
        '''
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        '''
        ghhjjjigff
        '''
        primes = get_primes(n)
        maria_turn = True

        while primes:
            selected_prime = primes.pop(0)
            nums = [num for num in nums if num % selected_prime != 0]

            # Check if the player cannot make a move
            if not nums:
                return "Ben" if maria_turn else "Maria"

            maria_turn = not maria_turn

    maria_wins = 0
    ben_wins = 0

    for round_num in range(x):
        winner = play_round(nums[round_num])

        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
