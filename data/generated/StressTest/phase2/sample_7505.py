# Premise: After 10 minutes, Pat stops to stretch.
# Hypothesis: After 60 minutes, Pat stops to stretch.
# Golden Label: contradiction

stretch_time_premise = 10
stretch_time_hypothesis = 60

# the hypothesis refers to the time when Pat stops to stretch, mentioned also in the premise
if stretch_time_hypothesis == stretch_time_premise:
    # check if the time in the hypothesis matches the time when Pat stops to stretch as mentioned in the premise
    label = "entailment"
elif stretch_time_hypothesis < stretch_time_premise:
    # check if the time in the hypothesis contradicts the time when Pat stops to stretch as mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific time when Pat stops to stretch
    # any time greater than 'stretch_time_premise' is inconsistent with the premise
    label = "contradiction"

print(label)

