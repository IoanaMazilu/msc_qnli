# Premise: Mira is making telescopes, each consisting of 2 lenses, 1 tube, and 1 eyepiece.
# Hypothesis: Mira is making telescopes, each consisting of less than 7 lenses, 1 tube, and 1 eyepiece.
# Golden Label: entailment

lenses_premise = 2
lenses_hypothesis = 7
tube_premise = 1
tube_hypothesis = 1
eyepiece_premise = 1
eyepiece_hypothesis = 1

# the hypothesis refers to the number of lenses, tubes, and eyepieces per telescope mentioned in the premise
if lenses_premise >= lenses_hypothesis:
    # check if the estimate of 'lenses_hypothesis' contradicts the number of lenses per telescope in the premise
    label = "contradiction"
elif tube_premise != tube_hypothesis or eyepiece_premise != eyepiece_hypothesis:
    # check if the number of tubes or eyepieces per telescope in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

