# Premise: One day, Raviraj left home and cycled 20 Km southwards, turned right and cycled 10 km and turned right and cycled 20 Km and turned left and cycled 20 Km.
# Hypothesis: One day, Raviraj left home and cycled less than 60 Km southwards, turned right and cycled 10 km and turned right and cycled 20 Km and turned left and cycled 20 Km.
# Golden Label: entailment

total_distance_premise = 20 + 10 + 20 + 20
south_distance_premise = 20
total_distance_hypothesis = 60
south_distance_hypothesis = 60

# the hypothesis talks about the total distance and the south distance Raviraj cycled in one day
if total_distance_hypothesis != total_distance_premise:
    # check to see if the total distance in the hypothesis contradicts the total distance in the premise
    label = "contradiction"
elif south_distance_hypothesis <= south_distance_premise:
    # check if the south distance in the hypothesis contradicts the south distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
