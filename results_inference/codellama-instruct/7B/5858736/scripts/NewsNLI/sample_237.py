injured_premise = 50
injured_hypothesis = 50

# the hypothesis mentions the number of people injured, which is also mentioned in the premise
if injured_hypothesis!= injured_premise:
    # check if the number of people injured from the hypothesis contradicts the number of people injured in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
