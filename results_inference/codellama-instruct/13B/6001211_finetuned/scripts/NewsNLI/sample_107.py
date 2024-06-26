arrested_premise = 5
arrested_hypothesis = 5
police_officers_hurt_premise = 21
demonstrator_hurt_premise = 1
police_officers_hurt_hypothesis = 21
demonstrator_hurt_hypothesis = 1

# the hypothesis mentions the number of people arrested and the number of police officers and demonstrators hurt, which are also mentioned in the premise
if arrested_hypothesis!= arrested_premise:
    # check if the number of people arrested in the hypothesis contradicts the number of people arrested in the premise
    label = "contradiction"
elif police_officers_hurt_hypothesis!= police_officers_hurt_premise or demonstrator_hurt_hypothesis!= demonstrator_hurt_premise:
    # check if the number of police officers or demonstrators hurt in the hypothesis contradicts the number of police officers or demonstrators hurt in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
