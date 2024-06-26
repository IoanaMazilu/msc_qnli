defeat_score_premise = 3
win_score_premise = 1
defeat_count_premise = 3
matches_count_premise = 5

defeat_score_hypothesis = 3
win_score_hypothesis = 1
defeat_count_hypothesis = 2

# the hypothesis mentions the 3-1 defeat at West Ham, which is also mentioned in the premise
# the hypothesis also mentions the number of consecutive defeats, which is referenced in the premise
if defeat_score_hypothesis != defeat_score_premise or win_score_hypothesis != win_score_premise:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
elif defeat_count_hypothesis >= defeat_count_premise:
    # check if the number of defeats in the hypothesis contradicts the number of defeats in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
