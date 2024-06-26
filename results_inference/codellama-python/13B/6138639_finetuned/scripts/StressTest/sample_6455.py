english_score_premise = 66
english_score_hypothesis = 66
math_score_premise = 60
math_score_hypothesis = 60
chemistry_score_premise = 72
chemistry_score_hypothesis = 72
biology_score_premise = 77
biology_score_hypothesis = 77
french_score_premise = 55
french_score_hypothesis = 55
physics_score_premise = 85
physics_score_hypothesis = 85

# the hypothesis refers to the scores of Andrea mentioned in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the estimate of 'english_score_hypothesis' contradicts the score of English in the premise
    label = "contradiction"
elif math_score_hypothesis!= math_score_premise:
    # check if the score of Mathematics in the hypothesis contradicts the score of Mathematics reported in the premise
    label = "contradiction"
elif chemistry_score_hypothesis!= chemistry_score_premise:
    # check if the score of Chemistry in the hypothesis contradicts the score of Chemistry reported in the premise
    label = "contradiction"
elif biology_score_hypothesis!= biology_score_premise:
    # check if the score of Biology in the hypothesis contradicts the score of Biology reported in the premise
    label = "contradiction"
elif french_score_hypothesis!= french_score_premise:
    # check if the score of French Language in the hypothesis contradicts the score of French Language reported in the premise
    label = "contradiction"
elif physics_score_hypothesis!= physics_score_premise:
    # check if the score of Physics in the hypothesis contradicts the score of Physics reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)