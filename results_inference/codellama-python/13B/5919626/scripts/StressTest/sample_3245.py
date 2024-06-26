people_room_premise = 10
people_room_hypothesis = 10

# the hypothesis talks about the same number of people in the room as the premise
if people_room_premise!= people_room_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'people_room_premise'
    label = "contradiction"
else:
    # the premise and hypothesis values are the same, so we can infer entailment
    label = "entailment"

print(label)
