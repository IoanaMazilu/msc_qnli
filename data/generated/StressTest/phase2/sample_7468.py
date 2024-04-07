# Premise: Level-less than 7 college graduates account for 10% of Listco's sales staff.
# Hypothesis: Level-1 college graduates account for 10% of Listco's sales staff.
# Golden Label: neutral

level_premise = 7
level_hypothesis = 1
percentage_premise = 10
percentage_hypothesis = 10

# the hypothesis talks about the level of college graduates and their percentage in Listco's sales staff, referenced also in the premise
if level_hypothesis >= level_premise:
    # check if the hypothesis contradicts the premise of 'level_premise' being the maximum level
    label = "contradiction"
elif percentage_hypothesis != percentage_premise:
    # check if the percentages of college graduates in the hypothesis and premise contradict each other
    label = "contradiction"
else:
    # the premise gives an estimate for the level of college graduates
    # the level mentioned in the hypothesis is less than 'level_premise', hence it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

