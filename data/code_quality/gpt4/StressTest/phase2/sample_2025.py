john_age_difference_premise = 6
john_age_difference_hypothesis = 5

# The hypothesis refers to the time when John was thrice as old as Tom, also mentioned in the premise
if john_age_difference_hypothesis >= john_age_difference_premise:
    # Check if the hypothesis value contradicts the time of 'john_age_difference_premise' years back
    label = "contradiction"
elif john_age_difference_hypothesis != john_age_difference_premise:
    # Check if the time in the hypothesis differs from the time reported in the premise
    label = "contradiction"
else:
    # If the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
