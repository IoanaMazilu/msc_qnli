sweets_division_premise = 5
sweets_division_hypothesis = 5
sweets_division_premise_alt = 6
sweets_division_hypothesis_alt = 6
sweets_division_premise_negative = 12

# the hypothesis refers to the number of people Jenny can divide her sweets to, mentioned in the premise
if sweets_division_hypothesis < sweets_division_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif sweets_division_hypothesis_alt != sweets_division_premise_alt:
    # check if the alternative number of people in the hypothesis contradicts the alternative number of people in the premise
    label = "contradiction"
elif sweets_division_premise_negative <= sweets_division_premise or sweets_division_premise_negative <= sweets_division_premise_alt:
    # check if the number of people she can't divide her sweets to contradicts the numbers of people she can divide her sweets to in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
