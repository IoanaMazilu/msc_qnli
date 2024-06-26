# define variables for the number of students studying Random-processing methods, Scramjet rocket engines and both
studying_random_premise = 302
studying_random_hypothesis = 102
studying_scramjet_premise = 232
studying_scramjet_hypothesis = 232
studying_both_premise = 112
studying_both_hypothesis = 112

# the hypothesis talks about the number of students studying Random-processing methods, Scramjet rocket engines and both, referenced also in the premise
if studying_random_hypothesis >= studying_random_premise:
    # check if the hypothesis value contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif studying_scramjet_hypothesis!= studying_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
elif studying_both_hypothesis!= studying_both_premise:
    # check if the number of students studying both Random-processing methods and Scramjet rocket engines in the hypothesis contradicts the number of students studying both Random-processing methods and Scramjet rocket engines reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
