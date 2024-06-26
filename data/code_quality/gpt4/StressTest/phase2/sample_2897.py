english_premise = 86
social_studies_premise = 75
art_premise = 52
music_premise = 87
biology_premise = 85
french_premise = 82

english_hypothesis = 86
social_studies_hypothesis = 75
art_hypothesis = 52
music_hypothesis = 87
biology_hypothesis = 85
french_hypothesis = 82

# the hypothesis states that Danny scored more than the mentioned marks in each subject in the premise
if english_hypothesis <= english_premise or social_studies_hypothesis <= social_studies_premise or art_hypothesis <= art_premise or music_hypothesis <= music_premise or biology_hypothesis <= biology_premise or french_hypothesis <= french_premise:
    # check if the hypothesis contradicts the premise by stating that Danny scored more than the mentioned marks in each subject
    label = "contradiction"
else:
    # the premise gives exact marks for each subject, but the hypothesis suggests that Danny scored more than the mentioned marks
    # this is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
