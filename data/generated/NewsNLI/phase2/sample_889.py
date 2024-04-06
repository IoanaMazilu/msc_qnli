# Premise: The department was evacuating two neighborhoods next to flooded creeks near downtown, he said.
# Hypothesis: Massive flooding prompts the evacuation of two neighborhoods near downtown.
# Golden Label: neutral

neighborhoods_premise = 2
neighborhoods_hypothesis = 2

# the hypothesis mentions the number of neighborhoods being evacuated, which is also mentioned in the premise
if neighborhoods_hypothesis != neighborhoods_premise:
    # check if the number of neighborhoods in the hypothesis contradicts the number of neighborhoods mentioned in the premise
    label = "contradiction"
else:
    # if the number of neighborhoods in the hypothesis does not contradict the number of neighborhoods in the premise, we can infer entailment
    label = "entailment"

print(label)

