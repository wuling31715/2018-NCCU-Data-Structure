import random 
import time 

def main():
    global final_answer, game_continue, round_times
    final_answer = answer_create()
    print(final_answer)
    game_continue = True 
    round_times = 1
    while game_continue:
        guess_input = input('-' * 10 + '\n')
        if answer_check(guess_input):
            pass
        else:
            hint = get_hint(guess_input)
            print(hint)
        round_times = round_times + 1

def answer_create():
    number = [i for i in range(10)]
    random_number = random.sample(number, 4)
    answer = ''
    for i in random_number:
        answer = answer + str(i)
    return answer    

def answer_check(guess_input):
    global game_continue, round_times 
    if final_answer == guess_input:
        game_continue = False
        print('4 A 0 B\nRound Times: %d' % (round_times))
        return True
    else:
        return False

def get_hint(guess_input):
    global final_answer
    A = 0
    B = 0
    final_answer_tmp = ''
    guess_input_tmp = ''
    for i, j in zip (final_answer, guess_input):
        if i == j:
            A = A + 1
        else:
            final_answer_tmp = final_answer_tmp + i
            guess_input_tmp = guess_input_tmp + j
    for i in final_answer_tmp:
        for j in guess_input_tmp:
            if i == j:
                B = B + 1
    return '%d A %d B' % (A, B)            

time_start = time.time()
main()
time_end = time.time()
time_used = time_end - time_start
print('Time Used: %d (s)' % (round(time_used)))
