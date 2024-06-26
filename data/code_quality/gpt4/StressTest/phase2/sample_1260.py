vikas_mowing_time_premise = 8
vishal_mowing_time_premise = 12
vikas_mowing_time_hypothesis = 1
vishal_mowing_time_hypothesis = 12

# the hypothesis refers to the time Vikas and Vishal need to mow a field, as stated in the premise
if vikas_mowing_time_hypothesis >= vikas_mowing_time_premise:
    # check if the 'vikas_mowing_time_hypothesis' contradicts the time Vikas needs in the premise
    label = "contradiction"
elif vishal_mowing_time_hypothesis != vishal_mowing_time_premise:
    # check if the 'vishal_mowing_time_hypothesis' contradicts the time Vishal needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
