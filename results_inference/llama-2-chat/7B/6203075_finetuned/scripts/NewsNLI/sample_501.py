cartons_recalled_premise = 2498
states_canada_premise = 19
deaths_cantaloupes_premise = 13
cartons_recalled_hypothesis = 2498
states_canada_hypothesis = 19
deaths_cantaloupes_hypothesis = 13

# the hypothesis and premise mention the number of cartons recalled and the states and Canada involved
if cartons_recalled_hypothesis!= cartons_recalled_premise:
    label = "contradiction"
elif states_canada_hypothesis!= states_canada_premise:
    label = "contradiction"
elif deaths_cantaloupes_hypothesis!= deaths_cantaloupes_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
