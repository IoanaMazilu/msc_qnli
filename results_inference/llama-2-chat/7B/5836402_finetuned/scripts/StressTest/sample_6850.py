apples_premise = 20
apples_hypothesis = 10

# the hypothesis refers to the number of apples Billy has, which is also mentioned in the premise
if apples_premise <= apples_hypothesis:
    # check if the estimate of 'apples_hypothesis' contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
