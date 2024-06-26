people_room_premise = 10
people_room_hypothesis = 10

# the hypothesis talks about the number of people in the room, referenced also in the premise
if people_room_hypothesis!= people_room_premise:
    # check if the hypothesis value contradicts the estimate of 'people_room_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of people in the room, but it does not explicitly entail the hypothesis
    label = "neutral"

print(label)
