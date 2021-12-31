class Judge:
    def __init__(self, answer: str) -> None:
        """
        Set the answer as the attribute of Judge
        answer: (int) the final answer
        """
        self.answer = answer
        # TODO

    def guess(self, num: str) -> bool:
        """
        Method that guess the number, it'll print info that shows:
            Your guess is ...; the result is xAxB
            e.g.: Your guess is 0123; the result is 0A1B
        num: the number that it guessed
        return: whether the player guess the correct answer
        """
        a = 0
        b = 0
        s1 = list(num)
        s2 = list(self.answer)
        S1 = list(map(int, s1))
        S2 = list(map(int, s2))
        for i in range(0,len(num)):
            for j in range(0,len(num)):
                if S1[j] == S2[i] and i == j:
                    a += 1
                elif S1[j] == S2[i]:
                    b += 1
        print(f"Your guess is {num}; the result is {a}A{b}B")
        if a == len(num):
            return True
        else:
            return False
        # TODO


def read_input(guess_len: int) -> str:
    """
    Function that read player's guess.
    guess_len: length the the player should guess. it would be same as the length of answer
    return: the valid string guessed by player

    You should show the hint message:
        "Enter your guess:\n"
    If the player's guess is invalid, you should print:
        "Invalid, please enter your guess again:\n"
    Note: a valid guess means contain only guess_len non-repetitive integer range from 0~9
    """
    print("Enter your guess:")
    while True:
        my_guess = input()
        list1 = list(my_guess)
        if len(my_guess) == guess_len and my_guess.isdigit() and len(set(list1)) == len(list1):
            return my_guess
        else:
            print("Invalid, please enter your guess again:")
    # TODO


def enter_answer() -> str:
    """
    Function that enter the answer, you can assume that the answer must be valid.
    """
    s = input()
    return s
    # TODO
