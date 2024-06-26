pens_rihanna_premise = 550
pens_rihanna_hypothesis = 150

# the hypothesis refers to the number of pens Rihanna brought home, which is also mentioned in the premise
if pens_rihanna_hypothesis >= pens_rihanna_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pens_rihanna_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pens
    # any number of pens less than 'pens_rihanna_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
