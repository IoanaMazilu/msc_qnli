# define variables for the scores in the premise and hypothesis
french_language_premise = 46
french_language_hypothesis = 86
geography_premise = 75
geography_hypothesis = 75
art_and_design_premise = 72
art_and_design_hypothesis = 72
history_premise = 63
history_hypothesis = 63
physical_education_premise = 65
physical_education_hypothesis = 65

# calculate the average score for each subject in the premise and hypothesis
average_french_language_premise = (french_language_premise + geography_premise + art_and_design_premise + history_premise + physical_education_premise) / 5
average_french_language_hypothesis = (french_language_hypothesis + geography_hypothesis + art_and_design_hypothesis + history_hypothesis + physical_education_hypothesis) / 5

# check if the average score in the hypothesis contradicts the average score in the premise
if average_french_language_hypothesis <= average_french_language_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
