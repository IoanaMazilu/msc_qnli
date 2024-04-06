# Premise: The victims were taken to WellStar Kennestone Hospital, where an emergency room doctor involved in the response said three were in critical condition.
# Hypothesis: Six people are taken to Wellstar Kennestone Hospital.
# Golden Label: neutral

victims_premise = 3
victims_hypothesis = 6

# the hypothesis mentions the number of people taken to the hospital, which is also referenced in the premise
if victims_hypothesis > victims_premise:
    # check if the number of victims in the hypothesis contradicts the number of victims reported in the premise
    label = "contradiction"
else:
    # if the number of victims in the hypothesis does not contradict the number of victims in the premise, we can infer entailment
    label = "entailment"

print(label)

