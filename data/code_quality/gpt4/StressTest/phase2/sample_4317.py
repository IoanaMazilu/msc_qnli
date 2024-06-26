# Scores for different subjects as per premise
social_studies_premise = 60
science_premise = 89
art_premise = 62
music_premise = 69
spanish_premise = 84
biology_premise = 89

# Total score as per premise
total_score_premise = social_studies_premise + science_premise + art_premise + music_premise + spanish_premise + biology_premise

# Scores for different subjects as per hypothesis
social_studies_hypothesis = 60
science_hypothesis = 89
art_hypothesis = 62
music_hypothesis = 69
spanish_hypothesis = 84
biology_hypothesis = 89

# Total score as per hypothesis
total_score_hypothesis = social_studies_hypothesis + science_hypothesis + art_hypothesis + music_hypothesis + spanish_hypothesis + biology_hypothesis

# The hypothesis refers to the scores in each subject and the total score. 
# We need to compare each individual score as well as the total score to establish relationship

if total_score_premise != total_score_hypothesis:
    # if total scores from premise and hypothesis don't match
    label = "contradiction"
elif social_studies_premise != social_studies_hypothesis or science_premise != science_hypothesis or art_premise != art_hypothesis or music_premise != music_hypothesis or spanish_premise != spanish_hypothesis or biology_premise != biology_hypothesis :
    # if individual scores from premise and hypothesis don't match
    label = "contradiction"
elif total_score_hypothesis >= 400:
    # hypothesis mentions total score should be less than 400, if it's not, it's contradiction
    label = "contradiction"
else:
    # if individual and total scores from premise and hypothesis match and total score is less than 400, it's entailment
    label = "entailment"

print(label)
