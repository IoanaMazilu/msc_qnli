john_rake_time_premise = 10
john_rake_time_hypothesis = 30
todd_rake_time_premise = 60
todd_rake_time_hypothesis = 60

# the hypothesis refers to the time it takes John and Todd to rake the lawn, also mentioned in the premise
if john_rake_time_hypothesis <= john_rake_time_premise:
    # check if the time taken by John in the hypothesis contradicts the estimate of more than 'john_rake_time_premise' in the premise
    label = "contradiction"
elif todd_rake_time_hypothesis != todd_rake_time_premise:
    # check if the time taken by Todd in the hypothesis contradicts the time taken by Todd reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by John
    # any time greater than 'john_rake_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
