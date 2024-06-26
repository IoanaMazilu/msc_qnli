man_city_score_premise = 2
leicester_score_premise = 2
man_city_score_hypothesis = 2
leicester_score_hypothesis = 2

# the hypothesis mentions the scores of Manchester City and Leicester, which are also mentioned in the premise
if man_city_score_hypothesis != man_city_score_premise:
    # check if the score of Manchester City in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif leicester_score_hypothesis != leicester_score_premise:
    # check if the score of Leicester from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
