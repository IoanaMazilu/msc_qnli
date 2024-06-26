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
