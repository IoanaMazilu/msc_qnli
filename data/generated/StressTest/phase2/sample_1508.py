# Premise: After 18 minutes, Cathy stops to stretch.
# Hypothesis: After 88 minutes, Cathy stops to stretch.
# Golden Label: contradiction

stretch_time_premise = 18
stretch_time_hypothesis = 88

# The hypothesis refers to the time when Cathy stops to stretch, which is also mentioned in the premise
if stretch_time_hypothesis == stretch_time_premise:
    # Check if the hypothesis time contradicts the premise time
    label = "entailment"
elif stretch_time_hypothesis != stretch_time_premise:
    # Check if the hypothesis time contradicts the premise time
    label = "contradiction"

print(label)

