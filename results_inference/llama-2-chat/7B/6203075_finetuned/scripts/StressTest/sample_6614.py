students_random_premise = 312
students_random_hypothesis = 212
students_scramjet_premise = 234
students_scramjet_hypothesis = 234
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis talks about the number of students studying Random-processing methods, Scramjet rocket engines, and both
if students_random_hypothesis!= students_random_premise:
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise or students_both_hypothesis!= students_both_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
