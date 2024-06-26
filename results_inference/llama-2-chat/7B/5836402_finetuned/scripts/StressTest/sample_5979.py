seniors_premise = 300
cars_premise = 50
seniors_hypothesis = 600
cars_hypothesis = 50

# the hypothesis refers to the number of seniors and cars mentioned in the premise
if seniors_premise <= seniors_hypothesis:
    # check if the estimate of'seniors_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
elif cars_premise!= cars_hypothesis:
    # check if the number of cars in the hypothesis contradicts the number of cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
