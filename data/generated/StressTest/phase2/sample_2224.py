# Premise: In less than 5979 approximately 1/3 of the 38.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In 1979 approximately 1/3 of the 38.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: neutral

year_premise = 5979
year_hypothesis = 1979
passengers_premise = 38.3
passengers_hypothesis = 38.3

# the hypothesis refers to the year and the number of passengers, both mentioned in the premise
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the estimate of 'less than year_premise'
    label = "contradiction"
elif passengers_hypothesis != passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, the relation remains neutral as 
    # the premise doesn't provide an exact year to entail the hypothesis year.
    label = "neutral"

print(label)

