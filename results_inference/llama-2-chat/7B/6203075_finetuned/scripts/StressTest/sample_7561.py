students_random_processing_premise = 110
students_scramjet_premise = 232
students_random_processing_hypothesis = 310
students_scramjet_hypothesis = 232
students_study_both_premise = 112
students_study_both_hypothesis = 112

# the hypothesis refers to the number of students studying random-processing methods, Scramjet rocket engines and both
if students_random_processing_hypothesis!= students_random_processing_premise:
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    label = "contradiction"
elif students_study_both_hypothesis!= students_study_both_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
