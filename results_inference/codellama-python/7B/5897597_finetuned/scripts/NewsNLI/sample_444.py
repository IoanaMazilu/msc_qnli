wales_place_premise = 3
wales_place_hypothesis = 3
scotland_score_premise = 3
scotland_score_hypothesis = 3

# the hypothesis mentions Wales' place above France and the score of Wales' match with Scotland, which are also mentioned in the premise
if wales_place_hypothesis!= wales_place_premise:
    # check if Wales' place in the hypothesis contradicts Wales' place in the premise
    label = "contradiction"
elif scotland_score_hypothesis!= scotland_score_premise:
    # check if the score of Wales' match with Scotland from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
