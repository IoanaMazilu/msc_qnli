arrested_premise = 5
arrested_hypothesis = 5
police_officers_hurt_premise = 21
police_officers_hurt_hypothesis = 21
protester_hurt_premise = 1
protester_hurt_hypothesis = 1

# the hypothesis mentions the number of people arrested and the number of police officers and one protester hurt, which are also mentioned in the premise
if arrested_hypothesis!= arrested_premise:
    # check if the number of people arrested in the hypothesis contradicts the number of people arrested in the premise
    label = "contradiction"
elif police_officers_hurt_hypothesis!= police_officers_hurt_premise:
    # check if the number of police officers hurt in the hypothesis contradicts the number of police officers hurt in the premise
    label = "contradiction"
elif protester_hurt_hypothesis!= protester_hurt_premise:
    # check if the number of protesters hurt in the hypothesis contradicts the number of protesters hurt in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
