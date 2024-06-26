level_premise = 4
level_hypothesis = 1
percentage_premise = 15
percentage_hypothesis = 15

# the hypothesis refers to the level and percentage of college graduates in Amtek's sales staff mentioned in the premise
if level_hypothesis >= level_premise:
    # check if the level in the hypothesis contradicts the level in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the level of college graduates
    # any level less than 'level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
