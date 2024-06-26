# define the variables
age_in_future_premise = 18
age_in_future_hypothesis = 38
age_past = 6
multiplier = 5

# compare the age in future in premise and hypothesis
if age_in_future_hypothesis < age_in_future_premise:
    # check if the future age estimate in hypothesis contradicts the future age in premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise but it can't be explicitly entailed from the premise
    label = "neutral"

print(label)
