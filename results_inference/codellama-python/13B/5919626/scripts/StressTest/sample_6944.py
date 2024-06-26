people_room_premise = 10
people_room_hypothesis = 10

# the hypothesis talks about the number of people in the room, which is consistent with the premise
if people_room_hypothesis!= people_room_premise:
    # check if the hypothesis value contradicts the estimate of 'people_room_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the room
    # any number of people equal to 'people_room_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
