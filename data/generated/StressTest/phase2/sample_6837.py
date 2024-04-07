# Premise: 9000 which he and Rick earned at the end of one year.
# Hypothesis: more than 4000 which he and Rick earned at the end of one year.
# Golden Label: entailment

earnings_premise = 9000
earnings_hypothesis = 4000

# the hypothesis refers to the earnings mentioned in the premise
if earnings_premise <= earnings_hypothesis:
    # check if the estimate of 'earnings_hypothesis' contradicts the earnings in the premise
    label = "contradiction"
else:
    # if the earnings in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

