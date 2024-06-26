year_premise = 3997
year_hypothesis = 1997
additional_investment = 10000
rakesh_investment = 35000

# the hypothesis talks about the year of investment and the investment amounts, all referenced also in the premise
if year_hypothesis >= year_premise:
    # check if the hypothesis year contradicts the estimate of less than 'year_premise'
    label = "contradiction"
elif additional_investment != 10000 or rakesh_investment != 35000:
    # check if the investment amounts contradicts those in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the year of investment
    # any year less than 'year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
