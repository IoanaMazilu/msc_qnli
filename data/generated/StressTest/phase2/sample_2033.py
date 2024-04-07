# Premise: Jisha walked for 3 days.
# Hypothesis: Jisha walked for 2 days.
# Golden Label: contradiction

walk_days_premise = 3
walk_days_hypothesis = 2

# the hypothesis refers to the number of days Jisha walked, as also mentioned in the premise
if walk_days_hypothesis == walk_days_premise:
    # check if the number of days in the hypothesis matches the number of days in the premise
    label = "entailment"
elif walk_days_hypothesis < walk_days_premise:
    # check if the number of days in the hypothesis is less than the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not match the premise value but also is not less than the premise value, we can infer neutrality
    label = "neutral"

print(label)

