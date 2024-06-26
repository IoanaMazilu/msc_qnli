math_premise = 76
science_premise = 65
social_studies_premise = 82
english_premise = 67
biology_premise = 55

math_hypothesis = 66
science_hypothesis = 65
social_studies_hypothesis = 82
english_hypothesis = 67
biology_hypothesis = 55

# the hypothesis refers to the marks scored by Shekar in different subjects mentioned in the premise
if math_hypothesis != math_premise:
    # check if the mathematics score in the hypothesis contradicts the mathematics score reported in the premise
    label = "contradiction"
elif science_hypothesis != science_premise or social_studies_hypothesis != social_studies_premise or english_hypothesis != english_premise or biology_hypothesis != biology_premise:
    # check if the scores in other subjects in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
