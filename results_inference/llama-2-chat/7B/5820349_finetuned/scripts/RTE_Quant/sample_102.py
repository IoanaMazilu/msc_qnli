killed_premise = 4
killed_hypothesis = 4
injured_premise = 80
injured_hypothesis = 80

# the hypothesis talks about the number of killed and injured people, which are also mentioned in the premise
if killed_hypothesis!= killed_premise:
    # check if the number of killed people in the hypothesis contradicts the number of killed people from the premise
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # check if the number of injured people in the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
