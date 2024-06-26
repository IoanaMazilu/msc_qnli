boys_premise = 3
boys_hypothesis = 6
girls_premise = 4
girls_hypothesis = 4

# the hypothesis talks about the number of boys and girls in a group, also mentioned in the premise
if boys_hypothesis <= boys_premise:
    # check if the number of boys in the hypothesis contradicts the premise estimate of more than 'boys_premise' boys
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys and an exact number of girls
    # any number of boys greater than 'boys_premise' and equal to 'girls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
