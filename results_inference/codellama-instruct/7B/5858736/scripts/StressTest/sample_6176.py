walking_time_premise = 15
train_time_premise = 0

# the hypothesis refers to the total time it takes Darcy to commute to work by walking and riding the train
if walking_time_premise + train_time_premise <= walking_time_hypothesis:
    # check if the estimate of 'walking_time_hypothesis' contradicts the total time it takes Darcy to commute to work by walking
    label = "contradiction"
else:
    # the premise gives only an estimate for the total time it takes Darcy to commute to work by walking
    # any number of minutes greater than 'walking_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
