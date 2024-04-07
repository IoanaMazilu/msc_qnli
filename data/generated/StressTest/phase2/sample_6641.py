# Premise: If Ram and Krish together can complete the same work in 40 days, then how long will Bhim take to complete it?
# Hypothesis: If Ram and Krish together can complete the same work in more than 40 days, then how long will Bhim take to complete it?
# Golden Label: contradiction

work_days_premise = 40
work_days_hypothesis = 40

# the hypothesis refers to the number of days Ram and Krish need to complete a work, which is also mentioned in the premise
if work_days_hypothesis > work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

