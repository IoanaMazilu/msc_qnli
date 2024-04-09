students_premise = 312
students_hypothesis = 212

# the hypothesis talks about the number of students studying different topics, referenced also in the premise
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of more than'students_premise' studying those topics
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying each topic
    # any number of students studying those topics greater than'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
