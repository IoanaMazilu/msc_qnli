# Premise: In a BCCI meeting there are 13 people.
# Hypothesis: In a BCCI meeting there are less than 63 people.
# Golden Label: entailment

people_premise = 13
people_hypothesis = 63

# the hypothesis refers to the number of people in a BCCI meeting mentioned in the premise
if people_premise >= people_hypothesis:
    # check if the number of people in the premise contradicts the estimate of 'less than people_hypothesis'
    label = "contradiction"
else:
    # if the premise number of people does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

