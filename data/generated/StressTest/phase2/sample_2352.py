# Premise: 205 total Tajima's are currently owned by the dealership.
# Hypothesis: less than 305 total Tajima's are currently owned by the dealership.
# Golden Label: entailment

tajimas_owned_premise = 205
tajimas_owned_hypothesis = 305

# the hypothesis refers to the number of Tajima's owned by the dealership, mentioned also in the premise
if tajimas_owned_premise >= tajimas_owned_hypothesis:
    # check if the number of Tajima's owned in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

