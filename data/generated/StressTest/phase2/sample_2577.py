# Premise: Carlos is 8 years old.
# Hypothesis: Carlos is more than 1 years old.
# Golden Label: entailment

carlos_age_premise = 8
carlos_age_hypothesis = 1

# the hypothesis talks about the age of Carlos, referenced also in the premise
if carlos_age_premise <= carlos_age_hypothesis:
    # check if Carlos's age in the premise contradicts the hypothesis that Carlos is older than 'carlos_age_hypothesis'
    label = "contradiction"
else:
    # if Carlos's age in the premise does not contradict the hypothesis that Carlos is older than 'carlos_age_hypothesis', we can infer entailment
    label = "entailment"

print(label)

