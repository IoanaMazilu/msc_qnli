# Premise: Albert is 2 times Mary’s age and 4 times as old as Betty.
# Hypothesis: Albert is more than 2 times Mary’s age and 4 times as old as Betty.
# Golden Label: contradiction

albert_age_times_mary_premise = 2
albert_age_times_betty_premise = 4
albert_age_times_mary_hypothesis = 2
albert_age_times_betty_hypothesis = 4

# the hypothesis talks about Albert's age in relation to Mary's and Betty's ages, which is also mentioned in the premise
if albert_age_times_mary_hypothesis == albert_age_times_mary_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif albert_age_times_betty_hypothesis != albert_age_times_betty_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates are the same as in the premise, but the hypothesis uses the term 'more than' which contradicts the premise
    label = "contradiction"

print(label)

