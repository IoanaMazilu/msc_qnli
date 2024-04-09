random_premise = 302
random_hypothesis = 102
scramjet_premise = 232
scramjet_hypothesis = 232
both_premise = 112
both_hypothesis = 112

# the hypothesis refers to the number of students studying each topic
if random_hypothesis <= random_premise:
    # check if the estimate of 'random_hypothesis' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif scramjet_hypothesis!= scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
elif both_hypothesis!= both_premise:
    # check if the number of students studying both Random-processing methods and Scramjet rocket engines in the hypothesis contradicts the number of students studying both reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
