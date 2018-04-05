"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(get_mark(score))


def get_mark(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()