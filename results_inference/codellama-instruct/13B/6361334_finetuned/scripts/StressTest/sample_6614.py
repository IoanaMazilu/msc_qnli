students_random_premise = 312
students_random_hypothesis = 212
students_scramjet_premise = 234
students_scramjet_hypothesis = 234
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis refers to the number of students studying Random-processing methods, Scramjet rocket engines and both, mentioned in the premise
if students_random_hypothesis!= students_random_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number of students mentioned in the premise
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students mentioned in the premise
    label = "contradiction"
elif students_both_hypothesis!= students_both_premise:
    # check if the number of students studying both Random-processing methods and Scramjet rocket engines in the hypothesis contradicts the number of students mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)