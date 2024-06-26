rd_ranking_premise = 15
rd_ranking_hypothesis = 65

# the hypothesis talks about Veena's ranking in a class, referenced also in the premise
if rd_ranking_hypothesis <= rd_ranking_premise:
    # check if the hypothesis value contradicts the estimate of more than 'rd_ranking_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Veena's ranking
    # any ranking greater than 'rd_ranking_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
