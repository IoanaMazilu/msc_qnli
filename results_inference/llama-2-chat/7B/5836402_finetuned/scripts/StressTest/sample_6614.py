random_processing_students_premise = 312
scramjet_students_premise = 234
students_both_premise = 112

random_processing_students_hypothesis = 212
scramjet_students_hypothesis = 234
students_both_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the faculty of Aerospace Engineering mentioned in the premise
if random_processing_students_premise!= random_processing_students_hypothesis or \
   scramjet_students_premise!= scramjet_students_hypothesis or \
   students_both_premise!= students_both_hypothesis:
    # check if the number of students studying different subjects in the hypothesis contradicts the number of students studying different subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
