boys_premise = 200
girls_premise = 160
boys_hypothesis = 700
girls_hypothesis = 160

# the hypothesis refers to the number of boys and girls in the senior class, mentioned in the premise
if boys_premise + girls_premise!= boys_hypothesis + girls_hypothesis:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives an exact count of the number of boys and girls in the senior class
    # any number of boys and girls greater than or equal to the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
