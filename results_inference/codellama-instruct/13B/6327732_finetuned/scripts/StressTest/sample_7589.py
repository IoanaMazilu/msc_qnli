# define variables for the scores in the premise
french_language_score = 86
geography_score = 75
art_and_design_score = 72
history_score = 63
physical_education_score = 65

# define variables for the scores in the hypothesis
french_language_hypothesis = 86
geography_hypothesis = 75
art_and_design_hypothesis = 72
history_hypothesis = 63
physical_education_hypothesis = 65

# calculate the average score for the premise
total_score_premise = french_language_score + geography_score + art_and_design_score + history_score + physical_education_score
average_score_premise = total_score_premise / 5

# calculate the average score for the hypothesis
total_score_hypothesis = french_language_hypothesis + geography_hypothesis + art_and_design_hypothesis + history_hypothesis + physical_education_hypothesis
average_score_hypothesis = total_score_hypothesis / 5

# compare the average scores
if average_score_premise <= average_score_hypothesis:
    # check if the hypothesis value contradicts the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
