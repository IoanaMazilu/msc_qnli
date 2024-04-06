# Premise: The survey said 57% supported it going forward and 28% opposing.
# Hypothesis: New CNN/ORC survey shows 57% of Americans support the pipeline going forward.
# Golden Label: neutral

support_premise = 0.57
support_hypothesis = 0.57
oppose_premise = 0.28

# the hypothesis mentions the support percentage from the survey, which is also referenced in the premise
# however, the hypothesis does not mention anything about the opposition percentage which is present in the premise
if support_hypothesis != support_premise:
    # check if the support percentage in the hypothesis contradicts the support percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)

