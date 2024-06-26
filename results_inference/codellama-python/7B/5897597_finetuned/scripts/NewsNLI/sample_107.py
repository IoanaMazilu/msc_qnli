police_officers_hurt_premise = 21
demonstrator_hurt_premise = 1
arrested_people_premise = 5
police_officers_hurt_hypothesis = 21
demonstrator_hurt_hypothesis = 1
arrested_people_hypothesis = 5

# the hypothesis mentions the number of police officers and demonstrators hurt and the number of people arrested, which are also mentioned in the premise
if police_officers_hurt_hypothesis!= police_officers_hurt_premise:
    # check if the number of police officers hurt in the hypothesis contradicts the number of police officers hurt in the premise
    label = "contradiction"
elif demonstrator_hurt_hypothesis!= demonstrator_hurt_premise:
    # check if the number of demonstrators hurt from the hypothesis contradicts the number of demonstrators hurt in the premise
    label = "contradiction"
elif arrested_people_hypothesis!= arrested_people_premise:
    # check if the number of people arrested from the hypothesis contradicts the number of people arrested in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
