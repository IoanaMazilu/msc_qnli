norwich_score_premise = 1
united_score_premise = 0
city_score_premise = 5
villa_score_premise = 0

norwich_score_hypothesis = 1
united_score_hypothesis = 0

# the hypothesis mentions the result of the match between Norwich and United, which is also mentioned in the premise
if norwich_score_hypothesis != norwich_score_premise or united_score_hypothesis != united_score_premise:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
