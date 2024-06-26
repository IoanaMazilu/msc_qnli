random_processing_students_premise = 302
random_processing_students_hypothesis = 102
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis refers to the number of students studying random-processing methods, Scramjet rocket engines, and both
if random_processing_students_hypothesis <= random_processing_students_premise:
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    label = "contradiction"
elif both_students_hypothesis!= both_students_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
