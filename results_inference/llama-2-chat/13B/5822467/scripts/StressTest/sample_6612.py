random_processing_premise = 312
scramjet_premise = 234
both_premise = 112

more_than_112_hypothesis = True

# the hypothesis refers to the number of students studying Random-processing methods and Scramjet rocket engines
if more_than_112_hypothesis and random_processing_premise <= both_premise:
    # check if the estimate of'more_than_112_hypothesis' contradicts the number of students studying both Random-processing methods and Scramjet rocket engines in the premise
    label = "contradiction"
elif scramjet_premise!= scramjet_hypothesis:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
