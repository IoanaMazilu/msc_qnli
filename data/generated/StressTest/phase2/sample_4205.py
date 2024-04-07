# Premise: Mira is making telescopes, each consisting of 2 lenses, 1 tube, and 1 eyepiece.
# Hypothesis: Mira is making telescopes, each consisting of 6 lenses, 1 tube, and 1 eyepiece.
# Golden Label: contradiction

lenses_premise = 2
lenses_hypothesis = 6
tube_premise = 1
tube_hypothesis = 1
eyepiece_premise = 1
eyepiece_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes, and eyepieces per telescope mentioned in the premise
if lenses_premise != lenses_hypothesis:
    # check if the number of lenses in the hypothesis contradicts the number of lenses reported in the premise
    label = "contradiction"
elif tube_premise != tube_hypothesis or eyepiece_premise != eyepiece_hypothesis:
    # check if the number of tubes or eyepieces in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if all the values in the hypothesis match the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

