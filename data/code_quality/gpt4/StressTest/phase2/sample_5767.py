parent_payback_premise = 4
parent_payback_hypothesis = 5

# the hypothesis refers to the same percentage of payback to parents
if parent_payback_hypothesis <= parent_payback_premise:
    # check if the hypothesis value contradicts the premise that Dana gives more than 'parent_payback_premise'
    label = "contradiction"
else:
    # the premise gives only a lower bound for the percentage of payback
    # any percentage greater than 'parent_payback_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
