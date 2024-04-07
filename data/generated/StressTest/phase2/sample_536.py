# Premise: Ramesh is 2:1 while that between Mr.
# Hypothesis: Ramesh is 6:1 while that between Mr.
# Golden Label: contradiction

ramesh_premise = 2/1
ramesh_hypothesis = 6/1

# the hypothesis talks about Ramesh, who is also referenced in the premise
if ramesh_premise != ramesh_hypothesis:
    # check if the ratio of Ramesh in the hypothesis contradicts the ratio of Ramesh in the premise
    label = "contradiction"
else:
    # the premise gives the ratio of Ramesh
    # the hypothesis should match the ratio given in premise for entailment
    label = "entailment"

print(label)

