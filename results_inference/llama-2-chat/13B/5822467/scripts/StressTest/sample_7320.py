rikki_gym_premise = 2 * 3 = 6
rikki_gym_hypothesis = 2 * 5 = 10

# the hypothesis refers to the number of weeks Rikki has gone to the gym
if rikki_gym_hypothesis <= rikki_gym_premise:
    # check if the hypothesis value contradicts the estimate of 'rikki_gym_premise'
    label = "contradiction"
elif rikki_gym_hypothesis > rikki_gym_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than or equal to 6 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
