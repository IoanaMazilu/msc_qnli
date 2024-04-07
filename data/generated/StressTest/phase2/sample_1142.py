# Premise: Meera is making telescopes, each consisting of 2 lenses, 1 tube, and 1 eyepiece.
# Hypothesis: Meera is making telescopes, each consisting of 5 lenses, 1 tube, and 1 eyepiece.
# Golden Label: contradiction

lenses_premise = 2
lenses_hypothesis = 5
tubes_premise = 1
tubes_hypothesis = 1
eyepiece_premise = 1
eyepiece_hypothesis = 1

# the hypothesis talks about the number of lenses, tubes, and eyepieces in a telescope, referenced also in the premise
if lenses_hypothesis != lenses_premise:
    # check if the number of lenses in the hypothesis contradicts the number of lenses reported in the premise
    label = "contradiction"
elif tubes_hypothesis != tubes_premise:
    # check if the number of tubes in the hypothesis contradicts the number of tubes reported in the premise
    label = "contradiction"
elif eyepiece_hypothesis != eyepiece_premise:
    # check if the number of eyepieces in the hypothesis contradicts the number of eyepieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

