students_random_premise = 112
students_random_hypothesis = 312
students_scramjet_premise = 234
students_scramjet_hypothesis = 234
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis talks about the number of students studying different subjects, which are also referenced in the premise
if students_random_hypothesis!= students_random_premise:
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    label = "contradiction"
elif students_both_hypothesis!= students_both_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
