switzerland_points_premise = 3
ecuador_points_premise = 3
ecuador_points_hypothesis = 3
honduras_score_premise = 1
honduras_score_hypothesis = 1

# the hypothesis mentions the score of the match between Ecuador and Honduras, which is also mentioned in the premise
# it also mentions the points of Ecuador, which is also mentioned in the premise
# however, the hypothesis refers to the place of the match, which cannot be entailed from the premise
if ecuador_points_hypothesis!= ecuador_points_premise:
    # check if the points of Ecuador in the hypothesis contradicts the points of Ecuador in the premise
    label = "contradiction"
elif honduras_score_hypothesis!= honduras_score_premise:
    # check if the score of the match in the hypothesis contradicts the score of the match in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
