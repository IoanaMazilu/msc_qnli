baseball_fans_premise = 330
baseball_fans_hypothesis = 130

# The hypothesis refers to the number of baseball fans mentioned in the premise
if baseball_fans_premise <= baseball_fans_hypothesis:
    # check if the estimate of 'baseball_fans_hypothesis' contradicts the number of baseball fans in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
