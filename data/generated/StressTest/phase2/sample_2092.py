# Premise: Two dogsled teams raced across a more than 200 mile course in Wyoming.
# Hypothesis: Two dogsled teams raced across a 300 mile course in Wyoming.
# Golden Label: neutral

course_length_premise = 200
course_length_hypothesis = 300

# the hypothesis talks about the length of a course, mentioned also in the premise
if course_length_hypothesis <= course_length_premise:
    # check if the hypothesis value contradicts the estimate of more than 'course_length_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the course
    # any length greater than 'course_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

