# Premise: 3600 from Anwar at 6% p.
# Hypothesis: more than 1600 from Anwar at 6% p.
# Golden Label: entailment

amount_premise = 3600
amount_hypothesis = 1600
interest_rate_premise = 6
interest_rate_hypothesis = 6

# the hypothesis refers to the amount and interest rate mentioned in the premise
if amount_premise < amount_hypothesis:
    # check if the 'amount_hypothesis' contradicts the amount in the premise
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

