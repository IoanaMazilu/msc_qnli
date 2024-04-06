# Premise: Peter Siebold, 43, was identified as the pilot who survived the crash.
# Hypothesis: Pilot who survived identified as Peter Siebold, 43, Sheriff's Office says.
# Golden Label: neutral

age_premise = 43
age_hypothesis = 43

# the hypothesis mentions the age of the pilot who survived the crash, which is also mentioned in the premise
if age_hypothesis != age_premise:
    # check if the age from the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age from the hypothesis does not contradict the age in the premise, we can infer entailment
    label = "entailment"

print(label)

