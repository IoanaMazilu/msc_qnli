distance_premise = 40
distance_hypothesis = 80
speed_maxwell_premise = 4
speed_maxwell_hypothesis = 4
speed_brad_premise = 6
speed_brad_hypothesis = 6

# the hypothesis talks about the distance between homes and the speed of Maxwell and Brad, referenced also in the premise
if distance_hypothesis == distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_maxwell_hypothesis!= speed_maxwell_premise or speed_brad_hypothesis!= speed_brad_premise:
    # check if the speeds of Maxwell and Brad in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
