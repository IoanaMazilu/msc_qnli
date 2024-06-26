suraj_avg_premise = 8
suraj_avg_hypothesis = 5

# the hypothesis refers to the number of innings in which Suraj has a certain average
if suraj_avg_hypothesis <= suraj_avg_premise:
    # check if the hypothesis value contradicts the estimate of'suraj_avg_premise'
    label = "contradiction"
elif suraj_avg_hypothesis > suraj_avg_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number of innings
    # any number of innings greater than'suraj_avg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
