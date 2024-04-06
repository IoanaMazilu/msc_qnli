# Premise: Twelve people were injured in the incident in the Dutch town of Apeldoorn, about 45 miles east of Amsterdam, police spokeswoman Esther Naber told CNN.
# Hypothesis: Five people killed and five badly injured in incident in Dutch town of Apeldoorn.
# Golden Label: neutral

injured_people_premise = 12
killed_people_hypothesis = 5
injured_people_hypothesis = 5

# the hypothesis mentions the number of killed and injured people in the incident, which is also referenced in the premise
# however, the number of killed and injured people in the hypothesis is different from the number of injured people in the premise
if (killed_people_hypothesis > 0) or (injured_people_hypothesis != injured_people_premise):
    # check if the number of killed people in the hypothesis contradicts the number of injured people in the premise
    # also check if the number of injured people in the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "neutral"

print(label)

