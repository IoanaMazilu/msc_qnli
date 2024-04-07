# Premise: After 30 minutes, Jim stops to stretch.
# Hypothesis: After 80 minutes, Jim stops to stretch.
# Golden Label: contradiction

stretch_time_premise = 30
stretch_time_hypothesis = 80

# the hypothesis talks about the time when Jim stops to stretch, which is also mentioned in the premise
if stretch_time_hypothesis != stretch_time_premise:
    # check if the time when Jim stops to stretch in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if both times are identical, the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

