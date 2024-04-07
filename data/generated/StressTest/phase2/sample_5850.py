# Premise: In a BCCI meeting there are 14 people.
# Hypothesis: In a BCCI meeting there are less than 54 people.
# Golden Label: entailment

people_premise = 14
people_hypothesis = 54

# the hypothesis talks about the number of people in a BCCI meeting, referenced also in the premise
if people_premise >= people_hypothesis:
    # check if the number of people in the premise contradicts the estimate of less than 'people_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

