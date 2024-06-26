anita_days = 18
indu_days = 27
geeta_days = 36

# the hypothesis refers to the total number of days required for the work, which is not explicitly mentioned in the premise
if anita_days + indu_days + geeta_days!= 58:
    # check if the total number of days in the hypothesis contradicts the sum of the days mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days required for the work
    # any number of days greater than the sum of the days mentioned in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
