students_random_premise = 312
students_random_hypothesis = 112
students_scramjet_premise = 234
students_scramjet_hypothesis = 234

# the hypothesis talks about the number of students studying different subjects, which are also mentioned in the premise
if students_random_hypothesis <= students_random_premise:
    # check if the hypothesis value contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
