walk_days_premise = 3
walk_days_hypothesis = 3

# the hypothesis refers to the number of days Panjali walked, also mentioned in the premise
if walk_days_hypothesis < walk_days_premise:
    # check if the 'walk_days_hypothesis' contradicts the number of days walked in the premise
    label = "entailment"
else:
    # if the 'walk_days_hypothesis' is not less than 'walk_days_premise', it contradicts the premise
    label = "contradiction"

print(label)
