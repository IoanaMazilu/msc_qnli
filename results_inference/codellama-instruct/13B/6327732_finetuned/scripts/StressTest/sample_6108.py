level_premise = 15
level_hypothesis = 4

# the hypothesis talks about the level of education required for Amtek's sales staff
# the premise mentions a percentage of the total sales staff, but does not provide a specific number
if level_hypothesis <= level_premise:
    # check if the hypothesis value contradicts the estimate of more than 'level_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of sales staff with a level of education
    # any percentage greater than 'level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
