# Premise: One hour after Matthew started waking from e to y, a distance of 45 km, Johnny started walking along the same road from y to e.
# Hypothesis: One hour after Matthew started waking from e to y, a distance of less than 45 km, Johnny started walking along the same road from y to e.
# Golden Label: contradiction

distance_walked_premise = 45
distance_walked_hypothesis = 45

# the hypothesis talks about the distance Matthew walked, also mentioned in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if the hypothesis value contradicts the premise of less than 'distance_walked_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

