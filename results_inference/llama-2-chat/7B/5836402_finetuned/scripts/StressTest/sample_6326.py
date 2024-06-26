bobby_score_premise = 38
bobby_score_hypothesis = 88
bonny_score_premise = 56
bonny_score_hypothesis = 56
vijay_score_premise = 66
vijay_score_hypothesis = 66
libin_score_premise = 75
libin_score_hypothesis = 75

# the hypothesis refers to the scores of the students in the premise
if bobby_score_premise!= bobby_score_hypothesis:
    # check if the score of Bobby in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif bonny_score_hypothesis!= bonny_score_premise:
    # check if the score of Bonny in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif vijay_score_hypothesis!= vijay_score_premise:
    # check if the score of Vijay in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif libin_score_hypothesis!= libin_score_premise:
    # check if the score of Libin in the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
