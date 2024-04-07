# Premise: Calculate the average mark scored by Nancy if she obtained the following scores in an examination:65, 78, 89, 51 and 69 marks (out of 100) in English Language, Physics, Mathematics, Chemistry and Biology?
# Hypothesis: Calculate the average mark scored by Nancy if she obtained the following scores in an examination:less than 65, 78, 89, 51 and 69 marks (out of 100) in English Language, Physics, Mathematics, Chemistry and Biology?
# Golden Label: contradiction

english_score_premise = 65
english_score_hypothesis = 65
physics_score_premise = 78
physics_score_hypothesis = 78
math_score_premise = 89
math_score_hypothesis = 89
chem_score_premise = 51
chem_score_hypothesis = 51
bio_score_premise = 69
bio_score_hypothesis = 69

# the hypothesis refers to the scores of Nancy in various subjects mentioned in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'english_score_premise'
    label = "contradiction"
elif physics_score_hypothesis != physics_score_premise or math_score_hypothesis != math_score_premise or chem_score_hypothesis != chem_score_premise or bio_score_hypothesis != bio_score_premise:
    # check if the scores in the rest of the subjects mentioned in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact scores for each subject
    # any score less than the given score in English and equal scores in the rest of the subjects is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

