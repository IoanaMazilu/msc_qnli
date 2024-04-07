# Premise: In less than 6979 approximately 1/3 of the 32.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In 1979 approximately 1/3 of the 32.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: neutral

year_premise = 6979
year_hypothesis = 1979
passengers_premise = 32.3 * 10**6
passengers_hypothesis = 32.3 * 10**6
airport_percentage_premise = 1/3
airport_percentage_hypothesis = 1/3

# the hypothesis talks about the number of passengers and the year referenced also in the premise
if year_hypothesis >= year_premise:
    # check if the hypothesis year contradicts the estimate of less than 'year_premise'
    label = "contradiction"
elif passengers_hypothesis != passengers_premise or airport_percentage_hypothesis != airport_percentage_premise:
    # check if the number of passengers or the percentage in the hypothesis contradicts the numbers reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the year
    # any year less than 'year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

