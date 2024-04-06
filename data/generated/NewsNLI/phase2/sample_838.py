# Premise: '' We call on Iranian authorities to immediately explain why Jason Rezaian, Yeganeh Salehi, and two other journalists have been detained, and we call for their immediate release,'' said Sherif Mansour, its Middle East and North Africa program coordinator.
# Hypothesis: Iranian official says Jason Rezaian and Yeganeh Salehi are among three journalists held.
# Golden Label: neutral

journalists_premise = 4
journalists_hypothesis = 3

# the hypothesis mentions the number of journalists being held, which is also mentioned in the premise
# we need to check if the number of journalists in the hypothesis contradicts the number of journalists in the premise
if journalists_hypothesis != journalists_premise:
    label = "contradiction"
else:
    # if the number of journalists in the hypothesis does not contradict the number of journalists in the premise, we cannot infer entailment nor contradiction
    label = "neutral"

print(label)

