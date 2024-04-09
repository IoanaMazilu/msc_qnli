# Scores in different subjects as per the premise and hypothesis
math_score_premise = 76
science_score_premise = 65
social_studies_score_premise = 82
english_score_premise = 67
biology_score_premise = 75

math_score_hypothesis = 46
science_score_hypothesis = 65
social_studies_score_hypothesis = 82
english_score_hypothesis = 67
biology_score_hypothesis = 75

# Check if the scores in the hypothesis contradict the scores in the premise
if math_score_hypothesis >= math_score_premise:
    label = "contradiction"
elif science_score_hypothesis!= science_score_premise or social_studies_score_hypothesis!= social_studies_score_premise or english_score_hypothesis!= english_score_premise or biology_score_hypothesis!= biology_score_premise:
    label = "contradiction"
else:
    # If the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
