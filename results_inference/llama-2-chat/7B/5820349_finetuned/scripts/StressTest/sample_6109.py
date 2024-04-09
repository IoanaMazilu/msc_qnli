level_premise = 4
level_hypothesis = 1
percentage_premise = 15
percentage_hypothesis = 15

# the hypothesis talks about the level of college graduates and their percentage in Amtek's sales staff, referenced also in the premise
if level_hypothesis >= level_premise:
    # check if the hypothesis value contradicts the estimate of less than 'level_premise'
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of college graduates in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the level of college graduates
    # any level less than 'level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
