people_room_premise = 10
people_room_hypothesis = 10

# the hypothesis talks about the number of people in a room, referenced also in the premise
if people_room_hypothesis!= people_room_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of people in the room
    # the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)
