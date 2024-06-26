total_score_premise = 400
total_score_hypothesis = 100

social_studies_score_premise = 60
science_score_premise = 89
art_score_premise = 62
music_score_premise = 69
spanish_score_premise = 84
biology_score_premise = 89

social_studies_score_hypothesis = 60
science_score_hypothesis = 89
art_score_hypothesis = 62
music_score_hypothesis = 69
spanish_score_hypothesis = 84
biology_score_hypothesis = 89

# the hypothesis talks about the scores of various subjects, similar to the premise
if total_score_hypothesis != total_score_premise:
    # check if the total possible score in the hypothesis contradicts the total possible score mentioned in the premise
    label = "contradiction"
elif social_studies_score_hypothesis != social_studies_score_premise or science_score_hypothesis != science_score_premise or art_score_hypothesis != art_score_premise or music_score_hypothesis != music_score_premise or spanish_score_hypothesis != spanish_score_premise or biology_score_hypothesis != biology_score_premise:
    # check if any of the subject scores in the hypothesis contradict the respective subject scores mentioned in the premise
    label = "contradiction"
else:
    # if none of the hypothesis values contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
