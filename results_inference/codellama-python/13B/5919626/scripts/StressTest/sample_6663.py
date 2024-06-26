people_room_premise = 10
people_room_hypothesis = 5

# the hypothesis talks about the number of people in the room, referenced also in the premise
if people_room_hypothesis >= people_room_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_room_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_room_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
