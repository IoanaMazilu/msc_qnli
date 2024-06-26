random_processing_premise = 312
scramjet_premise = 234
both_premise = 112

random_processing_hypothesis = 212
scramjet_hypothesis = 234
both_hypothesis = 112

# the hypothesis refers to the number of students studying each topic
if random_processing_hypothesis <= random_processing_premise:
    # check if the estimate of 'random_processing_hypothesis' contradicts the number of students studying random processing methods in the premise
    label = "contradiction"
elif scramjet_hypothesis!= scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
