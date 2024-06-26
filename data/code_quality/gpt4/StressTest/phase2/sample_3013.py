john_speed_premise = 78
john_speed_hypothesis = 48
harry_speed_premise = 72
harry_speed_hypothesis = 72
john_time = 20
harry_time = 15

# the hypothesis refers to the speeds of John and Harry when crossing a field, which are also mentioned in the premise
if john_speed_hypothesis >= john_speed_premise:
    # check if the speed of John in the hypothesis contradicts the premise, where his speed is less than 'john_speed_premise'
    label = "contradiction"
elif harry_speed_hypothesis != harry_speed_premise:
    # check if the speed of Harry in the hypothesis contradicts the speed of Harry reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
