students_random_processing_premise = 302
students_scramjet_premise = 232
students_both_premise = 112
students_random_processing_hypothesis = 102
students_scramjet_hypothesis = 232
students_both_hypothesis = 112

# the hypothesis refers to the number of students studying Random-processing methods and both Scramjet rocket engines
if students_random_processing_hypothesis <= students_random_processing_premise:
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    label = "contradiction"
elif students_both_hypothesis!= students_both_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
