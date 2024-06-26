injured_people_premise = 50
injured_people_hypothesis = 50

# the hypothesis mentions the number of injured people, which is also mentioned in the premise
if injured_people_hypothesis!= injured_people_premise:
    # check if the number of injured people in the hypothesis contradicts the number of injured people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
