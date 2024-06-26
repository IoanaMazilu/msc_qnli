pilgrimage_participants_premise = 70e6
pilgrimage_participants_hypothesis = 70e6

# the hypothesis talks about the number of people participating in pilgrimage to the Ganges river
# the premise also mentions the same number of people participating in the pilgrimage
if pilgrimage_participants_hypothesis!= pilgrimage_participants_premise:
    # check if the number of participants in the hypothesis contradicts the number of participants from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
