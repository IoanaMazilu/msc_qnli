random_processing_students_premise = 102
random_processing_students_hypothesis = 302
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis talks about the number of students studying random-processing methods, Scramjet rocket engines and both
if random_processing_students_hypothesis <= random_processing_students_premise:
    label = "entailment"
elif scramjet_students_hypothesis!= scramjet_students_premise or students_both_hypothesis!= students_both_premise:
    # check if the number of students studying Scramjet rocket engines or both in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
