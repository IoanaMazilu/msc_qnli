# Premise: less than 8887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Hypothesis: 5887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Golden Label: neutral

divided_amount_premise = 8887
divided_amount_hypothesis = 5887

# The hypothesis talks about the amount divided between Shyam and Ram, which is also referenced in the premise
if divided_amount_hypothesis >= divided_amount_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'divided_amount_premise'
    label = "contradiction"
elif divided_amount_hypothesis < divided_amount_premise:
    # The premise gives only an estimate for the amount divided
    # Any amount less than 'divided_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    label = "contradiction"

print(label)

