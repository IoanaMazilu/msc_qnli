score_us_premise = 2
score_slovenia_premise = 2
score_us_hypothesis = 2
score_slovenia_hypothesis = 2

# the hypothesis mentions the score of the match between the United States and Slovenia, which is also referenced in the premise
if score_us_hypothesis!= score_us_premise:
    # check if the score of the United States in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif score_slovenia_hypothesis!= score_slovenia_premise:
    # check if the score of Slovenia from the hypothesis contradicts the score of Slovenia in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
