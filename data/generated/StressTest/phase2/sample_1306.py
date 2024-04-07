# Premise: Pens, Pencils and Markers in a Jenna's desk are in the ratio of less than 7:2:5.
# Hypothesis: Pens, Pencils and Markers in a Jenna's desk are in the ratio of 2:2:5.
# Golden Label: neutral

pens_premise = 7
pencils_premise = 2
markers_premise = 5

pens_hypothesis = 2
pencils_hypothesis = 2
markers_hypothesis = 5

# the hypothesis refers to the same ratio of pens, pencils and markers mentioned in the premise
if pens_hypothesis >= pens_premise:
    # check if the 'pens_hypothesis' contradicts the estimate of less than 'pens_premise' pens
    label = "contradiction"
elif pencils_hypothesis != pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils in the premise
    label = "contradiction"
elif markers_hypothesis != markers_premise:
    # check if the number of markers in the hypothesis contradicts the number of markers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

