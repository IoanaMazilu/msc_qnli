# Premise: After working for 6 days, David was joined by Moore.
# Hypothesis: After working for less than 6 days, David was joined by Moore.
# Golden Label: contradiction

work_days_premise = 6
work_days_hypothesis = 6

# the hypothesis refers to the number of days David worked alone before Moore joined him, also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

