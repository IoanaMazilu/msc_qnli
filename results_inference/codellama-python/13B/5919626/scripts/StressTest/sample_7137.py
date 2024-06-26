people_room_premise = 10
people_room_hypothesis = 10

# the hypothesis talks about the number of people in the room, which is also mentioned in the premise
if people_room_premise!= people_room_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'people_room_premise'
    label = "contradiction"
else:
    # the premise and hypothesis values are the same, so we can infer entailment
    label = "entailment"

print(label)
