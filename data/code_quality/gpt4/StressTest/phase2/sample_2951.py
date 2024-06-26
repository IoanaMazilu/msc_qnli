subtract_from_age_premise = 6
subtract_from_age_hypothesis = 2

# both the premise and the hypothesis refer to the calculation of Anup's age based on John's age
if subtract_from_age_premise != subtract_from_age_hypothesis:
    # check if the number of years subtracted from John's age in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of years subtracted in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
