distance_rakesh_air_premise = 8800
distance_rakesh_air_hypothesis = 1800
total_journey_premise = 3/5 * distance_rakesh_air_premise
total_journey_hypothesis = 3/5 * distance_rakesh_air_hypothesis

# the hypothesis talks about the distance Rakesh travelled by air, which is also mentioned in the premise
if distance_rakesh_air_hypothesis!= distance_rakesh_air_premise:
    # check if the distance Rakesh travelled by air in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif total_journey_hypothesis!= total_journey_premise:
    # check if the total journey in the hypothesis contradicts the total journey in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
