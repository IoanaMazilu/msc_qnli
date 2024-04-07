# Premise: John was thrice as old as Tom 6 yrs back.
# Hypothesis: John was thrice as old as Tom 1 yrs back.
# Golden Label: contradiction

john_age_difference_premise = 6
john_age_difference_hypothesis = 1

# the hypothesis refers to the age difference between John and Tom mentioned in the premise
if john_age_difference_premise != john_age_difference_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

