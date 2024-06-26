students_random_processing_premise = 312
students_scramjet_premise = 234
students_both_premise = 112

students_random_processing_hypothesis = 112
students_scramjet_hypothesis = 234
students_both_hypothesis = 112

# the hypothesis refers to the number of students studying random-processing methods, scramjet rocket engines, and both
if students_random_processing_premise <= students_random_processing_hypothesis:
    # check if the number of students studying random-processing methods in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif students_scramjet_premise!= students_scramjet_hypothesis:
    # check if the number of students studying scramjet rocket engines in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif students_both_premise!= students_both_hypothesis:
    # check if the number of students studying both in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
