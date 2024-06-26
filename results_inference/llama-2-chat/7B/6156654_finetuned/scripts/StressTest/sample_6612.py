students_random_processing_premise = 312
students_scramjet_rocket_engines_premise = 234
students_both_premise = 112

students_random_processing_hypothesis = 112
students_scramjet_rocket_engines_hypothesis = 234
students_both_hypothesis = 112

# the hypothesis talks about the number of students studying random-processing methods, scramjet rocket engines, and both
if students_random_processing_hypothesis <= students_random_processing_premise:
    label = "contradiction"
elif students_scramjet_rocket_engines_hypothesis!= students_scramjet_rocket_engines_premise:
    label = "contradiction"
elif students_both_hypothesis!= students_both_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
