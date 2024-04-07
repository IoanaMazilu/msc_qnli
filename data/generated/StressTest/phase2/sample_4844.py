# Premise: Raji invests some money at the beginning, Lakshmi invests double the amount after 6 months, and Priya invests thrice the amount after 8 months.
# Hypothesis: Raji invests some money at the beginning, Lakshmi invests double the amount after 7 months, and Priya invests thrice the amount after 8 months.
# Golden Label: contradiction

raji_investment_time_premise = 0
lakshmi_investment_time_premise = 6
priya_investment_time_premise = 8

raji_investment_time_hypothesis = 0
lakshmi_investment_time_hypothesis = 7
priya_investment_time_hypothesis = 8

# the hypothesis talks about the investment times of Raji, Lakshmi, and Priya, which is also referenced in the premise
if raji_investment_time_hypothesis != raji_investment_time_premise:
    # check if the investment time of Raji in the hypothesis contradicts the premise
    label = "contradiction"
elif lakshmi_investment_time_hypothesis != lakshmi_investment_time_premise:
    # check if the investment time of Lakshmi in the hypothesis contradicts the premise
    label = "contradiction"
elif priya_investment_time_hypothesis != priya_investment_time_premise:
    # check if the investment time of Priya in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

