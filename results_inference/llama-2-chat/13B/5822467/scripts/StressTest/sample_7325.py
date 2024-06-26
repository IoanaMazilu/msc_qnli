rikki_gym_premise = 3
rikki_gym_hypothesis = 5

# the hypothesis refers to the number of weeks after which Rikki's gym attendance increases
if rikki_gym_hypothesis <= rikki_gym_premise:
    # check if the hypothesis value contradicts the estimate of 'rikki_gym_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks after which the increase happens
    # any number of weeks greater than 'rikki_gym_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
