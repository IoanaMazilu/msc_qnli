# Premise: 3750 from Anwar at 6% p.
# Hypothesis: less than 7750 from Anwar at 6% p.
# Golden Label: entailment

amount_from_anwar_premise = 3750
amount_from_anwar_hypothesis = 7750

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_from_anwar_premise >= amount_from_anwar_hypothesis:
    # check if the value of 'amount_from_anwar_premise' contradicts the estimate of less than 'amount_from_anwar_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

