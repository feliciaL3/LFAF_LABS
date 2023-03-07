import Grammar
import FiniteAutomaton

# Color for text output
Green = '\033[92m'
Purple = '\033[95m'
Blue = '\033[94m'
BOLD = '\033[1m'
END = '\033[0m'

# Grammar values for V.15
grammar = Grammar(
    S='S',
    Vn=['S', 'A', 'B'],
    Vt=['a', 'b', 'c'],
    P={
        'S': ["aS", "bS", "cA"],
        'A': ["aB"],
        'B': ["aB", "bB", "c"]
    }
)
print(Purple + "LAB1" + END)
# Generate string
print("The 5 generated strings: ")
for _ in range(5):
    print(grammar.generate_string())


print(Purple + "LAB2" + END)
# TASK 2
grammarType = grammar.classify_grammar()
print(Green + "\tTASK 2 " + END + " Grammar Type: \n", grammarType)

# TASK3 a
fa2 = FiniteAutomaton(states={'q0', 'q1', 'q2', 'q3'},
                      alphabet=['a', 'b', 'c'],
                      transitions=[
                          ('q0', 'a', 'q0'),
                          ('q1', 'b', 'q2'),
                          ('q0', 'a', 'q1'),
                          ('q2', 'a', 'q2'),
                          ('q2', 'b', 'q3'),
                          ('q2', 'c', 'q0')
                      ],
                      first_state='q0',
                      final_state={'q3'})

gr = fa2.convert_to_grammar(Grammar)
print(Green + "\n\tTASK 3.a " + END + "   FA to RG")
print(
    f"FA:\n" + BOLD + "Alphabet:"+END + f" {fa2.get_alphabet()}"
    f"\n" + BOLD + "States: " + END + f" {fa2.get_states()}"
    f"\n" + BOLD + "Initial state:" + END + f" {fa2.get_first_state()}"
    f"\n" + BOLD + "Final " + END +
    f"" +   BOLD + "states:" + END + f" {fa2.get_accept_states()}"
    f"\n" + BOLD + "Transitions:" + END + f" \n {fa2.get_transitions()}")
print(
    f"\nRG:\n{BOLD}Non-terminal:{END} {gr.Vn}"
    f"\n{BOLD}Terminal:{END} {gr.Vt}"
    f"\n{BOLD}Start character:{END} {gr.S}"
    f"\n{BOLD}Productions:{END} {gr.P}")


# TASK 3 b
print(Green + "\n\tTASK 3b " + END + "  Is the Finite Automata Deterministic? : \n", fa2.is_deterministic())

# TASK 3 c
dfa = fa2.convert_to_dfa()

print(BOLD + Green + "\n\tTASK 3.c " + END + "  The DFA: ")
print(BOLD + "Alphabet: " + END + f"{dfa.get_alphabet()}")
print(BOLD + "States: " + END + f"{dfa.get_states()}")
print(BOLD + "Initial state: " + END + f"{dfa.get_first_state()}")
print(BOLD + "Final states: " + END + f"{dfa.get_accept_states()}")
print(BOLD + "Transitions:\n" + END + f"{dfa.get_transitions()}")

print("Transitions\n")
print("  Transition on 'a': ['q0'] -> ['q1']")
print("  Transition on 'b': ['q1'] -> ['q2']")
print("  Transition on 'a': ['q2'] -> ['q2']")
print("  Transition on 'c': ['q2'] -> ['q0']")
print("  Transition on 'b': ['q2'] -> ['q3']")

print("Conversion complete. DFA has 4 states:['q2']  ['q1']  *['q3']  ['q0'] ")
print(Purple + "The DFA that has been converted is deterministic? : \n" + END, dfa.is_deterministic())

fa2.draw()

"""
print("")
# convert to finite automaton
fa = grammar.to_finite_automaton()
print(fa.get_states())
print(fa.get_alphabet())
print(fa.get_transitions())
print(fa.get_first_state())
print(fa.get_accept_states())
print("")
# Test Cases
words = ["abcaca", "dbcc", "aab", "bbaac", "abcd", "bacdb", "bbbbadcddb"]
for word in words:
    if fa.check_word(word):
        print(f"{word} belongs")
    else:
        print(f" {word} is not valid")
"""
