# Premise: Jacob's age less than 28 years hence will be thrice his age four years ago.
# Hypothesis: Jacob's age 18 years hence will be thrice his age four years ago.
# Golden Label: neutral

age_future_premise = 28
age_future_hypothesis = 18
age_past = 4

# the hypothesis refers to Jacob's future and past ages mentioned in the premise
if age_future_hypothesis != age_future_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
elif (age_future_premise - age_past*3) != 0 or (age_future_hypothesis - age_past*3) != 0:
    # check if the relation between the future and past ages in the premise and hypothesis hold
    label = "contradiction"
else:
    # if the hypothesis values and relations do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

