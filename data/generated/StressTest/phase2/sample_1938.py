# Premise: It takes John exactly 30 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Hypothesis: It takes John exactly less than 60 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Golden Label: entailment

john_rake_time_premise = 30
john_rake_time_hypothesis = 60
todd_rake_time_premise = 60
todd_rake_time_hypothesis = 60

# the hypothesis refers to the time it takes John and Todd to rake a lawn, as mentioned in the premise
if john_rake_time_hypothesis <= john_rake_time_premise:
    # check if the hypothesis value contradicts the exact time 'john_rake_time_premise' that John takes to rake a lawn
    label = "contradiction"
elif todd_rake_time_hypothesis != todd_rake_time_premise:
    # check if the time Todd takes to rake a lawn in the hypothesis contradicts the time in the premise
    label = "contradiction"
elif john_rake_time_hypothesis > john_rake_time_premise:
    # the hypothesis that John takes less than 'john_rake_time_hypothesis' to rake the lawn can be entailed from the premise
    label = "entailment"
else:
    # other cases would mean a neutral relation
    label = "neutral"

print(label)

