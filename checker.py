from collections import Counter
import random
import word_operations
import constants
import main
def get_response(word, *_o):
    if len(_o) == 0:
        other_word = constants.FINAL_WORD
    else:
        other_word = _o[0]
    answer = [constants.GREY_COLOR] * 5
    frvRem = Counter(other_word)
    for i in range(constants.STRING_LENGTH):
        if word[i] == other_word[i]:
            answer[i] = constants.GREEN_COLOR
            frvRem.subtract(word[i])
    for i in range(constants.STRING_LENGTH):
        if answer[i] != constants.GREEN_COLOR and frvRem[word[i]] > 0:
            answer[i] = constants.YELLOW_COLOR
            frvRem.subtract(word[i])
    return answer
        
def testing_tool():
    words = word_operations.getInitWords()
    average_score = 0
    efficiency = 0
    for i in range(2500):
        constants.FINAL_WORD = random.choice(words)
        print(constants.FINAL_WORD)
        answer = main.main(True)
        average_score += answer
        efficiency += (answer <= 6)
        print(f"Finished in {answer} rounds")
        print(f"Efficiency until now is {efficiency / (i + 1)}")
        print(f"The average score until now is {average_score / (i + 1)}")

if __name__ == '__main__':
    testing_tool()