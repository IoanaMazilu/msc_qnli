manchester_city_score_premise = 2
leicester_score_premise = 2
manchester_city_score_hypothesis = 2
leicester_score_hypothesis = 2

# the hypothesis mentions the score of the match between Manchester City and Leicester, which is also referenced in the premise
if manchester_city_score_hypothesis!= manchester_city_score_premise:
    # check if the score of Manchester City in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif leicester_score_hypothesis!= leicester_score_premise:
    # check if the score of Leicester from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
