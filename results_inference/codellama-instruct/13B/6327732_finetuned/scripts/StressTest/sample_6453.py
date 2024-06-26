# define variables for the scores in the premise
english_score_premise = 66
mathematics_score_premise = 60
chemistry_score_premise = 72
biology_score_premise = 77
french_language_score_premise = 55
physics_score_premise = 85

# define variables for the scores in the hypothesis
english_score_hypothesis = 76
mathematics_score_hypothesis = 60
chemistry_score_hypothesis = 72
biology_score_hypothesis = 77
french_language_score_hypothesis = 55
physics_score_hypothesis = 85

# calculate the average score for the premise
average_score_premise = (english_score_premise + mathematics_score_premise + chemistry_score_premise + biology_score_premise + french_language_score_premise + physics_score_premise) / 6

# calculate the average score for the hypothesis
average_score_hypothesis = (english_score_hypothesis + mathematics_score_hypothesis + chemistry_score_hypothesis + biology_score_hypothesis + french_language_score_hypothesis + physics_score_hypothesis) / 6

# compare the average scores
if average_score_hypothesis < average_score_premise:
    # the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise
    label = "neutral"

print(label)
