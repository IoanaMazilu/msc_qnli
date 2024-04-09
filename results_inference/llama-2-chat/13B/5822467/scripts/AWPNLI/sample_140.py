students_premise = 10.0
students_got_off_premise = 3.0
students_hypothesis = 7.0

# compute the number of students left on the bus based on the premise
students_left_premise = students_premise - students_got_off_premise

if students_hypothesis > students_left_premise:
    # check if the number of students left on the bus in the hypothesis contradicts the estimate of students left on the bus from the premise
    label = "contradiction"
elif students_hypothesis!= students_left_premise:
    # check if the number of students left on the bus in the hypothesis contradicts the number of students left on the bus from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
