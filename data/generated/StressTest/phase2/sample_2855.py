# Premise: If Michael earned $363 last week, how many hours did he work?
# Hypothesis: If Michael earned $more than 363 last week, how many hours did he work?
# Golden Label: contradiction

earnings_premise = 363
earnings_hypothesis = 363

# the hypothesis talks about Michael's earnings last week, referenced also in the premise
if earnings_hypothesis < earnings_premise:
    # check if the hypothesis value contradicts the earnings in the premise
    label = "contradiction"
elif earnings_hypothesis == earnings_premise:
    # if hypothesis value is same as the premise it's entailment
    label = "entailment"
else:
    # the premise gives exact earnings of Michael
    # any earnings greater than 'earnings_premise' consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

