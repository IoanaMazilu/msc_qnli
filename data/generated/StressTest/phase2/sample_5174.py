# Premise: After 12 minutes, Cathy stops to stretch.
# Hypothesis: After less than 12 minutes, Cathy stops to stretch.
# Golden Label: contradiction

stretch_time_premise = 12
stretch_time_hypothesis = 12

# the hypothesis refers to the moment when Cathy stops to stretch, mentioned in the premise too
if stretch_time_hypothesis < stretch_time_premise:
    # check if the hypothesis value contradicts the exact time reported in the premise
    label = "contradiction"
elif stretch_time_hypothesis > stretch_time_premise:
    # check if the hypothesis value contradicts the exact time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

