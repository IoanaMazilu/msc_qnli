sums_attempted_premise = 30
sums_attempted_hypothesis = 80
marks_obtained_premise = 65
marks_obtained_hypothesis = 65

# the hypothesis refers to the number of sums Sandy attempted and marks obtained, mentioned in the premise
if sums_attempted_hypothesis <= sums_attempted_premise:
    # check if the estimate of 'sums_attempted_hypothesis' contradicts the number of sums attempted in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
