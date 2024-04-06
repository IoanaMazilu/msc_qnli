# Premise: Furyk took full advantage to record six birdies in his first round, a bogey on the final hole not dampening his enthusiasm.
# Hypothesis: A double bogey on the final hole leaves one over.
# Golden Label: neutral

bogey_premise = 1
bogey_hypothesis = 2

# the hypothesis mentions a double bogey on the final hole, which contradicts the premise that mentions only one bogey
if bogey_hypothesis != bogey_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)

