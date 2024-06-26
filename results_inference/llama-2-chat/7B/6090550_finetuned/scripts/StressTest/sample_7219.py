y_premise = 30
y_hypothesis = 80

# the hypothesis talks about Lena's grade, which is also mentioned in the premise
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the estimate of more than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the grade
    # any grade greater than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
