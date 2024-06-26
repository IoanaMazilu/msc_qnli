lenses_premise = 2
lenses_hypothesis = 8
tubes_premise = 1
tubes_hypothesis = 1
eyepieces_premise = 1
eyepieces_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes, and eyepieces in a telescope
if lenses_hypothesis == lenses_premise:
    # check if the number of lenses in the hypothesis contradicts the number of lenses in the premise
    label = "contradiction"
elif tubes_hypothesis!= tubes_premise or eyepieces_hypothesis!= eyepieces_premise:
    # check if the number of tubes or eyepieces in the hypothesis contradicts the number of tubes or eyepieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
