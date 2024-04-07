# Premise: John purchased more than 3 kg of apples at the rate of 70 per kg and 9 kg of banana at the rate of 55 per kg.
# Hypothesis: John purchased 8 kg of apples at the rate of 70 per kg and 9 kg of banana at the rate of 55 per kg.
# Golden Label: neutral

apples_purchased_premise = 3
apples_purchased_hypothesis = 8
apples_rate_premise = 70
apples_rate_hypothesis = 70
bananas_purchased_premise = 9
bananas_purchased_hypothesis = 9
bananas_rate_premise = 55
bananas_rate_hypothesis = 55

# the hypothesis refers to the number and rate of apples and bananas purchased mentioned in the premise
if apples_purchased_hypothesis <= apples_purchased_premise:
    # check if the number of apples purchased in the hypothesis contradicts the estimate of more than 'apples_purchased_premise'
    label = "contradiction"
elif apples_rate_hypothesis != apples_rate_premise:
    # check if the rate of apples in the hypothesis contradicts the rate of apples mentioned in the premise
    label = "contradiction"
elif bananas_purchased_hypothesis != bananas_purchased_premise:
    # check if the number of bananas purchased in the hypothesis contradicts the number of bananas purchased reported in the premise
    label = "contradiction"
elif bananas_rate_hypothesis != bananas_rate_premise:
    # check if the rate of bananas in the hypothesis contradicts the rate of bananas mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # exact number of apples in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

