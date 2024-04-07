# Premise: In Parkin's company more than 20% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Hypothesis: In Parkin's company 60% of the employees earn less than $50,000 a year, 60% of the employees earn more than $40,000 a year, 11% of the employees earn $43,000 a year and 5% of the employees earn $49,000 a year.
# Golden Label: neutral

less_than_50000_premise = 20
less_than_50000_hypothesis = 60
more_than_40000_premise = 60
more_than_40000_hypothesis = 60
earn_43000_premise = 11
earn_43000_hypothesis = 11
earn_49000_premise = 5
earn_49000_hypothesis = 5

# the hypothesis refers to the same statistics about Parkin's company employees' earnings mentioned in the premise
if less_than_50000_hypothesis <= less_than_50000_premise:
    # check if the hypothesis estimate contradicts the premise estimate for employees earning less than $50,000
    label = "contradiction"
elif more_than_40000_hypothesis != more_than_40000_premise:
    # check if the estimate for employees earning more than $40,000 in the hypothesis contradicts the premise
    label = "contradiction"
elif earn_43000_hypothesis != earn_43000_premise:
    # check if the estimate for employees earning $43,000 in the hypothesis contradicts the premise
    label = "contradiction"
elif earn_49000_hypothesis != earn_49000_premise:
    # check if the estimate for employees earning $49,000 in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones
    label = "neutral"

print(label)

