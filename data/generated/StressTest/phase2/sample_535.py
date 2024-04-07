# Premise: Ramesh is less than 6:1 while that between Mr.
# Hypothesis: Ramesh is 2:1 while that between Mr.
# Golden Label: neutral

ramesh_ratio_premise = 6
ramesh_ratio_hypothesis = 2

# the hypothesis talks about the Ramesh's ratio mentioned in the premise
if ramesh_ratio_hypothesis > ramesh_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ramesh_ratio_premise'
    label = "contradiction"
elif ramesh_ratio_hypothesis == ramesh_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ramesh_ratio_premise'
    label = "contradiction"
else:
    # any ratio less than 'ramesh_ratio_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

