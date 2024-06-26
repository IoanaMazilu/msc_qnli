course_length_premise = 20
course_length_hypothesis = 40
bicycle_speed_premise = 30
bicycle_speed_hypothesis = 30
bicycle_time_premise = 12/60  # Converted minutes to hours
bicycle_time_hypothesis = 12/60  # Converted minutes to hours
run_speed_premise = 8
run_speed_hypothesis = 8

# the hypothesis refers to the length of the course, the speed and duration of bicycling, and the speed of running mentioned in the premise

if (course_length_premise > course_length_hypothesis) or (bicycle_speed_premise != bicycle_speed_hypothesis) or (bicycle_time_premise != bicycle_time_hypothesis) or (run_speed_premise != run_speed_hypothesis):
    # check if any of the values or estimates in the hypothesis contradict the premise
    label = "contradiction"
elif course_length_premise < course_length_hypothesis:
    # if course_length_premise is less than course_length_hypothesis, it can be inferred that the hypothesis is an entailment
    label = "entailment"
else:
    # if none of the above conditions are met, we can conclude that the relation is neutral
    label = "neutral"

print(label)
