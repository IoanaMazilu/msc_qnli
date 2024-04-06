# Premise: Turnout was registered at just over 95 percent, it said.
# Hypothesis: Turnout was just over 95 percent, electoral commission says.
# Golden Label: neutral

turnout_premise = 0.95
turnout_hypothesis = 0.95

# the hypothesis mentions the turnout, which is also mentioned in the premise
if turnout_hypothesis != turnout_premise:
    # check if the turnout in the hypothesis contradicts the turnout reported in the premise
    label = "contradiction"
else:
    # if the hypothesis turnout does not contradict the premise turnout, we can infer entailment
    label = "entailment"

print(label)

