earnings_premise = 9000
earnings_hypothesis = 4000

# the hypothesis refers to the earnings mentioned in the premise
if earnings_premise <= earnings_hypothesis:
    # check if the estimate of 'earnings_hypothesis' contradicts the earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)