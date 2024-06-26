peanuts_premise = 30
peanuts_added_premise = 8
peanuts_hypothesis = 10
peanuts_added_hypothesis = 8

# The hypothesis refers to the same situation as the premise but with a different initial number of peanuts
if peanuts_hypothesis >= peanuts_premise:
    # Check if the initial number of peanuts in the hypothesis contradicts the estimate of less than 'peanuts_premise'
    label = "contradiction"
elif peanuts_added_hypothesis != peanuts_added_premise:
    # Check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the initial number of peanuts
    # Any number of peanuts less than 'peanuts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
