albert_age_mary_premise = 2
albert_age_mary_hypothesis = 6
albert_age_betty_premise = 4
albert_age_betty_hypothesis = 4

# the hypothesis refers to Albert's age compared to Mary's and Betty's, as mentioned in the premise
if albert_age_mary_premise >= albert_age_mary_hypothesis:
    # check if the estimate of 'albert_age_mary_hypothesis' contradicts the comparison of Albert's age to Mary's in the premise
    label = "contradiction"
elif albert_age_betty_hypothesis != albert_age_betty_premise:
    # check if the comparison of Albert's age to Betty's in the hypothesis contradicts the comparison in the premise
    label = "contradiction"
else:
    # if the hypothesis values and comparisons do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
