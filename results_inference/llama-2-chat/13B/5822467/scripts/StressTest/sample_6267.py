deaths_premise = 10
deaths_hypothesis = 30
fearful_left_premise = 20

# the hypothesis refers to the percentage of deaths and the number of people who left the village
if deaths_hypothesis <= deaths_premise:
    # check if the estimate of 'deaths_hypothesis' contradicts the number of deaths reported in the premise
    label = "contradiction"
elif fearful_left_premise!= deaths_hypothesis:
    # check if the number of people who left the village contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
