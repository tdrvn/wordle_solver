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
        
def testing_tool(logs):
    words = word_operations.getInitWords('answer_words.txt')
    average_score = 0
    efficiency = 0
    for i in range(len(words)):
        constants.FINAL_WORD = words[i]

        with open(logs,'a') as out:
            print(constants.FINAL_WORD)
            out.write(constants.FINAL_WORD + '\n')
            
        answer = main.main(True)
        efficiency += (answer <= 6)
        if efficiency:
            average_score += answer
        with open(logs,'a') as out:
            out.write(f"Finished in {answer} rounds\n")
            print(f"Finished in {answer} rounds")
            out.write(f"Efficiency until now is {efficiency / (i + 1)}\n")       
            out.write(f"The average score until now is {average_score / (i + 1)}\n")

if __name__ == '__main__':
    testing_tool('logs2-onlyAnswers.txt')