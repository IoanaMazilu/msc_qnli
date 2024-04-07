# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him 4 months later, investing Rs.
# Golden Label: contradiction

join_month_premise = 2
join_month_hypothesis = 4

# the hypothesis refers to the month Jose joined which is also mentioned in the premise
if join_month_premise != join_month_hypothesis:
    # check if the month in the hypothesis contradicts the month mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

