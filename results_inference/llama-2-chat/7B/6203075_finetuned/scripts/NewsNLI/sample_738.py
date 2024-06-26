distance_east_northeast_premise = 156
distance_west_premise = 164
distance_east_northeast_hypothesis = 156
distance_west_hypothesis = 164
depth_strike_hypothesis = 35

# the hypothesis mentions the distance to the east-northeast and west of Bitung and Tobelo, respectively, which are also mentioned in the premise
if distance_east_northeast_hypothesis!= distance_east_northeast_premise or distance_west_hypothesis!= distance_west_premise:
    # check if the distances in the hypothesis contradict the distances in the premise
    label = "contradiction"
elif depth_strike_hypothesis!= 35:
    # check if the depth of the strike in the hypothesis contradicts the depth of the strike in the premise
    label = "contradiction"
else:
    # if the distances and depth of the strike in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
