rikki_gym_premise = 3
rikki_gym_hypothesis = 2

# the hypothesis refers to the number of weeks until Rikki's gym attendance increases
if rikki_gym_hypothesis <= rikki_gym_premise:
    # check if the hypothesis value contradicts the estimate of 'rikki_gym_premise'
    label = "contradiction"
elif rikki_gym_hypothesis > rikki_gym_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number of weeks until the increase
    # any number of weeks less than 'rikki_gym_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
