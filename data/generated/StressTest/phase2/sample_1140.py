# Premise: Meera is making telescopes, each consisting of 2 lenses, 1 tube, and 1 eyepiece.
# Hypothesis: Meera is making telescopes, each consisting of less than 5 lenses, 1 tube, and 1 eyepiece.
# Golden Label: entailment

lenses_per_telescope_premise = 2
lenses_per_telescope_hypothesis = 5
tubes_per_telescope_premise = 1
tubes_per_telescope_hypothesis = 1
eyepieces_per_telescope_premise = 1
eyepieces_per_telescope_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes, and eyepieces per telescope mentioned in the premise
if lenses_per_telescope_premise >= lenses_per_telescope_hypothesis:
    # check if the estimate of 'lenses_per_telescope_hypothesis' contradicts the number of lenses per telescope in the premise
    label = "contradiction"
elif tubes_per_telescope_premise != tubes_per_telescope_hypothesis:
    # check if the number of tubes per telescope in the hypothesis contradicts the number of tubes per telescope reported in the premise
    label = "contradiction"
elif eyepieces_per_telescope_premise != eyepieces_per_telescope_hypothesis:
    # check if the number of eyepieces per telescope in the hypothesis contradicts the number of eyepieces per telescope reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

