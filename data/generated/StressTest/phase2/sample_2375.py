# Premise: In a BCCI meeting there are 12 people.
# Hypothesis: In a BCCI meeting there are 42 people.
# Golden Label: contradiction

people_premise = 12
people_hypothesis = 42

# the hypothesis talks about the number of people in the BCCI meeting, referenced also in the premise
if people_hypothesis != people_premise:
    # check if the hypothesis value contradicts the exact number of 'people_premise'
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"

print(label)

