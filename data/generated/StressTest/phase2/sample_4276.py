# Premise: If Michael earned $less than 652 last week, how many hours did he work?
# Hypothesis: If Michael earned $352 last week, how many hours did he work?
# Golden Label: neutral

earnings_premise = 652
earnings_hypothesis = 352

# the hypothesis talks about Michael's earnings, referenced also in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the hypothesis value contradicts the estimate of less than 'earnings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the earnings
    # any earnings less than 'earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

