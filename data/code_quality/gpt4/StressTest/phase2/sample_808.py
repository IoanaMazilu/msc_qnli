years_ago_premise = 7
years_ago_hypothesis = 5

# the hypothesis talks about a time in the past when Kate was 5 times as old as her Son, referenced also in the premise
if years_ago_hypothesis >= years_ago_premise:
    # check if the hypothesis time contradicts the estimate of less than 'years_ago_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for when Kate was 5 times as old as her Son
    # any time less than 'years_ago_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
