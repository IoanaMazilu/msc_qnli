# the hypothesis talks about the time required by a train to cover the distance between Chennai and Jammu, referenced also in the premise
if train_time_hypothesis == train_time_premise:
    # check if the hypothesis value contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives an exact time for the train journey
    # any time greater than 'train_time_premise' contradicts the premise
    label = "contradiction"

print(label)
