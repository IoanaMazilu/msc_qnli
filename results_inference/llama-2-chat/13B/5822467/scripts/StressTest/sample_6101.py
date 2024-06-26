days_mary_premise = 16
days_mary_hypothesis = 76

# the hypothesis talks about the number of days required to complete a task alone, referenced also in the premise
if days_mary_hypothesis <= days_mary_premise:
    # check if the hypothesis value contradicts the estimate of 'days_mary_premise'
    label = "contradiction"
elif days_mary_premise == days_mary_hypothesis:
    # the premise and hypothesis values are the same, no contradiction or entailment
    label = "neutral"
else:
    # the premise gives an estimate for the number of days required to complete a task alone
    # any number of days greater than 'days_mary_premise' contradicts the premise
    label = "contradiction"

print(label)
