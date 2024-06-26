girls_premise = 1
girls_hypothesis = 2

# the hypothesis is referring to the number of girls going on a date with boys, also referenced in the premise
if girls_hypothesis <= girls_premise:
    # check if the number of girls in the hypothesis contradicts the estimate of more than 'girls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of girls
    # any number of girls greater than 'girls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
