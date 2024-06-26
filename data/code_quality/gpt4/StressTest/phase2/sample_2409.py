course_length_premise = 300
course_length_hypothesis = 100

# the hypothesis refers to the length of the course mentioned in the premise
if course_length_premise < course_length_hypothesis:
    # check if the hypothesis contradicts the course length in the premise
    label = "contradiction"
else:
    # if the hypothesized course length does not contradict the premise, it can be inferred as entailment
    label = "entailment"

print(label)
