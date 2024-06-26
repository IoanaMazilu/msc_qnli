y = 8800

distance_raised_premise = 1800 / 5 = 360
distance_raised_hypothesis = 8800 / 5 = 1760

distance_raised_premise_contradiction = 1800 / 5 = 360
distance_raised_hypothesis_contradiction = 8800 / 5 = 1760

distance_raised_neutral = 1800 / 5 = 360
distance_raised_hypothesis_neutral = 8800 / 5 = 1760

if distance_raised_premise_contradiction!= distance_raised_hypothesis_contradiction:
    # check if the distance raised in the hypothesis contradicts the distance raised in the premise
    label = "contradiction"
elif distance_raised_premise_contradiction!= distance_raised_neutral:
    # check if the distance raised in the hypothesis contradicts the distance raised in the premise
    label = "contradiction"
else:
    # if the distances in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)
