# Premise: John was thrice as old as Tom more than 4 yrs back.
# Hypothesis: John was thrice as old as Tom 6 yrs back.
# Golden Label: neutral

john_old_time_premise = 4
john_old_time_hypothesis = 6

# the hypothesis refers to the time when John was thrice as old as Tom, also mentioned in the premise
if john_old_time_hypothesis != john_old_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise exactly specifies the time when John was thrice as old as Tom
    # if the hypothesis time matches the premise time, we can infer entailment
    label = "entailment"

print(label)

