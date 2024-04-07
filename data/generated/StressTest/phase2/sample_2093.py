# Premise: Two dogsled teams raced across a 300 mile course in Wyoming.
# Hypothesis: Two dogsled teams raced across a more than 300 mile course in Wyoming.
# Golden Label: contradiction

course_length_premise = 300
course_length_hypothesis = 300

# the hypothesis talks about the length of the course in Wyoming, mentioned also in the premise
if course_length_hypothesis <= course_length_premise:
    # check if the hypothesis course length contradicts the premise course length
    label = "contradiction"
else:
    # if the hypothesis course length is greater than the premise course length, 
    # we cannot infer entailment because the premise does not provide information beyond 'course_length_premise'
    label = "neutral"

print(label)

