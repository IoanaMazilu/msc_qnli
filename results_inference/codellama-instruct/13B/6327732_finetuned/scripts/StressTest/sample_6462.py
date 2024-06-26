students_random_premise = 302
students_random_hypothesis = 102
students_scramjet_premise = 232
students_scramjet_hypothesis = 232
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis refers to the number of students studying Random-processing methods and Scramjet rocket engines, both mentioned in the premise
if students_random_hypothesis <= students_random_premise:
    # check if the estimate of'students_random_hypothesis' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
