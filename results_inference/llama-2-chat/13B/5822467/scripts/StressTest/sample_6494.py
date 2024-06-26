percentage_premise = 3
months_premise = 4
amount_premise = 10000

# define variables for the hypothesis
percentage_hypothesis = 2
months_hypothesis = 4
amount_hypothesis = 10000

# calculate the amount owed after 4 years with the hypothesis
owing_hypothesis = amount_premise * (1 + percentage_hypothesis/100) ** months_hypothesis

# compare the amount owed with the premise
if owing_hypothesis <= amount_premise:
    # the hypothesis is consistent with the premise, neutral
    label = "neutral"
elif owing_hypothesis > amount_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise only gives an estimate, so the hypothesis is not explicitly entailed
    label = "neutral"

print(label)
