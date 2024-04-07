# Premise: If Danny scored 86, 75, 52, 87, 85 and 82 marks (out of 100) in English, Social Studies, Art, Music, Biology and French.
# Hypothesis: If Danny scored more than 76, 75, 52, 87, 85 and 82 marks (out of 100) in English, Social Studies, Art, Music, Biology and French.
# Golden Label: entailment

eng_premise = 86
soc_studies_premise = 75
art_premise = 52
music_premise = 87
bio_premise = 85
french_premise = 82

eng_hypothesis = 76
soc_studies_hypothesis = 75
art_hypothesis = 52
music_hypothesis = 87
bio_hypothesis = 85
french_hypothesis = 82

# the hypothesis refers to the scores of Danny in different subjects mentioned in the premise
if eng_premise <= eng_hypothesis:
    # check if the estimate of 'eng_hypothesis' contradicts the score in English in the premise
    label = "contradiction"
elif soc_studies_premise != soc_studies_hypothesis or art_premise != art_hypothesis or music_premise != music_hypothesis or bio_premise != bio_hypothesis or french_premise != french_hypothesis:
    # check if the scores in other subjects in the hypothesis contradict the corresponding scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

