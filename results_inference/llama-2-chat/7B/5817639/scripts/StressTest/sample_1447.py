% more_deaths_premise = 4
% more_deaths_hypothesis = 5
% remainder_left_premise = 85
% remainder_left_hypothesis = 85

# the hypothesis talks about the percentage of people who died and the percentage of people who left the village
if more_deaths_hypothesis <= more_deaths_premise:
    # check if the hypothesis value contradicts the estimate of more than'more_deaths_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who died
    # any number of people who died consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
