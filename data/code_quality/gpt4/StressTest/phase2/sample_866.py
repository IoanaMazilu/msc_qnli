distance_delhi_mathura_premise = 110
distance_delhi_mathura_hypothesis = 110

# the hypothesis refers to the distance between Delhi and Mathura mentioned in the premise
if distance_delhi_mathura_hypothesis < distance_delhi_mathura_premise:
    # check if the hypothesis distance is less than the premise distance
    label = "contradiction"
elif distance_delhi_mathura_hypothesis > distance_delhi_mathura_premise:
    # check if the hypothesis distance is more than the premise distance
    label = "contradiction"
else:
    # If the hypothesis distance matches the premise distance, we can infer entailment
    label = "entailment"

print(label)
