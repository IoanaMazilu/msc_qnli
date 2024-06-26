john_rake_time_premise = 30
john_rake_time_hypothesis = 30
todd_rake_time_premise = 60
todd_rake_time_hypothesis = 60

# the hypothesis refers to the time it takes for John and Todd to rake a lawn
if john_rake_time_hypothesis > john_rake_time_premise:
    # checking if the time it takes John to rake the lawn contradicts the premise
    label = "contradiction"
elif todd_rake_time_hypothesis != todd_rake_time_premise:
    # checking if the time it takes Todd to rake the lawn contradicts the premise
    label = "contradiction"
else:
    # if both the times mentioned in the hypothesis do not contradict the ones in the premise, we infer entailment
    label = "entailment"

print(label)
