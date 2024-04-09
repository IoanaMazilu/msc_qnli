students_premise = 310
students_hypothesis = 810

# the hypothesis talks about the number of students studying different topics at the faculty of Aerospace Engineering
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif students_hypothesis - students_premise == 232:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying them in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
