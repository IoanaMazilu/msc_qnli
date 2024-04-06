# Premise: There were'' four separate homicide scenes within the residence'' -- suggesting people had been killed in four different locales -- Police Chief Greg Suhr said.
# Hypothesis: There were 4 separate homicide scenes in the single residence, the city's police chief says.
# Golden Label: neutral

homicide_scenes_premise = 4
homicide_scenes_hypothesis = 4

# the hypothesis mentions the number of homicide scenes in the residence, which is also mentioned in the premise
if homicide_scenes_hypothesis != homicide_scenes_premise:
    # check if the number of homicide scenes in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of homicide scenes in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

