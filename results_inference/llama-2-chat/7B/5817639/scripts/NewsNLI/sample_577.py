theme_premise = "central theme"
competition_hypothesis = "others competed"

# check if the hypothesis contradicts the premise
if theme_premise!= competition_hypothesis:
    label = "contradiction"
elif competition_hypothesis > theme_premise:
    # check if the number of competitors in the hypothesis is greater than the number of competitors in the premise
    label = "entailment"
else:
    label = "neutral"

print(label)
