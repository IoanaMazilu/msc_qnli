# Premise: Loud sirens sounded after the quake, which had an estimated depth of 40 miles, the USGS said.
# Hypothesis: The depth of the quake was 40 miles, the U.S. Geological Survey says.
# Golden Label: entailment

depth_premise = 40
depth_hypothesis = 40

# the hypothesis mentions the depth of the earthquake, which is also mentioned in the premise
if depth_hypothesis != depth_premise:
    # check if the depth in the hypothesis contradicts the depth reported in the premise
    label = "contradiction"
else:
    # if the depth in the hypothesis does not contradict the depth in the premise, we can infer entailment
    label = "entailment"

print(label)

