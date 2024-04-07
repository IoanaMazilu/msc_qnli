# Premise: It takes John exactly 30 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Hypothesis: It takes John exactly 80 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn.
# Golden Label: contradiction

john_raking_time_premise = 30
john_raking_time_hypothesis = 80
todd_raking_time_premise = 60
todd_raking_time_hypothesis = 60

# the hypothesis refers to the raking time of John and Todd mentioned in the premise
if john_raking_time_premise != john_raking_time_hypothesis:
    # check if the raking time of John in the hypothesis contradicts the raking time of John mentioned in the premise
    label = "contradiction"
elif todd_raking_time_premise != todd_raking_time_hypothesis:
    # check if the raking time of Todd in the hypothesis contradicts the raking time of Todd mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

