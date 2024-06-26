girls_premise = 2
boys_premise = 2

# the hypothesis talks about the number of girls and boys in a date, referenced also in the premise
if girls_hypothesis <= girls_premise:
    # check if the hypothesis value contradicts the estimate of less than 'girls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of girls
    # any number of girls greater than 'girls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
