# Premise: If Cara is 110 km away from Dan at 7 am, and also 110 km away from Dan at 11 am, then how fast is Dan driving (in kilometers per hour)?
# Hypothesis: If Cara is less than 110 km away from Dan at 7 am, and also 110 km away from Dan at 11 am, then how fast is Dan driving (in kilometers per hour)?
# Golden Label: contradiction

distance_premise_7am = 110
distance_hypothesis_7am = 110
distance_premise_11am = 110
distance_hypothesis_11am = 110

# the hypothesis refers to the distances between Cara and Dan at 7 am and at 11 am
if distance_hypothesis_7am >= distance_premise_7am:
    # check if the hypothesis distance at 7 am contradicts the premise
    label = "contradiction"
elif distance_hypothesis_11am != distance_premise_11am:
    # check if the hypothesis distance at 11 am contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis distances do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

