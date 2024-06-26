men_premise = 600
men_hypothesis = 100

# the hypothesis refers to the number of men employed by NHAI to build a highway, also mentioned in the premise
if men_hypothesis >= men_premise:
    # check if the number of men in the hypothesis contradicts the estimate of less than'men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of men
    # any number of men less than'men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
