# Premise: His wife Maggie can wash all the windows in 6 hours.
# Hypothesis: His wife Maggie can wash all the windows in 2 hours.
# Golden Label: contradiction

windows_washing_time_premise = 6
windows_washing_time_hypothesis = 2

# the hypothesis refers to the time Maggie needs to wash all the windows, also mentioned in the premise
if windows_washing_time_hypothesis != windows_washing_time_premise:
    # check if the time needed for Maggie to wash the windows in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

