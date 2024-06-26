men_premise = 600
men_hypothesis = 100

# the hypothesis talks about the number of men employed by NHAI, referenced also in the premise
if men_hypothesis >= men_premise:
    # check if the hypothesis value contradicts the estimate of less than'men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of men
    # any number of men less than'men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
