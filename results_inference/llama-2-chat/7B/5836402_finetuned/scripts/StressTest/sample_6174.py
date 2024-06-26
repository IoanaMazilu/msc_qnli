walk_train_minutes_premise = 15
walk_train_minutes_hypothesis = 55

# the hypothesis refers to the difference in minutes between walking and train commute mentioned in the premise
if walk_train_minutes_hypothesis >= walk_train_minutes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'walk_train_minutes_premise'
    label = "contradiction"
elif walk_train_minutes_hypothesis < walk_train_minutes_premise:
    # if the hypothesis value is less than the premise one, it is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
