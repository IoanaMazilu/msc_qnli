unemployment_rate_premise = 7.8
jobs_added_premise = 114000

# define variables with representative names for the numerical entities in both inputs
unemployment_rate_hypothesis = 7.8
jobs_added_hypothesis = 114000

# extract all quantities as valid numbers (integers or floats)
unemployment_rate_premise = float(unemployment_rate_premise)
jobs_added_premise = int(jobs_added_premise)
unemployment_rate_hypothesis = float(unemployment_rate_hypothesis)
jobs_added_hypothesis = int(jobs_added_hypothesis)

# compare the variables
if unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the premise
    label = "contradiction"
elif jobs_added_hypothesis!= jobs_added_premise:
    # check if the number of jobs added in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same unemployment rate and number of jobs added
    # any comparison between the two is neutral
    label = "neutral"

print(label)
