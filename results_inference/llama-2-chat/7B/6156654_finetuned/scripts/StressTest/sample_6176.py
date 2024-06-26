walk_train_premise = 15
walk_train_hypothesis = 15

# the hypothesis talks about the difference in commute time between walking and train, which is also mentioned in the premise
if walk_train_hypothesis <= walk_train_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is a premise entailment
    label = "entailment"

print(label)
