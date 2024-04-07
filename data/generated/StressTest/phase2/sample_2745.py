# Premise: In a BCCI meeting there are 15 people.
# Hypothesis: In a BCCI meeting there are less than 55 people.
# Golden Label: entailment

people_premise = 15
people_hypothesis = 55

# the hypothesis discusses the number of people in a BCCI meeting, which is also mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the number of 'people_premise'
    label = "contradiction"
elif people_premise >= people_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'people_hypothesis'
    label = "contradiction"
else:
    # the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

