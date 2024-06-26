home_time_premise = 5
home_time_hypothesis = 5

# the hypothesis refers to Sasha's home reaching time mentioned in the premise
if home_time_hypothesis > home_time_premise:
    # check if the 'home_time_hypothesis' contradicts the home reaching time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
