# Premise: If Danny scored more than 76, 75, 52, 87, 85 and 82 marks (out of 100) in English, Social Studies, Art, Music, Biology and French.
# Hypothesis: If Danny scored 86, 75, 52, 87, 85 and 82 marks (out of 100) in English, Social Studies, Art, Music, Biology and French.
# Golden Label: neutral

english_score_premise = 76
english_score_hypothesis = 86
social_studies_score_premise = 75
social_studies_score_hypothesis = 75
art_score_premise = 52
art_score_hypothesis = 52
music_score_premise = 87
music_score_hypothesis = 87
biology_score_premise = 85
biology_score_hypothesis = 85
french_score_premise = 82
french_score_hypothesis = 82

# the hypothesis talks about the scores of Danny in different subjects, also mentioned in the premise
if english_score_hypothesis <= english_score_premise:
    # check if the English score in the hypothesis contradicts the premise
    label = "contradiction"
elif social_studies_score_hypothesis != social_studies_score_premise:
    # check if the Social Studies score in the hypothesis contradicts the premise
    label = "contradiction"
elif art_score_hypothesis != art_score_premise:
    # check if the Art score in the hypothesis contradicts the premise
    label = "contradiction"
elif music_score_hypothesis != music_score_premise:
    # check if the Music score in the hypothesis contradicts the premise
    label = "contradiction"
elif biology_score_hypothesis != biology_score_premise:
    # check if the biology score in the hypothesis contradicts the premise
    label = "contradiction"
elif french_score_hypothesis != french_score_premise:
    # check if the French score in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

