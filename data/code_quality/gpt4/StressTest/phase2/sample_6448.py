years_premise = 8
years_hypothesis = 5

# the hypothesis talks about the number of years until John will be twice as old as Frank, referenced also in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_premise'
    label = "contradiction"
elif years_hypothesis < years_premise:
    # the premise gives an estimate for the number of years
    # the hypothesis number is less than the premise's estimate, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
