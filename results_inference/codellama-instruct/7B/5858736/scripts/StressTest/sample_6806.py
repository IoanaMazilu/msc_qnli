premise_start_time = 0
premise_distance = 31
hypothesis_start_time = 0
hypothesis_distance = 61

# the hypothesis refers to the time and distance traveled by Yolanda and Bob
if hypothesis_start_time <= premise_start_time:
    # check if the estimate of 'hypothesis_start_time' contradicts the time reported in the premise
    label = "contradiction"
elif hypothesis_distance <= premise_distance:
    # check if the estimate of 'hypothesis_distance' contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
