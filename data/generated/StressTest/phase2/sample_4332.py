# Premise: Nitin borrowed some money at the rate of 6% p.
# Hypothesis: Nitin borrowed some money at the rate of more than 4% p.
# Golden Label: entailment

interest_rate_premise = 6
interest_rate_hypothesis = 4

# the hypothesis refers to the interest rate of borrowed money mentioned in the premise
if interest_rate_premise <= interest_rate_hypothesis:
    # check if the estimate of 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

