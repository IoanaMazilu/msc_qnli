injured_people_premise = 2
injured_people_hypothesis = 2

# the hypothesis mentions the number of injured people, which is also mentioned in the premise
if injured_people_hypothesis!= injured_people_premise:
    # check if the number of injured people in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of injured people in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
