students_random_premise = 102
students_scramjet_premise = 232
students_both_premise = 112
students_random_hypothesis = 302
students_scramjet_hypothesis = 232
students_both_hypothesis = 112

# the hypothesis refers to the number of students studying random-processing methods, scramjet rocket engines and both
if students_random_hypothesis!= students_random_premise:
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    label = "contradiction"
elif students_both_hypothesis!= students_both_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
