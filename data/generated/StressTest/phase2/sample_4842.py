# Premise: Raji invests some money at the beginning, Lakshmi invests double the amount after 6 months, and Priya invests thrice the amount after 8 months.
# Hypothesis: Raji invests some money at the beginning, Lakshmi invests double the amount after more than 3 months, and Priya invests thrice the amount after 8 months.
# Golden Label: entailment

lakshmi_investment_time_premise = 6
lakshmi_investment_time_hypothesis = 3

# the hypothesis talks about the time Lakshmi invests her amount, which is also mentioned in the premise
if lakshmi_investment_time_hypothesis >= lakshmi_investment_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific time for Lakshmi's investment
    # any time less than 6 months is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
