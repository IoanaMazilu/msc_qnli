boys_premise = 400
boys_hypothesis = 300
girls_premise = 240
girls_hypothesis = 240

# the hypothesis refers to the number of boys and girls in the senior class mentioned in the premise
if boys_hypothesis >= boys_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of less than 'boys_premise'
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys less than 'boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
