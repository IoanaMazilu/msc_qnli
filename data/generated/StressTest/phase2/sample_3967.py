# Premise: Albert is less than 7 times Mary’s age but only 4 times as old as Betty.
# Hypothesis: Albert is 2 times Mary’s age but only 4 times as old as Betty.
# Golden Label: neutral

albert_mary_ratio_premise = 7
albert_mary_ratio_hypothesis = 2

albert_betty_ratio_premise = 4
albert_betty_ratio_hypothesis = 4

# the hypothesis talks about Albert's age ratio to Mary's and Betty's, also mentioned in the premise
if albert_mary_ratio_hypothesis >= albert_mary_ratio_premise:
    # check if the hypothesis value contradicts the premise statement of Albert being less than 'albert_mary_ratio_premise' times Mary's age
    label = "contradiction"
elif albert_betty_ratio_hypothesis != albert_betty_ratio_premise:
    # check if the ratio of Albert's age to Betty's in the hypothesis contradicts the same ratio given in the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for Albert's age ratio to Mary's
    # any number less than 'albert_mary_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

