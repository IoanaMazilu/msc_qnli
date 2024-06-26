premise_argentina_score = 2
premise_greece_score = 0
premise_south_korea_score = 2
premise_nigeria_score = 0

hypothesis_south_korea_score = 2
hypothesis_nigeria_score = 0

# the hypothesis mentions the score of South Korea and Nigeria, which are also mentioned in the premise
if hypothesis_south_korea_score!= premise_south_korea_score:
    # check if the score of South Korea in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif hypothesis_nigeria_score!= premise_nigeria_score:
    # check if the score of Nigeria in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
