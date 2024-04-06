# Premise: New York (CNN) -- Her teachers knew she loved to doodle on her tests and homework, but no one thought Olivia Bouler's drawing skills would raise more than $110,000 to help birds affected by the Gulf oil spill.
# Hypothesis: So far, she's raised more than $110,000.
# Golden Label: neutral

raised_money_premise = 110000
raised_money_hypothesis = 110000

# the hypothesis mentions the amount of money raised, which is also mentioned in the premise
if raised_money_hypothesis != raised_money_premise:
    # check if the money raised in the hypothesis contradicts the money raised reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

