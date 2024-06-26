pat_tv_hours_premise_lower_bound = 1 # lower bound of standard deviations below the mean
pat_tv_hours_premise_upper_bound = 2 # upper bound of standard deviations below the mean
pat_tv_hours_hypothesis_lower_bound = 6 # lower bound of standard deviations below the mean in hypothesis
pat_tv_hours_hypothesis_upper_bound = 2 # upper bound of standard deviations below the mean in hypothesis

# the hypothesis talks about the number of hours Pat watched television, also mentioned in the premise
if pat_tv_hours_hypothesis_lower_bound < pat_tv_hours_premise_lower_bound or pat_tv_hours_hypothesis_upper_bound > pat_tv_hours_premise_upper_bound:
    # check if the lower bound of the hypothesis is less than the lower bound of the premise
    # or if the upper bound of the hypothesis is more than the upper bound of the premise
    # if so, it contradicts the premise
    label = "contradiction"
else:
    # otherwise, the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
