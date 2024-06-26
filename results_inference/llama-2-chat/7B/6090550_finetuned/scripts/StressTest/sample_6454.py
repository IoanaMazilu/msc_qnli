# scores in the premise
score_english = 76
score_mathematics = 60
score_chemistry = 72
score_biology = 77
score_french_language = 55
score_physics = 85

# scores in the hypothesis
score_english_hypothesis = 66
score_mathematics_hypothesis = 60
score_chemistry_hypothesis = 72
score_biology_hypothesis = 77
score_french_language_hypothesis = 55
score_physics_hypothesis = 85

# calculate the average score in each subject
score_english_premise = score_english
score_mathematics_premise = score_mathematics
score_chemistry_premise = score_chemistry
score_biology_premise = score_biology
score_french_language_premise = score_french_language
score_physics_premise = score_physics

# calculate the average score in each subject in the hypothesis
score_english_hypothesis = score_english_hypothesis
score_mathematics_hypothesis = score_mathematics_hypothesis
score_chemistry_hypothesis = score_chemistry_hypothesis
score_biology_hypothesis = score_biology_hypothesis
score_french_language_hypothesis = score_french_language_hypothesis
score_physics_hypothesis = score_physics_hypothesis

# compare the average scores in each subject in the hypothesis with the average scores in each subject in the premise
if score_english_hypothesis!= score_english_premise or score_mathematics_hypothesis!= score_mathematics_premise or score_chemistry_hypothesis!= score_chemistry_premise or score_biology_hypothesis!= score_biology_premise or score_french_language_hypothesis!= score_french_language_premise or score_physics_hypothesis!= score_physics_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
