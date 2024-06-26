participants_premise = 70e6
participants_hypothesis = 70e6

# the hypothesis talks about the number of participants in the pilgrimage, which is also mentioned in the premise
if participants_hypothesis!= participants_premise:
    # check if the number of participants in the hypothesis contradicts the number of participants from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
