maths_premise = 76
maths_hypothesis = 16
science_premise = 65
science_hypothesis = 65
social_studies_premise = 82
social_studies_hypothesis = 82
english_premise = 62
english_hypothesis = 62
biology_premise = 85
biology_hypothesis = 85

# the hypothesis refers to the scores in Mathematics, Science, Social studies, English and Biology mentioned in the premise
if maths_hypothesis > maths_premise:
    # check if the 'maths_hypothesis' contradicts the Mathematics score in the premise
    label = "contradiction"
elif science_hypothesis != science_premise:
    # check if the 'science_hypothesis' contradicts the Science score in the premise
    label = "contradiction"
elif social_studies_hypothesis != social_studies_premise:
    # check if the 'social_studies_hypothesis' contradicts the Social studies score in the premise
    label = "contradiction"
elif english_hypothesis != english_premise:
    # check if the 'english_hypothesis' contradicts the English score in the premise
    label = "contradiction"
elif biology_hypothesis != biology_premise:
    # check if the 'biology_hypothesis' contradicts the Biology score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
