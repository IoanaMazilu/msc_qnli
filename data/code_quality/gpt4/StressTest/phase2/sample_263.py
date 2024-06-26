sums_attempted_premise = 30
sums_attempted_hypothesis = 50
marks_obtained_premise = 55
marks_obtained_hypothesis = 55

# the hypothesis refers to the number of sums attempted and marks obtained by Sandy, also mentioned in the premise
if sums_attempted_hypothesis != sums_attempted_premise:
    # check if the number of sums attempted in the hypothesis contradicts the number of sums attempted in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
