class FiniteStateAutomaton:
    def __init__(self):
        self.transitions = {
            0: {'a': 1, 'b': 0},
            1: {'a': 1, 'b': 2},
            2: {'a': 1, 'b': 0}
        }
        self.current_state = 0

    def process_input(self, input_str):
        for char in input_str:
            if char not in self.transitions[self.current_state]:
                return False
            self.current_state = self.transitions[self.current_state][char]
        return self.current_state == 2

def main():
    automaton = FiniteStateAutomaton()

    test_strings = ['ab', 'aab', 'abb', 'aabb', 'abaab', 'bab', 'aaabb']

    for test_str in test_strings:
        if automaton.process_input(test_str):
            print(f"'{test_str}' matches the pattern")
        else:
            print(f"'{test_str}' does not match the pattern")

if __name__ == "__main__":
    main()
