random_processing_students_premise = 302
scramjet_students_premise = 232
common_students_premise = 112

random_processing_students_hypothesis = 102
scramjet_students_hypothesis = 232
common_students_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the faculty of Aerospace Engineering
if random_processing_students_premise!= random_processing_students_hypothesis or scramjet_students_premise!= scramjet_students_hypothesis or common_students_premise!= common_students_hypothesis:
    # check if the number of students in each category in the hypothesis contradicts the number of students in each category in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
