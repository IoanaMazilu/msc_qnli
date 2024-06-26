john_age_multiple_premise = 3
tom_age_past_premise = 6

john_age_multiple_hypothesis = 3
tom_age_past_hypothesis = 5

# the hypothesis refers to the age difference between John and Tom mentioned in the premise
if john_age_multiple_premise != john_age_multiple_hypothesis:
    # check if the age multiple in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif tom_age_past_premise != tom_age_past_hypothesis:
    # check if the past years in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
