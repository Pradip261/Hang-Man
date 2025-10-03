word_list=['elephant','buffalo','monkey'] # list of words 

# choose random variable.
import random
choosen_word=random.choice(word_list)
#print(choosen_word)

#showing line.
show_dash=""
for x in choosen_word:
    show_dash+="-"
print("  "+show_dash)

# run the loop.
life=len(choosen_word)        ## calculate life
print(f"You have total {life} life.")
old_guess=[None]*len(choosen_word)
gussed_word=0
while(gussed_word!=len(choosen_word)):
    guess=input("Enter your gussed letter:").lower()
    count=0
    flag=0
    for i in range(len(choosen_word)):
        if choosen_word[i]==guess:
            count=choosen_word.count(guess)
            #print(count)
            if guess in show_dash: # turning off the repeatetion
                if count==1:
                    flag=1
                    print(f"There is no more {guess}")
                    continue
                elif count>1:
                    if guess==old_guess[i]:
                        print(f"There is no more {guess}")
                        flag=1
                        continue
            show_dash=list(show_dash)
            show_dash[i]=guess
            show_dash=''.join(show_dash)
            print("  "+show_dash)
            flag=1
            gussed_word+=1
            old_guess[i]=guess
    if flag!=1:
        print("  Life Lost")
        life-=1
        print(f"life={life}")
        if life==0:
            print("----------You Loose----------")
            break
    #print("Gussed word=",gussed_word)
if life!=0:
    print("----------You Won----------")
