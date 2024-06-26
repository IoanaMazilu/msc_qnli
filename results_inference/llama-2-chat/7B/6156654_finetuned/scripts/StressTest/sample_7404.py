lenses_premise = 2
lenses_hypothesis = 7
tube_premise = 1
tube_hypothesis = 1
eyepiece_premise = 1
eyepiece_hypothesis = 1

# the hypothesis refers to the number of lenses, tube, and eyepiece in each telescope
if lenses_premise >= lenses_hypothesis:
    # check if the number of lenses in the premise contradicts the number of lenses in the hypothesis
    label = "contradiction"
elif tube_premise!= tube_hypothesis or eyepiece_premise!= eyepiece_hypothesis:
    # check if the number of tube or eyepiece in the premise contradicts the number of tube or eyepiece in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and the premise values do not contradict, we can infer entailment
    label = "entailment"

print(label)
