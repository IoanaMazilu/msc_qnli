# Scores from premise
english_score_premise = 76
math_score_premise = 60
chemistry_score_premise = 72
biology_score_premise = 77
french_score_premise = 55
physics_score_premise = 85

# Scores from hypothesis
english_score_hypothesis = 66
math_score_hypothesis = 60
chemistry_score_hypothesis = 72
biology_score_hypothesis = 77
french_score_hypothesis = 55
physics_score_hypothesis = 85

# Check if the scores from hypothesis contradict the scores from premise
if (english_score_hypothesis >= english_score_premise) or (math_score_hypothesis!= math_score_premise) or (chemistry_score_hypothesis!= chemistry_score_premise) or (biology_score_hypothesis!= biology_score_premise) or (french_score_hypothesis!= french_score_premise) or (physics_score_hypothesis!= physics_score_premise):
    label = "contradiction"
else:
    # If the scores from hypothesis do not contradict the scores from premise, we can infer entailment
    label = "entailment"

print(label)
