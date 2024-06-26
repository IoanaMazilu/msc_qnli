# From the premises
earn_less_50k_premise = 20
earn_more_40k_premise = 60
earn_43k_premise = 11
earn_49k_premise = 5

# From the hypothesis
earn_less_50k_hypothesis = 60
earn_more_40k_hypothesis = 60
earn_43k_hypothesis = 11
earn_49k_hypothesis = 5

# Compare the percentage of employees earning less than $50,000 a year
if earn_less_50k_hypothesis <= earn_less_50k_premise:
    label = "contradiction"
# Compare the percentage of employees earning more than $40,000 a year
elif earn_more_40k_hypothesis != earn_more_40k_premise:
    label = "contradiction"
# Compare the percentage of employees earning $43,000 a year
elif earn_43k_hypothesis != earn_43k_premise:
    label = "contradiction"
# Compare the percentage of employees earning $49,000 a year
elif earn_49k_hypothesis != earn_49k_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)