# Premise: Connie has 64.0 red and blue markers and 41.0 of the markers are red.
# Hypothesis: 23.0 markers are blue.
# Golden Label: entailment

total_markers_premise = 64.0
red_markers_premise = 41.0
blue_markers_hypothesis = 23.0

# the hypothesis refers to the number of blue markers, which can be inferred from the premise
# compute the number of blue markers in the premise
blue_markers_premise = total_markers_premise - red_markers_premise
if blue_markers_hypothesis != blue_markers_premise:
    # check if the number of blue markers in the hypothesis contradicts the number of blue markers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

