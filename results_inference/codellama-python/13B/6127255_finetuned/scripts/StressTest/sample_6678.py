ages_sum_premise = 93
ages_sum_hypothesis = 43

# the hypothesis refers to the sum of ages of Aswin, Sachin and Sumesh mentioned in the premise
if ages_sum_premise <= ages_sum_hypothesis:
    # check if the estimate of 'ages_sum_hypothesis' contradicts the sum of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
