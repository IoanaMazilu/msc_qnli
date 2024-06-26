course_length_premise = 300
course_length_hypothesis = 400

# the hypothesis refers to the length of the course mentioned in the premise
if course_length_hypothesis < course_length_premise:
    # check if the estimate of 'course_length_hypothesis' contradicts the length of the course in the premise
    label = "contradiction"
else:
    # if the hypothesis estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
