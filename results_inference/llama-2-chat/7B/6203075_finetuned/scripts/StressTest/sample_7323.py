average_times_gym_premise = 3
average_times_gym_hypothesis = 3

# the hypothesis refers to the same increase in the average number of times Rikki goes to the gym, after a certain number of weeks
if average_times_gym_hypothesis!= average_times_gym_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value, we can infer entailment
    label = "entailment"

print(label)
