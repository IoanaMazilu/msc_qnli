english_mark_premise = 86
english_mark_hypothesis = 46
spanish_mark_premise = 50
spanish_mark_hypothesis = 50
social_studies_mark_premise = 60
social_studies_mark_hypothesis = 60
fine_art_mark_premise = 67
fine_art_mark_hypothesis = 67
physical_education_mark_premise = 79
physical_education_mark_hypothesis = 79

# the hypothesis refers to the marks scored by Belinda in each subject, as mentioned in the premise
if english_mark_hypothesis >= english_mark_premise:
    # check if the estimate of 'english_mark_hypothesis' contradicts the number of marks in English in the premise
    label = "contradiction"
elif spanish_mark_hypothesis != spanish_mark_premise:
    # check if the number of marks in Spanish in the hypothesis contradicts the number of marks in Spanish reported in the premise
    label = "contradiction"
elif social_studies_mark_hypothesis != social_studies_mark_premise:
    # check if the number of marks in Social Studies in the hypothesis contradicts the number of marks in Social Studies reported in the premise
    label = "contradiction"
elif fine_art_mark_hypothesis != fine_art_mark_premise:
    # check if the number of marks in Fine Art in the hypothesis contradicts the number of marks in Fine Art reported in the premise
    label = "contradiction"
elif physical_education_mark_hypothesis != physical_education_mark_premise:
    # check if the number of marks in Physical Education in the hypothesis contradicts the number of marks in Physical Education reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
