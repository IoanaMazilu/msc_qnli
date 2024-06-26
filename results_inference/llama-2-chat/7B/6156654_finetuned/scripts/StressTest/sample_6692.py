distance_rakesh_premise = 1800
distance_rakesh_hypothesis = 7800
total_journey_premise = distance_rakesh_premise / 3
total_journey_hypothesis = distance_rakesh_hypothesis / 3

# the hypothesis refers to the distance Rakesh travelled by air, which is also mentioned in the premise
if distance_rakesh_hypothesis!= distance_rakesh_premise:
    # check if the distance Rakesh travelled by air in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif total_journey_hypothesis!= total_journey_premise:
    # check if the total journey in the hypothesis contradicts the total journey in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
