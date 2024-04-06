# Premise: Three people were taken to hospitals, but officials could not immediately say why.
# Hypothesis: Three residents taken to hospital ; extent of injuries not known.
# Golden Label: entailment

people_premise = 3
people_hypothesis = 3

# the hypothesis mentions the number of people taken to hospital, which is also referenced in the premise
# however, the hypothesis refers to these people as 'residents', which cannot be entailed from the premise
if people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis does not contradict the number of people in the premise, it could be entailment or neutral
    # but as the status of these people (whether they are residents or not) cannot be entailed from the premise, it is neutral
    label = "neutral"

print(label)

