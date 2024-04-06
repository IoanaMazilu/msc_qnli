# Premise: The blaze has ignited 14,000 acres in the area, fire officials said.
# Hypothesis: Fire ignites 14,000 acres, fire officials say.
# Golden Label: entailment

acres_burned_premise = 14000
acres_burned_hypothesis = 14000

# the hypothesis mentions the number of acres ignited by the fire, which is also stated in the premise
if acres_burned_hypothesis != acres_burned_premise:
    # check if the number of acres burned in the hypothesis contradicts the number of acres burned reported in the premise
    label = "contradiction"
else:
    # if the value in the hypothesis does not contradict the value in the premise, we can infer entailment
    label = "entailment"

print(label)

