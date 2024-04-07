# Premise: In a BCCI meeting there are 11 people.
# Hypothesis: In a BCCI meeting there are less than 31 people.
# Golden Label: entailment

people_premise = 11
people_hypothesis = 31

# the hypothesis refers to the number of people in the BCCI meeting mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
elif people_premise > people_hypothesis:
    # check if the number of people in the premise contradicts the estimate of less than 'people_hypothesis'
    label = "contradiction"
else:
    # the hypothesis estimate does not contradict or explicitly entail the premise number of people
    label = "neutral"

print(label)

