# Premise: Shekar scored 76, 65, 82, 67 and 95 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Hypothesis: Shekar scored more than 46, 65, 82, 67 and 95 marks in Mathematics, Science, Social studies, English and Biology respectively.
# Golden Label: entailment

# define the scores from the premise
maths_premise = 76
science_premise = 65
social_studies_premise = 82
english_premise = 67
biology_premise = 95

# define the scores from the hypothesis
maths_hypothesis = 46
science_hypothesis = 65
social_studies_hypothesis = 82
english_hypothesis = 67
biology_hypothesis = 95

# compare the scores from the premise and the hypothesis
if maths_hypothesis >= maths_premise or science_hypothesis > science_premise or social_studies_hypothesis > social_studies_premise or english_hypothesis > english_premise or biology_hypothesis > biology_premise:
    # check if any score from the hypothesis contradicts the corresponding score from the premise
    label = "contradiction"
elif maths_hypothesis < maths_premise and science_hypothesis == science_premise and social_studies_hypothesis == social_studies_premise and english_hypothesis == english_premise and biology_hypothesis == biology_premise:
    # check if all scores from the hypothesis are either less than or equal to the corresponding scores from the premise
    label = "entailment"
else:
    # if neither of the above conditions are met, the relation is neutral
    label = "neutral"

print(label)

