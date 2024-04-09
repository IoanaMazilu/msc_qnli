# Define variables for the premise and hypothesis
monday_wednesday_friday_premise = 2
tuesday_thursday_premise = 5

# Define variables for the hypothesis
monday_wednesday_friday_hypothesis = 9

# Check if the hypothesis value contradicts the estimate of the premise
if monday_wednesday_friday_hypothesis <= monday_wednesday_friday_premise:
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of hours worked on Monday, Wednesday, and Friday
    # Any number of hours worked greater than'monday_wednesday_friday_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
