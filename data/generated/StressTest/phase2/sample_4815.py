# Premise: If Dhoni paid a total of $38, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Hypothesis: If Dhoni paid a total of $less than 58, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Golden Label: entailment

rent_paid_premise = 38
rent_paid_hypothesis = 58

# the hypothesis refers to the rent paid by Dhoni, also mentioned in the premise
if rent_paid_hypothesis <= rent_paid_premise:
    # check if the estimate of 'rent_paid_hypothesis' contradicts the rent paid in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

