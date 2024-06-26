lenses_premise = 2
lenses_hypothesis = 7
tube_premise = 1
tube_hypothesis = 1
eyepiece_premise = 1
eyepiece_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes, and eyepieces in a telescope, mentioned in the premise
if lenses_premise >= lenses_hypothesis:
    # check if the number of lenses in the premise contradicts the estimate of less than 'lenses_hypothesis'
    label = "contradiction"
elif tube_premise!= tube_hypothesis or eyepiece_premise!= eyepiece_hypothesis:
    # check if the number of tubes or eyepieces in the hypothesis contradicts the number of tubes or eyepieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
