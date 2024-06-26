pat_stretch_premise = 10
pat_stretch_hypothesis = 60

# the hypothesis refers to the time Pat stops to stretch, mentioned in the premise
if pat_stretch_premise <= pat_stretch_hypothesis:
    # check if the hypothesis value contradicts the time estimate in the premise
    label = "contradiction"
elif pat_stretch_hypothesis!= pat_stretch_premise:
    # check if the time estimate in the hypothesis contradicts the time estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
