kilometers_premise = 40.0
kilometers_per_hour_premise = 8.0
hours_hypothesis = 5.0

# calculate the total distance traveled in the premise
total_distance_premise = kilometers_premise * hours_premise

# compare the total distance in the hypothesis to the total distance in the premise
if total_distance_hypothesis!= total_distance_premise:
    # if the total distance in the hypothesis contradicts the total distance in the premise
    label = "contradiction"
else:
    # if the total distance in the hypothesis is equal to or less than the total distance in the premise
    # we can infer entailment
    label = "entailment"

print(label)
