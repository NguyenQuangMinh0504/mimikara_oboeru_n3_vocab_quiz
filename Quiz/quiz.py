
import copy
import random
def quiz(data):
    for i in range(9999999999):
        a_random_number = random.randint(0,len(data)-1)
        set_meaning = data[a_random_number][1]
        len_set = len(set_meaning)
        a_random_meaning = set_meaning[random.randint(0,len_set-1)]
        print('------------------') 
        print(a_random_meaning)
        guest = input('your answer: ')
        if guest == data[a_random_number][0][0]:
            if len(data[a_random_number]) == 4:
                print('correct')
                print('the pronunciation is: ',data[a_random_number][2][0])
                print('kanji is: ',data[a_random_number][3][0])
            elif len(data[a_random_number]) == 3:
                print('correct')
                print('the pronunciation is: ',data[a_random_number][2][0])
            else:
                print('correct')
                

        else:
            if len(data[a_random_number]) == 4:
                print('incorrect')
                print('the right answer is:',data[a_random_number][0][0])
                print('the pronunciation is: ',data[a_random_number][2][0])
                print('kanji is: ',data[a_random_number][3][0])
                
            elif len(data[a_random_number]) == 3:
                print('incorrect')
                print('the right answer is:',data[a_random_number][0][0])
                print('the pronunciation is: ',data[a_random_number][2][0])
            else:
                print('incorrect')
                print('the right answer is:',data[a_random_number][0][0])

def quiz_reverse_2_times(data):
    data1 = copy.deepcopy(data)
    for i in range(99999999999999):
        if len(data1) == 0:
            print('\n============================')
            print('FINISH')
            print('AMAZING GOOD JOB !!!!')
            print('============================')
            break
        else:
            print('---------------')
            print('number of words: ',len(data1))
            a_random_number = random.randint(0,len(data1)-1)
            print(data1[a_random_number][0][0])
            guest1 = input('your meaning: ')
            guest2 = input('and how to read: ')
            
            
            if guest1 in data1[a_random_number][1] and guest2 in data1[a_random_number][2]:    
                print('\ncorrect')
                print('the pronunciation is: ',data1[a_random_number][2][0])
                print('kanji is: ',data1[a_random_number][3][0])
                data1.pop(a_random_number)
            else:
                print('incorrect')
                print('the right answer is: ',', '.join(data1[a_random_number][1]))
                print('the pronunciation is: ',data1[a_random_number][2][0])
                print('kanji is: ',data1[a_random_number][3][0])

def quiz_reverse_1_time(data):
    data1 = copy.deepcopy(data)
    for i in range(99999999999999):
        if len(data1) == 0:
            print('\n============================')
            print('FINISH')
            print('AMAZING GOOD JOB !!!!')
            print('============================')
        else:
            print('---------------')
            print('number of words: ',len(data1))
            a_random_number = random.randint(0,len(data1)-1)
            print(data1[a_random_number][0][0])
            guest1 = input('your meaning: ')
             
            if guest1 in data1[a_random_number][1]:    
                print('\ncorrect')
                print('the pronunciation is: ',data1[a_random_number][2][0])
                print('kanji is: ',data1[a_random_number][3][0])
                data1.pop(a_random_number)
            else:
                print('incorrect')
                print('the right answer is: ',', '.join(data1[a_random_number][1]))
                print('the pronunciation is: ',data1[a_random_number][2][0])
                print('kanji is: ',data1[a_random_number][3][0])
                

            
def Check_In_Dict(data,word):
    for i in data:
        if word == i[0][0]:
            return 'Word in dictionary'
    return 'Word not in dictionary'

            
                
    
