students_random_premise = 110
students_random_hypothesis = 310
students_scramjet_premise = 232
students_scramjet_hypothesis = 232
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis mentions the number of students studying both Random-processing methods and Scramjet rocket engines
if students_both_hypothesis <= students_both_premise:
    # check if the hypothesis value contradicts the number of students studying both methods in the premise
    label = "contradiction"
elif students_random_hypothesis!= students_random_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)