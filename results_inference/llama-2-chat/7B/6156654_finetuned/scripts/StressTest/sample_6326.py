bobby_score_premise = 38
bobby_score_hypothesis = 88
bonny_score_premise = 56
bonny_score_hypothesis = 56
vijay_score_premise = 66
vijay_score_hypothesis = 66
libin_score_premise = 75
libin_score_hypothesis = 75

# the hypothesis refers to the scores of Bobby, Bonny, Vijay and Libin in the exam
if bobby_score_hypothesis!= bobby_score_premise:
    # check if Bobby's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
elif bonny_score_hypothesis!= bonny_score_premise:
    # check if Bonny's score in the hypothesis contradicts her score in the premise
    label = "contradiction"
elif vijay_score_hypothesis!= vijay_score_premise:
    # check if Vijay's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
elif libin_score_hypothesis!= libin_score_premise:
    # check if Libin's score in the hypothesis contradicts his score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
