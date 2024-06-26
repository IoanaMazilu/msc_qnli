john_rake_time_premise = 60
john_rake_time_hypothesis = 30
todd_rake_time_premise = 60
todd_rake_time_hypothesis = 60

# the hypothesis refers to the time it takes John and Todd to rake a lawn, mentioned in the premise
if john_rake_time_hypothesis >= john_rake_time_premise:
    # check if the time it takes John to rake a lawn in the hypothesis contradicts the premise
    label = "contradiction"
elif todd_rake_time_hypothesis!= todd_rake_time_premise:
    # check if the time it takes Todd to rake a lawn in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes John to rake a lawn
    # any time less than 'john_rake_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
