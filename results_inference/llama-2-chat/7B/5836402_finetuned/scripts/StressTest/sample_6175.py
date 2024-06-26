walk_train_premise = 55
walk_train_hypothesis = 15

# the hypothesis refers to the difference in commute time between walking and train, mentioned in the premise
if walk_train_hypothesis >= walk_train_premise:
    # check if the hypothesis value contradicts the estimate of less than 'walk_train_premise'
    label = "contradiction"
elif walk_train_hypothesis < walk_train_premise:
    # check if the hypothesis value is less than the estimate of 'walk_train_premise'
    label = "entailment"
else:
    # if the hypothesis value is equal to the estimate, it is neutral
    label = "neutral"

print(label)
