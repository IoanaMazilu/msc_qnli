# Premise: The total of the ages of Amar, Akbar and Anthony is 66 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is less than 66 years.
# Golden Label: contradiction

total_age_premise = 66
total_age_hypothesis = 66

# the hypothesis talks about the total age of Amar, Akbar and Anthony, referenced also in the premise
if total_age_hypothesis >= total_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact total for the ages
    # any total less than 'total_age_premise' contradicts the premise
    label = "contradiction"

print(label)

