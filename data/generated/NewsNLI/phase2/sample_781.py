# Premise: In addition to ordering 20 people released, the Supreme Court called for the review of cases involving six others who were convicted in the massacre.
# Hypothesis: Mexican high court orders release of 20 convicted in 1997 killings of 45 people.
# Golden Label: neutral

people_released_premise = 20
people_released_hypothesis = 20

# the hypothesis mentions the number of people ordered to be released by the high court, which is also referenced in the premise
if people_released_hypothesis != people_released_premise:
    # check if the number of people to be released in the hypothesis contradicts the number of people to be released in the premise
    label = "contradiction"
else:
    # if the number of people to be released does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

