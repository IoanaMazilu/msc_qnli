lenses_per_telescope_premise = 2
lenses_per_telescope_hypothesis = 8
tubes_per_telescope_premise = 1
tubes_per_telescope_hypothesis = 1
eyepieces_per_telescope_premise = 1
eyepieces_per_telescope_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes, and eyepieces per telescope mentioned in the premise
if lenses_per_telescope_hypothesis!= lenses_per_telescope_premise:
    # check if the number of lenses in the hypothesis contradicts the number of lenses per telescope reported in the premise
    label = "contradiction"
elif tubes_per_telescope_hypothesis!= tubes_per_telescope_premise:
    # check if the number of tubes in the hypothesis contradicts the number of tubes per telescope reported in the premise
    label = "contradiction"
elif eyepieces_per_telescope_hypothesis!= eyepieces_per_telescope_premise:
    # check if the number of eyepieces in the hypothesis contradicts the number of eyepieces per telescope reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
