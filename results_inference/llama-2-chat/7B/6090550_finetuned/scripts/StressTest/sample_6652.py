y_premise = 88
x_hypothesis = 18

# the hypothesis talks about the number of apples Maddie has, which is also mentioned in the premise
if x_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the estimate of less than 'y_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples less than 'y_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
