# Premise: Pens, Pencils and Markers in a Jenna's desk are in the ratio of 2:2:5.
# Hypothesis: Pens, Pencils and Markers in a Jenna's desk are in the ratio of less than 7:2:5.
# Golden Label: entailment

pens_premise = 2
pencils_premise = 2
markers_premise = 5

pens_hypothesis = 7
pencils_hypothesis = 2
markers_hypothesis = 5

# the hypothesis talks about the ratio of pens, pencils, and markers in Jenna's desk, which is also mentioned in the premise
if pens_hypothesis <= pens_premise:
    # check if the ratio of pens in the hypothesis contradicts the ratio of pens in the premise
    label = "contradiction"
elif pencils_hypothesis != pencils_premise or markers_hypothesis != markers_premise:
    # check if the ratio of pencils or markers in the hypothesis contradicts the ratio of pencils or markers in the premise
    label = "contradiction"
else:
    # the premise gives an exact ratio for pens, pencils, and markers
    # any ratio of pens less than 'pens_premise' and equal ratios for pencils and markers is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

