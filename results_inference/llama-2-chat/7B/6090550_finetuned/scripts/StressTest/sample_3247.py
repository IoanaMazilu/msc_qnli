y_premise = 50
y_hypothesis = 90

# the hypothesis talks about the number of students representing x percent of the boys at Jones Elementary School, referenced also in the premise
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the estimate of more than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students greater than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
