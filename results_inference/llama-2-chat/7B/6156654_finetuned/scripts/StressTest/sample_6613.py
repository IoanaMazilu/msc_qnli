students_random_processing_premise = 112
students_scramjet_rocket_engines_premise = 234
students_study_both_premise = 112
students_random_processing_hypothesis = 312
students_scramjet_rocket_engines_hypothesis = 234
students_study_both_hypothesis = 112

# the hypothesis talks about the number of students studying random-processing methods and scramjet rocket engines, which are also mentioned in the premise
if students_random_processing_hypothesis!= students_random_processing_premise:
    label = "contradiction"
elif students_scramjet_rocket_engines_hypothesis!= students_scramjet_rocket_engines_premise:
    label = "contradiction"
elif students_study_both_hypothesis!= students_study_both_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
