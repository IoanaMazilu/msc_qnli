anita_days = 18
indu_days = 27
geeta_days = 36

# the hypothesis talks about the number of days required for a piece of work
# the premise gives estimates for the number of days required for each person
if anita_days + indu_days + geeta_days < 38:
    # check if the sum of the estimates contradicts the hypothesis
    label = "contradiction"
elif anita_days + indu_days + geeta_days == 38:
    # check if the sum of the estimates is consistent with the hypothesis
    label = "entailment"
else:
    # the premise gives only estimates for the number of days required
    # any number of days greater than 38 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
