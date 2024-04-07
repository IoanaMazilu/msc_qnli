# Premise: 3900 from Anwar at 6% p.
# Hypothesis: more than 1900 from Anwar at 6% p.
# Golden Label: entailment

amount_premise = 3900
amount_hypothesis = 1900
interest_rate = 6  # same in both premise and hypothesis

# the hypothesis refers to an amount and interest rate mentioned in the premise
if amount_premise < amount_hypothesis:
    # check if the amount in the premise contradicts the estimate of 'more than amount_hypothesis' in the hypothesis
    label = "contradiction"
elif amount_premise == amount_hypothesis:
    # check if the amount in the premise contradicts the estimate of 'more than amount_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

