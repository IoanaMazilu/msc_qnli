# Premise: On a less than 40 mile course, Bil bicycled at an average rate of 30 miles per hour for the first 12 minutes and without a break, ran the rest of the distance at an average rate of 8 miles per hour.
# Hypothesis: On a 20 mile course, Bil bicycled at an average rate of 30 miles per hour for the first 12 minutes and without a break, ran the rest of the distance at an average rate of 8 miles per hour.
# Golden Label: neutral

course_distance_premise = 40
course_distance_hypothesis = 20
bicycle_speed = 30
running_speed = 8
bicycle_time = 12 / 60 # convert minutes to hours

# calculate the distances covered by bicycle and by running in both premise and hypothesis
bicycle_distance_premise = bicycle_speed * bicycle_time
running_distance_premise = course_distance_premise - bicycle_distance_premise

bicycle_distance_hypothesis = bicycle_speed * bicycle_time
running_distance_hypothesis = course_distance_hypothesis - bicycle_distance_hypothesis

# the hypothesis refers to the course distance, the bicycling and running distances in the premise
if course_distance_hypothesis > course_distance_premise:
    # check if the course distance in the hypothesis contradicts the course distance in the premise
    label = "contradiction"
elif running_distance_hypothesis > running_distance_premise or bicycle_distance_hypothesis > bicycle_distance_premise:
    # check if the distances covered by running and bicycling in the hypothesis contradict the distances in the premise
    label = "contradiction"
elif running_distance_hypothesis < running_distance_premise and bicycle_distance_hypothesis < bicycle_distance_premise:
    # if the distances in the hypothesis are less than the distances in the premise, we can infer entailment
    label = "entailment"
else:
    # if the distances in the hypothesis do not contradict the distances in the premise, but cannot be fully and explicitly entailed from the premise, we infer neutrality
    label = "neutral"

print(label)

