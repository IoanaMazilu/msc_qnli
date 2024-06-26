people_arrested_premise = 5
people_arrested_hypothesis = 5
officers_hurt_premise = 21
officers_hurt_hypothesis = 21
demonstrator_hurt_premise = 1
demonstrator_hurt_hypothesis = 1

# the hypothesis mentions the number of people arrested, the number of police officers and the demonstrator who were hurt, which are also mentioned in the premise
if people_arrested_hypothesis!= people_arrested_premise:
    # check if the number of people arrested in the hypothesis contradicts the number of people arrested in the premise
    label = "contradiction"
elif officers_hurt_hypothesis!= officers_hurt_premise:
    # check if the number of police officers who were hurt in the hypothesis contradicts the number of police officers who were hurt in the premise
    label = "contradiction"
elif demonstrator_hurt_hypothesis!= demonstrator_hurt_premise:
    # check if the number of demonstrators who were hurt in the hypothesis contradicts the number of demonstrators who were hurt in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
