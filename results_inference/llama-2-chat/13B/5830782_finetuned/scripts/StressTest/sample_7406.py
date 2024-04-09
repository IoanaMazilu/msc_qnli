lenses_premise = 2
lenses_hypothesis = 8
tubes_premise = 1
tubes_hypothesis = 1
eyepieces_premise = 1
eyepieces_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes, and eyepieces used in making telescopes, as mentioned in the premise
if lenses_premise!= lenses_hypothesis:
    # check if the number of lenses in the hypothesis contradicts the number of lenses reported in the premise
    label = "contradiction"
elif tubes_premise!= tubes_hypothesis or eyepieces_premise!= eyepieces_hypothesis:
    # check if the number of tubes or eyepieces in the hypothesis contradicts the number of tubes or eyepieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
