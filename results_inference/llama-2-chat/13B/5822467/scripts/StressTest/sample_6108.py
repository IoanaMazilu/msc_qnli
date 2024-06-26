level_1_graduates_premise = 15
level_less_4_graduates_hypothesis = 15

# the hypothesis refers to the percentage of sales staff with level less than 4 college education
if level_less_4_graduates_hypothesis <= level_1_graduates_premise:
    # check if the hypothesis value contradicts the estimate of 'level_1_graduates_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of sales staff with level 1 college education
    # any percentage less than or equal to 15% for sales staff with level less than 4 college education is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
