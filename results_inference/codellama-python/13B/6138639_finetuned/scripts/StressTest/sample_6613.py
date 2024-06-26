students_random_premise = 112
students_random_hypothesis = 312
students_scramjet_premise = 234
students_scramjet_hypothesis = 234
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis talks about the number of students studying Random-processing methods, Scramjet rocket engines and both, referenced also in the premise
if students_random_hypothesis <= students_random_premise:
    # check if the hypothesis value contradicts the estimate of more than'students_random_premise'
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
elif students_both_hypothesis!= students_both_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying Random-processing methods
    # any number of students greater than'students_random_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
