course_distance_premise = 100
course_distance_hypothesis = 300

# the hypothesis refers to the distance of the course mentioned in the premise
if course_distance_premise >= course_distance_hypothesis:
    # check if the estimate of 'course_distance_hypothesis' contradicts the distance of the course in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
