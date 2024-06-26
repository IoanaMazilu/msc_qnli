albert_age_times_mary_premise = 2
albert_age_times_betty_premise = 4
albert_age_times_mary_hypothesis = 3
albert_age_times_betty_hypothesis = 4

# the hypothesis refers to Albert's age in relation to Mary's and Betty's, just like the premise
if albert_age_times_mary_hypothesis < albert_age_times_mary_premise:
    # check if the hypothesis estimate contradicts the multiplier of Albert's age in relation to Mary's age in the premise
    label = "contradiction"
elif albert_age_times_betty_hypothesis != albert_age_times_betty_premise:
    # check if the multiplier of Albert's age in relation to Betty's age in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
