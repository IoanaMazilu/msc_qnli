boys_premise = 300
girls_premise = 240
hypothesis = 300

# the hypothesis refers to the number of boys and girls in Addison High School's senior class
if hypothesis <= (boys_premise + girls_premise):
    # check if the hypothesis value contradicts the estimate of 'boys_premise' and 'girls_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of boys and girls, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
