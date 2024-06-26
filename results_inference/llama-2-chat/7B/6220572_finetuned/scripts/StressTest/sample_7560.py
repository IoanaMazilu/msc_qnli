students_random_premise = 310
students_random_hypothesis = 110
students_scramjet_premise = 232
students_scramjet_hypothesis = 232

# the hypothesis talks about the number of students studying different subjects, referenced also in the premise
if students_random_hypothesis <= students_random_premise:
    # check if the hypothesis value contradicts the estimate of more than'students_random_premise'
    label = "contradiction"
elif students_scramjet_hypothesis!= students_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
else:
    # the premise gives only estimates for the number of students studying different subjects
    # any number of students studying different subjects consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
