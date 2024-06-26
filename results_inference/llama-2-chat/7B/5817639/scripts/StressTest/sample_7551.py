boys_premise = 6
girls_premise = 4
boys_hypothesis = 2
girls_hypothesis = 4

# the hypothesis talks about the gender distribution in a group, referenced also in the premise
if boys_hypothesis <= boys_premise:
    # check if the hypothesis value contradicts the estimate of 'boys_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys,
    # any number of boys greater than 'boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

if girls_hypothesis <= girls_premise:
    # check if the hypothesis value contradicts the estimate of 'girls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of girls,
    # any number of girls greater than 'girls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
