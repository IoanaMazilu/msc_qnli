# Premise: But al-Beeraqdar said, without naming names, that two contractors were being held on charges involving'' illegal substances'' found on the men when they were taken into custody.
# Hypothesis: Two others remain in custody on charges involving'' illegal substances''
# Golden Label: neutral

contractors_in_custody_premise = 2
contractors_in_custody_hypothesis = 2

# the hypothesis mentions the number of contractors in custody, which is also mentioned in the premise
if contractors_in_custody_hypothesis != contractors_in_custody_premise:
    # check if the number of contractors in custody from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of contractors in custody from the hypothesis does not contradict the number from the premise, we can infer entailment
    label = "entailment"

print(label)

