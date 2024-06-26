first_speed_premise = 44
first_speed_hypothesis = 44
second_speed_premise = 60
second_speed_hypothesis = 60

# the hypothesis refers to the speeds mentioned in the premise
if first_speed_premise!= first_speed_hypothesis:
    # check if the first speed in the hypothesis contradicts the first speed reported in the premise
    label = "contradiction"
elif second_speed_hypothesis!= second_speed_premise:
    # check if the second speed in the hypothesis contradicts the second speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
