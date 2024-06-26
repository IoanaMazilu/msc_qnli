people_room_premise = 10
people_room_hypothesis = 10

# the hypothesis talks about the number of people in the room, referenced also in the premise
if people_room_hypothesis!= people_room_premise:
    # check if the number of people in the room in the hypothesis contradicts the number of people in the room reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are consistent with each other
    label = "entailment"

print(label)
