# Scores of Bobby, Bonny, Vijay and Libin in the premise
bobby_score_premise = 38
bonny_score_premise = 56
vijay_score_premise = 66
libin_score_premise = 75

# Scores of Bobby, Bonny, Vijay and Libin in the hypothesis
bobby_score_hypothesis = 88
bonny_score_hypothesis = 56
vijay_score_hypothesis = 66
libin_score_hypothesis = 75

# The hypothesis refers to the scores of Bobby, Bonny, Vijay and Libin mentioned in the premise
if bobby_score_hypothesis!= bobby_score_premise:
    # Check if the score of Bobby in the hypothesis contradicts the score of Bobby in the premise
    label = "contradiction"
elif bonny_score_hypothesis!= bonny_score_premise:
    # Check if the score of Bonny in the hypothesis contradicts the score of Bonny in the premise
    label = "contradiction"
elif vijay_score_hypothesis!= vijay_score_premise:
    # Check if the score of Vijay in the hypothesis contradicts the score of Vijay in the premise
    label = "contradiction"
elif libins_score_hypothesis!= libins_score_premise:
    # Check if the score of Libin in the hypothesis contradicts the score of Libin in the premise
    label = "contradiction"
else:
    # If the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
