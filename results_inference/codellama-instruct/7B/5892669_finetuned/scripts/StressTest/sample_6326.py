bobby_score_premise = 38
bonny_score_premise = 56
vijay_score_premise = 66
libin_score_premise = 75

bobby_score_hypothesis = 88
bonny_score_hypothesis = 56
vijay_score_hypothesis = 66
libin_score_hypothesis = 75

# the hypothesis refers to the scores of Bobby, Bonny, Vijay and Libin mentioned in the premise
if bobby_score_hypothesis!= bobby_score_premise:
    # check if the score of Bobby in the hypothesis contradicts the score of Bobby reported in the premise
    label = "contradiction"
elif bonny_score_hypothesis!= bonny_score_premise or vijay_score_hypothesis!= vijay_score_premise or libin_score_hypothesis!= libin_score_premise:
    # check if the scores of Bonny, Vijay and Libin in the hypothesis contradict the scores of Bonny, Vijay and Libin reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
