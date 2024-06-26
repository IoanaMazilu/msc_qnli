men_premise = 100
men_hypothesis = 600

# the hypothesis refers to the number of men employed in the premise
if men_hypothesis <= men_premise:
    # check if the hypothesis value contradicts the estimate of'men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of men
    # any number of men greater than'men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
