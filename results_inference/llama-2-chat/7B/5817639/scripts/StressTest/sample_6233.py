# Define variables for the premise and hypothesis
bruce_cleaning_rate_premise = 2
anne_cleaning_rate_premise = 3

bruce_cleaning_rate_hypothesis = 3
anne_cleaning_rate_hypothesis = 3

# Check if the hypothesis value contradicts the estimate of the premise
if bruce_cleaning_rate_hypothesis <= bruce_cleaning_rate_premise:
    label = "contradiction"
elif anne_cleaning_rate_hypothesis <= anne_cleaning_rate_premise:
    label = "contradiction"
else:
    # The premise gives an estimate for the number of hours it takes Bruce and Anne to clean the house working separately
    # Any number of hours that Bruce and Anne can clean the house in working together is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
