# Premise: Ayisha's father's age will be twice Shankar's age after less than 80 years.
# Hypothesis: Ayisha's father's age will be twice Shankar's age after 10 years.
# Golden Label: neutral

future_years_premise = 80
future_years_hypothesis = 10

# the hypothesis refers to the future years after which Ayisha's father's age will be twice Shankar's age, also mentioned in the premise
if future_years_hypothesis >= future_years_premise:
    # check if the 'future_years_hypothesis' contradicts the estimate of less than 'future_years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of future years
    # any number of years less than 'future_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

