john_rake_time_premise = 30
john_rake_time_hypothesis = 30
todd_rake_time_premise = 60
todd_rake_time_hypothesis = 60

# the hypothesis talks about the time it takes John and Todd to rake a lawn, referenced also in the premise
if john_rake_time_hypothesis >= john_rake_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_rake_time_premise'
    label = "contradiction"
elif todod_rake_time_hypothesis!= todod_rake_time_premise:
    # check if the number of raked lawns in the hypothesis contradicts the number of raked lawns reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
