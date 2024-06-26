days_premise = 30
days_hypothesis = 80

# the hypothesis refers to the number of days Lexi needed to save for a vacation, as mentioned in the premise
if days_hypothesis <= days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
elif days_hypothesis > days_premise:
    # if the hypothesis value is greater than the number of days in the premise, it can be entailed from the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the number of days in the premise, it can be neutral
    label = "neutral"

print(label)
