# Premise: Two dogsled teams raced across a 300 mile course in Wyoming.
# Hypothesis: Two dogsled teams raced across a 800 mile course in Wyoming.
# Golden Label: contradiction

course_length_premise = 300
course_length_hypothesis = 800

# the hypothesis refers to the length of a course mentioned in the premise
if course_length_hypothesis != course_length_premise:
    # check if the length of the course in the hypothesis contradicts the length of the course reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

