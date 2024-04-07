# Premise: Ravina leaves the job 3 days before the completion of the work.
# Hypothesis: Ravina leaves the job more than 1 days before the completion of the work.
# Golden Label: entailment

leave_days_premise = 3
leave_days_hypothesis = 1

# the hypothesis refers to the number of days Ravina leaves the job before the completion of the work as mentioned in the premise
if leave_days_hypothesis >= leave_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

