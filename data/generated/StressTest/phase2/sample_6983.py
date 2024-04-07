# Premise: Nitin borrowed some money at the rate of 6% p.
# Hypothesis: Nitin borrowed some money at the rate of 8% p.
# Golden Label: contradiction

borrow_rate_premise = 6
borrow_rate_hypothesis = 8

# the hypothesis talks about the interest rate at which Nitin borrowed some money, which is also mentioned in the premise
if borrow_rate_hypothesis != borrow_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the interest rate in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

