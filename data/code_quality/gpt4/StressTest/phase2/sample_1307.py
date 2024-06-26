ratio_pens_pencils_markers_premise = (2, 2, 5)
ratio_pens_pencils_markers_hypothesis = (3, 2, 5)

# the hypothesis talks about the ratio of pens, pencils, and markers in Jenna's desk, which is also mentioned in the premise
if ratio_pens_pencils_markers_hypothesis != ratio_pens_pencils_markers_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis give exactly the same ratios
    label = "entailment"

print(label)
