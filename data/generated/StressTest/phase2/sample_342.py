# Premise: It takes John exactly 30 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Hypothesis: It takes John exactly more than 10 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Golden Label: entailment

john_time_premise = 30
john_time_hypothesis = 10
todd_time_premise = 60
todd_time_hypothesis = 60

# the hypothesis refers to the time it takes for John and Todd to rake a lawn, which is also mentioned in the premise
if john_time_premise <= john_time_hypothesis:
    # check if the estimate of 'john_time_hypothesis' contradicts the exact time it takes for John in the premise
    label = "contradiction"
elif todd_time_premise != todd_time_hypothesis:
    # check if the time it takes for Todd in the hypothesis contradicts the exact time it takes for Todd in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

