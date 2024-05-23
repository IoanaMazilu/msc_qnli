english_score_premise = 76
english_score_hypothesis = 66
mathematics_score_premise = 60
mathematics_score_hypothesis = 60
chemistry_score_premise = 72
chemistry_score_hypothesis = 72
biology_score_premise = 77
biology_score_hypothesis = 77
french_language_score_premise = 55
french_language_score_hypothesis = 55
physics_score_premise = 85
physics_score_hypothesis = 85

# calculate the average score for each subject
english_score_avg_premise = (english_score_premise + mathematics_score_premise + chemistry_score_premise + biology_score_premise + french_language_score_premise + physics_score_premise) / 6
english_score_avg_hypothesis = (english_score_hypothesis + mathematics_score_hypothesis + chemistry_score_hypothesis + biology_score_hypothesis + french_language_score_hypothesis + physics_score_hypothesis) / 6

# compare the average scores
if english_score_avg_premise <= english_score_avg_hypothesis:
    label = "entailment"
elif english_score_avg_hypothesis!= english_score_avg_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)