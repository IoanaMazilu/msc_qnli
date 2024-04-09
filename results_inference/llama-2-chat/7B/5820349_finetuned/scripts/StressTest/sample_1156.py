year_premise = 2979
year_hypothesis = 1979
passengers_premise = 37.3
passengers_hypothesis = 37.3

# the hypothesis talks about the year and the number of passengers at Kennedy Airport, referenced also in the premise
if year_hypothesis >= year_premise:
    # check if the year in the hypothesis contradicts the estimate of less than 'year_premise'
    label = "contradiction"
elif passengers_hypothesis!= passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the year
    # any year less than 'year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
