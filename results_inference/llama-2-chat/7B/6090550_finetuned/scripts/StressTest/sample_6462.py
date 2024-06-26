random_processing_students_premise = 302
random_processing_students_hypothesis = 102
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
students_study_both_premise = 112
students_study_both_hypothesis = 112

# the hypothesis refers to the number of students studying random-processing methods, Scramjet rocket engines and both
if random_processing_students_hypothesis <= random_processing_students_premise:
    label = "entailment"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying them in the premise
    label = "contradiction"
elif students_study_both_hypothesis!= students_study_both_premise:
    # check if the number of students studying both in the hypothesis contradicts the number of students studying both in the premise
    label = "contradiction"
else:
    label = "neutral"

print(label)
