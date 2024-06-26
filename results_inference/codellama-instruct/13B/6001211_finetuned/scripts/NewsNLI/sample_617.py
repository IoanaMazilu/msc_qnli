manchester_city_points_premise = 1
manchester_united_points_hypothesis = 1
norwich_score_premise = 1
norwich_score_hypothesis = 1

# the hypothesis mentions the points of Manchester United and the score of the Norwich City game, which are also mentioned in the premise
if manchester_united_points_hypothesis!= manchester_city_points_premise:
    # check if the points of Manchester United in the hypothesis contradicts the points of Manchester City reported in the premise
    label = "contradiction"
elif norwich_score_hypothesis!= norwich_score_premise:
    # check if the score of the Norwich City game from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
