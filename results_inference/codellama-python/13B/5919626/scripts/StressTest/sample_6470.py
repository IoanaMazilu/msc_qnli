people_room_premise = 10
people_room_hypothesis = 10

# the premise and hypothesis refer to the same number of people in the room
if people_room_premise!= people_room_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'people_room_premise'
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same number of people in the room
    label = "entailment"

print(label)