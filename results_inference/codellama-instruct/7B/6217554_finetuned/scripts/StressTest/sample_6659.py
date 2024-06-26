Karen_speed_premise = 60
Tom_speed_premise = 45
Karen_speed_hypothesis = 70
Tom_speed_hypothesis = 45

# the hypothesis talks about the average speed of Karen and Tom, referenced also in the premise
if Karen_speed_hypothesis!= Karen_speed_premise:
    # check if the average speed of Karen in the hypothesis contradicts the average speed of Karen reported in the premise
    label = "contradiction"
elif Tom_speed_hypothesis!= Tom_speed_premise:
    # check if the average speed of Tom in the hypothesis contradicts the average speed of Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
