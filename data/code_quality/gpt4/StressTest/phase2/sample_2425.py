john_age_multiple = 3
past_years_premise = 1
past_years_hypothesis = 6

# The hypothesis and premise both discuss the relationship between John's and Tom's age in the past
# The premise specifies that John was 3 times as old as Tom more than "past_years_premise" ago
# The hypothesis specifies that John was 3 times as old as Tom "past_years_hypothesis" ago
if past_years_hypothesis <= past_years_premise:
    # Check if the number of years ago specified in the hypothesis contradicts the premise's claim of "more than past_years_premise" years
    label = "contradiction"
else:
    # If the number of years ago specified in the hypothesis is greater than past_years_premise, it does not contradict the premise
    # However, the premise does not provide enough information to explicitly entail the hypothesis
    label = "neutral"

print(label)
