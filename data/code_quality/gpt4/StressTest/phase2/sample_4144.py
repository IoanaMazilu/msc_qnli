lenses_premise = 6
lenses_hypothesis = 2

tube_premise = 1
tube_hypothesis = 1

eyepiece_premise = 1
eyepiece_hypothesis = 1

# the hypothesis refers to the number of each component of a telescope made by Mira, mentioned in the premise
if lenses_hypothesis >= lenses_premise:
    # check if the number of lenses in the hypothesis contradicts the estimate of less than 'lenses_premise'
    label = "contradiction"
elif tube_hypothesis != tube_premise or eyepiece_hypothesis != eyepiece_premise:
    # check if the number of tubes or eyepieces in the hypothesis contradicts the number of tubes or eyepieces reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise and can be explicitly inferred from the premise
    label = "entailment"

print(label)
