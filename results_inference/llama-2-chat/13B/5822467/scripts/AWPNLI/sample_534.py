birds_on_fence_premise = 12.0
birds_fly_away_premise = 8.0
birds_on_fence_hypothesis = 4.0

# compute the difference between the number of birds on the fence in the premise and the hypothesis
difference = birds_on_fence_premise - birds_on_fence_hypothesis

# check if the difference is greater than zero
if difference > 0:
    # if the difference is greater than zero, the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the difference is zero or negative, the hypothesis is consistent with the premise
    label = "entailment"

print(label)
