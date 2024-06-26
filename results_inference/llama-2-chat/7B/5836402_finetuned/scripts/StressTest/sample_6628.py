min_score_less_than_8 = 8
min_score_less_than_2 = 2
min_score_less_than_3 = 3

# the hypothesis refers to the minimum scores Mary got in the game, mentioned in the premise
if min_score_less_than_8 > min_score_less_than_3:
    # check if the minimum score'min_score_less_than_8' contradicts the minimum score'min_score_less_than_3' mentioned in the premise
    label = "contradiction"
elif min_score_less_than_3!= min_score_less_than_2:
    # check if the minimum score'min_score_less_than_3' contradicts the minimum score'min_score_less_than_2' mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
