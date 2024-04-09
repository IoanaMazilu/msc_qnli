boys_premise = 300
girls_premise = 240
hypothesis = 300, 240

# the hypothesis talks about the number of boys and girls in Addison High School's senior class
if hypothesis[0] <= boys_premise or hypothesis[1] <= girls_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boys_premise' and 'girls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys and girls
    # any number of boys and girls greater than the estimates but less than or equal to the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
