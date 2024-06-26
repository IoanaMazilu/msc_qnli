cartons_recalled_premise = 2498
states_canada_premise = 19

# The hypothesis refers to the same bacteria that caused 13 deaths from tainted cantaloupes, which is also mentioned in the premise
# However, the hypothesis does not mention the number of cartons recalled or the states/Canada involved, which are mentioned in the premise

if cartons_recalled_premise!= 2498 or states_canada_premise!= 19:
    label = "contradiction"
else:
    label = "neutral"

print(label)
