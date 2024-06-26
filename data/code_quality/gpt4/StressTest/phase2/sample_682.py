english_score_premise = 46
english_score_hypothesis = 86
spanish_score = 50
social_studies_score = 60
fine_art_score = 67
physical_education_score = 79

# The hypothesis refers to the scores of Belinda in multiple subjects mentioned in the premise
if english_score_hypothesis <= english_score_premise:
    # Check if the score of English in the hypothesis contradicts the score of English in the premise
    label = "contradiction"
else:
    # if the English score in the hypothesis does not contradict the premise one, we cannot infer entailment, but neutrality
    label = "neutral"

print(label)
