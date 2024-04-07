# Premise: Albert is less than 4 times Mary’s age and 4 times as old as Betty.
# Hypothesis: Albert is 2 times Mary’s age and 4 times as old as Betty.
# Golden Label: neutral

albert_mary_ratio_premise = 4
albert_mary_ratio_hypothesis = 2
albert_betty_ratio_premise = 4
albert_betty_ratio_hypothesis = 4

# the hypothesis talks about Albert's age compared to Mary's and Betty's age, which is also referenced in the premise
if albert_mary_ratio_hypothesis >= albert_mary_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'albert_mary_ratio_premise'
    label = "contradiction"
elif albert_betty_ratio_hypothesis != albert_betty_ratio_premise:
    # check if the age ratio between Albert and Betty in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # the premise gives a range for the age ratio between Albert and Mary
    # 'albert_mary_ratio_hypothesis' falls within this range, so it doesn't contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

