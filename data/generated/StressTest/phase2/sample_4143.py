# Premise: Mira is making telescopes, each consisting of 2 lenses, 1 tube, and 1 eyepiece.
# Hypothesis: Mira is making telescopes, each consisting of less than 6 lenses, 1 tube, and 1 eyepiece.
# Golden Label: entailment

lenses_per_telescope_premise = 2
lenses_per_telescope_hypothesis = 6
tube_per_telescope_premise = 1
tube_per_telescope_hypothesis = 1
eyepiece_per_telescope_premise = 1
eyepiece_per_telescope_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes and eyepieces used in making telescopes as mentioned in the premise
if lenses_per_telescope_hypothesis <= lenses_per_telescope_premise:
    # check if the estimate of 'lenses_per_telescope_hypothesis' contradicts the number of lenses used in the premise
    label = "contradiction"
elif tube_per_telescope_premise != tube_per_telescope_hypothesis or eyepiece_per_telescope_premise != eyepiece_per_telescope_hypothesis:
    # check if the number of tubes or eyepieces in the hypothesis contradicts the number of tubes or eyepieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

