john_age_multiple_premise = 3
john_age_multiple_hypothesis = 3
years_back_premise = 6
years_back_hypothesis = 2

# The hypothesis and premise refer to the age difference between John and Tom at different points in time.
if john_age_multiple_premise != john_age_multiple_hypothesis:
    # check if the multiple of age difference between John and Tom in the hypothesis contradicts the multiple in the premise
    label = "contradiction"
elif years_back_premise == years_back_hypothesis:
    # check if the number of years back in the hypothesis contradicts the number of years back in the premise
    label = "contradiction"
else:
    # the premise and hypothesis give the same relationship between John and Tom's age, but at different times
    # therefore, the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
