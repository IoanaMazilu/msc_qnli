# Premise: Two dogsled teams raced across a 300 mile course in Wyoming.
# Hypothesis: Two dogsled teams raced across a less than 300 mile course in Wyoming.
# Golden Label: contradiction

course_length_premise = 300
course_length_hypothesis = 300

# the hypothesis talks about the length of a dogsled race course, referenced also in the premise
if course_length_hypothesis >= course_length_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)

