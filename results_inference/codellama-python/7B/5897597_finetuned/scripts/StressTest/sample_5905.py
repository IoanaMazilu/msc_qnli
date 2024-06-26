# Defining the variables
cookies_eaten_by_michael_premise = 7/8
cookies_eaten_by_michael_hypothesis = 1/8
cookies_eaten_by_steve_premise = 1/2
cookies_eaten_by_steve_hypothesis = 1/2
cookies_eaten_more_than_michael_premise = 150
cookies_eaten_more_than_michael_hypothesis = 150

# The hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler, mentioned in the premise
if cookies_eaten_by_michael_hypothesis >= cookies_eaten_by_michael_premise:
    # Check if the estimate of 'cookies_eaten_by_michael_hypothesis' contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif cookies_eaten_by_steve_hypothesis!= cookies_eaten_by_steve_premise:
    # Check if the number of cookies eaten by Steve in the hypothesis contradicts the number of cookies eaten by Steve in the premise
    label = "contradiction"
elif cookies_eaten_more_than_michael_hypothesis!= cookies_eaten_more_than_michael_premise:
    # Check if the number of cookies eaten by Tyler in the hypothesis contradicts the number of cookies eaten by Tyler in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of cookies eaten by Michael
    # Any number of cookies less than 'cookies_eaten_by_michael_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
