random_premise = 102
random_hypothesis = 302
scramjet_premise = 232
scramjet_hypothesis = 232
both_premise = 112
both_hypothesis = 112

# the hypothesis talks about the number of students studying each topic
if random_hypothesis <= random_premise:
    # check if the hypothesis value contradicts the estimate of more than 'random_premise'
    label = "contradiction"
elif scramjet_hypothesis!= scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
elif both_hypothesis!= both_premise:
    # check if the number of students studying both topics in the hypothesis contradicts the number of students studying both topics reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
