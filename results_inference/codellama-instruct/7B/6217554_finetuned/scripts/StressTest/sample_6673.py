# define variables for the distances and speeds
distance_premise = 5
distance_hypothesis = 1
speed_premise_1 = 40
speed_premise_2 = 60
speed_hypothesis_1 = 40
speed_hypothesis_2 = 60

# check if the hypothesis values contradict the premise ones
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif speed_hypothesis_1!= speed_premise_1 or speed_hypothesis_2!= speed_premise_2:
    # check if the speeds in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
