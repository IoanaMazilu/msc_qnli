course_length_premise = 300
course_length_hypothesis = 800

# the hypothesis refers to the length of the course in the premise
if course_length_premise > course_length_hypothesis:
    # check if the length of the course in the premise contradicts the estimate of less than 'course_length_hypothesis'
    label = "contradiction"
else:
    # if the course length in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
