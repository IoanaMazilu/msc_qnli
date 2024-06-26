distance_premise = 130
distance_hypothesis = 530

# the hypothesis refers to the same distance mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the claimed 'distance_hypothesis' contradicts the actual distance in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # check if the claimed 'distance_hypothesis' is equal to the actual distance in the premise
    label = "entailment"
else:
    # the premise states the exact distance, any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
