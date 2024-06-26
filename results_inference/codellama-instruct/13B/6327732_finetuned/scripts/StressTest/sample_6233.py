# define variables for the rates and the time
rate_bruce = 4
rate_anne = 4
time_premise = 4
time_hypothesis = 3

# check if the hypothesis value contradicts the premise value
if time_hypothesis <= time_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
