level_premise = 7
level_hypothesis = 1
percentage_premise = 10
percentage_hypothesis = 10

# the hypothesis refers to the level and percentage of college graduates in Listco's sales staff mentioned in the premise
if level_hypothesis >= level_premise:
    # check if the hypothesis level contradicts the premise level
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only a maximum level for the college graduates
    # any level less than 'level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)