interest_rate_premise = 8
interest_rate_hypothesis = 6

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_premise <= interest_rate_hypothesis:
    # check if the estimate of 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
