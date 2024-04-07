# Premise: Two dogsled teams raced across a 300 mile course in Wyoming.
# Hypothesis: Two dogsled teams raced across a more than 200 mile course in Wyoming.
# Golden Label: entailment

course_length_premise = 300
course_length_hypothesis = 200

# the hypothesis refers to the course length mentioned in the premise
if course_length_premise < course_length_hypothesis:
    # check if the premise course length contradicts the estimate of more than 'course_length_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

