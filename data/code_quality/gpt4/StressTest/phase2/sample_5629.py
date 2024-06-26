albert_age_times_mary_premise = 3
albert_age_times_mary_hypothesis = 2
albert_age_times_betty_premise = 4
albert_age_times_betty_hypothesis = 4

# the hypothesis refers to the age relations of Albert, Mary and Betty mentioned in the premise
if albert_age_times_mary_hypothesis >= albert_age_times_mary_premise:
    # check if the estimate of 'albert_age_times_mary_hypothesis' contradicts the number of times Albert's age is less than Mary's in the premise
    label = "contradiction"
elif albert_age_times_betty_hypothesis != albert_age_times_betty_premise:
    # check if the number of times Albert's age is equal to Betty's in the hypothesis contradicts the same relation reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
