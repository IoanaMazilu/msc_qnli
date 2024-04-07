# Premise: On a less than 80 mile course, Pat bicycled at an average rate of 30 miles per hour for the first 12 minutes and without a break, ran the rest of the distance at an average rate of 8 miles per hour.
# Hypothesis: On a 20 mile course, Pat bicycled at an average rate of 30 miles per hour for the first 12 minutes and without a break, ran the rest of the distance at an average rate of 8 miles per hour.
# Golden Label: neutral

course_distance_premise = 80
course_distance_hypothesis = 20
bicycle_speed = 30
bicycle_time = 12 / 60 # we convert the time from minutes to hours
run_speed = 8

# the hypothesis refers to the details of Pat's course, which are also mentioned in the premise
if course_distance_hypothesis >= course_distance_premise:
    # check if the course distance in the hypothesis contradicts the estimate of less than 'course_distance_premise'
    label = "contradiction"
elif bicycle_speed * bicycle_time + run_speed * (course_distance_hypothesis - bicycle_speed * bicycle_time) > course_distance_hypothesis:
    # check if the total distance covered by Pat in the hypothesis contradicts the hypothesis course distance
    label = "contradiction"
else:
    # the premise gives only an upper limit for the course distance
    # any course distance less than 'course_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

