# Premise: Ajay bought less than 35 kg of dal at the rate of Rs 14.50 per kg and 10 kg at the rate of Rs 13 per kg.
# Hypothesis: Ajay bought 15 kg of dal at the rate of Rs 14.50 per kg and 10 kg at the rate of Rs 13 per kg.
# Golden Label: neutral

dal_bought_premise = 35
dal_bought_hypothesis = 15
dal_rate_premise = 14.50
dal_rate_hypothesis = 14.50
other_dal_bought_premise = 10
other_dal_bought_hypothesis = 10
other_dal_rate_premise = 13
other_dal_rate_hypothesis = 13

# the hypothesis refers to the amount and rate of dal bought which is also mentioned in the premise
if dal_bought_hypothesis > dal_bought_premise:
    # check if the amount of dal bought in the hypothesis contradicts the estimate of less than 'dal_bought_premise' 
    label = "contradiction"
elif dal_rate_hypothesis != dal_rate_premise:
    # check if the rate of dal in the hypothesis contradicts the rate of dal in the premise
    label = "contradiction"
elif other_dal_bought_hypothesis != other_dal_bought_premise:
    # check if the amount of other dal bought in the hypothesis contradicts the amount of other dal bought in the premise
    label = "contradiction"
elif other_dal_rate_hypothesis != other_dal_rate_premise:
    # check if the rate of other dal in the hypothesis contradicts the rate of other dal in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

