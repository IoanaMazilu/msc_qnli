john_age_difference_premise = 2
john_age_difference_hypothesis = 2
years_premise = 5
years_hypothesis = 8

# the hypothesis talks about the age difference between John and Frank in a certain number of years, referenced also in the premise
if john_age_difference_hypothesis!= john_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
elif years_hypothesis <= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # the premise gives an exact age difference and a specific number of years
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
