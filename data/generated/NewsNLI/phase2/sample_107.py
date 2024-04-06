# Premise: Twenty-one police officers and one demonstrator were hurt, and at least five people have been arrested, police said.
# Hypothesis: At least five arrested ; 21 police officers and one protester hurt in the clashes, police say.
# Golden Label: entailment

police_officers_hurt_premise = 21
demonstrator_hurt_premise = 1
people_arrested_premise = 5

police_officers_hurt_hypothesis = 21
demonstrator_hurt_hypothesis = 1
people_arrested_hypothesis = 5

# the hypothesis mentions the number of police officers and demonstrators hurt, and the number of people arrested, which are also mentioned in the premise
if police_officers_hurt_hypothesis != police_officers_hurt_premise:
    # check if the number of police officers hurt in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif demonstrator_hurt_hypothesis != demonstrator_hurt_premise:
    # check if the number of demonstrators hurt from the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif people_arrested_hypothesis != people_arrested_premise:
    # check if the number of people arrested from the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

