rd_premise = 65
rd_hypothesis = 15

# the hypothesis talks about Veena's ranking in a class, referenced also in the premise
if rd_hypothesis <= rd_premise:
    # check if the hypothesis value contradicts the estimate of Veena's ranking in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Veena's ranking
    # any ranking greater than 'rd_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
