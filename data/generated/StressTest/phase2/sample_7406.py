# Premise: Mira is making telescopes, each consisting of 2 lenses, 1 tube, and 1 eyepiece.
# Hypothesis: Mira is making telescopes, each consisting of 8 lenses, 1 tube, and 1 eyepiece.
# Golden Label: contradiction

lenses_premise = 2
lenses_hypothesis = 8
tubes_premise = 1
tubes_hypothesis = 1
eyepiece_premise = 1
eyepiece_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes and eyepieces mentioned in the premise
if lenses_premise != lenses_hypothesis:
    # check if the number of lenses in the hypothesis contradicts the number of lenses reported in the premise
    label = "contradiction"
elif tubes_premise != tubes_hypothesis:
    # check if the number of tubes in the hypothesis contradicts the number of tubes reported in the premise
    label = "contradiction"
elif eyepiece_premise != eyepiece_hypothesis:
    # check if the number of eyepieces in the hypothesis contradicts the number of eyepieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

