bobby_score_premise = 48
bobby_score_hypothesis = 38
bonny_score_premise = 56
bonny_score_hypothesis = 56
vijay_score_premise = 66
vijay_score_hypothesis = 66
libin_score_premise = 75
libin_score_hypothesis = 75

# the hypothesis mentions the scores of Bobby, Bonny, Vijay and Libin in an exam, which are also referenced in the premise
if bonny_score_hypothesis != bonny_score_premise or vijay_score_hypothesis != vijay_score_premise or libin_score_hypothesis != libin_score_premise:
    # check if the scores of Bonny, Vijay and Libin in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
elif bobby_score_hypothesis >= bobby_score_premise:
    # check if the score of Bobby in the hypothesis contradicts the estimate of less than 'bobby_score_premise' 
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
