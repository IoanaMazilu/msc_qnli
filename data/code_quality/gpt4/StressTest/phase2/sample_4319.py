# defining the score variables for both premise and hypothesis
social_studies_score_premise = 60
science_score_premise = 89
art_score_premise = 62
music_score_premise = 69
spanish_score_premise = 84
biology_score_premise = 89
total_score_premise = 100

social_studies_score_hypothesis = 60
science_score_hypothesis = 89
art_score_hypothesis = 62
music_score_hypothesis = 69
spanish_score_hypothesis = 84
biology_score_hypothesis = 89

# checking if all the scores in the hypothesis are equal to those in the premise
if (social_studies_score_hypothesis != social_studies_score_premise or
    science_score_hypothesis != science_score_premise or
    art_score_hypothesis != art_score_premise or
    music_score_hypothesis != music_score_premise or
    spanish_score_hypothesis != spanish_score_premise or
    biology_score_hypothesis != biology_score_premise):
    label = "contradiction"
else:
    # if all the scores are equal, the only difference is in the total score (out of 100 in premise, more than 100 in hypothesis)
    label = "contradiction"

print(label)
