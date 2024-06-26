course_distance_premise = 20
course_distance_hypothesis = 40
bicycle_speed_premise = 30
bicycle_speed_hypothesis = 30
running_speed_premise = 8
running_speed_hypothesis = 8
bicycle_time_premise = 12
bicycle_time_hypothesis = 12

# the hypothesis refers to the same situation described in the premise, but with different total course distance
if course_distance_hypothesis != course_distance_premise:
    # check if the total course distance in the hypothesis contradicts the total course distance reported in the premise
    label = "contradiction"
elif bicycle_speed_hypothesis != bicycle_speed_premise or running_speed_hypothesis != running_speed_premise or bicycle_time_hypothesis != bicycle_time_premise:
    # check if any of the other quantities in the hypothesis contradict the corresponding quantities reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
