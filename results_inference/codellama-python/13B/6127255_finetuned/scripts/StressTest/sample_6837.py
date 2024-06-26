earning_premise = 9000
earning_hypothesis = 4000

# the hypothesis refers to the total earnings mentioned in the premise
if earning_premise <= earning_hypothesis:
    # check if the estimate of 'earning_hypothesis' contradicts the earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
# 