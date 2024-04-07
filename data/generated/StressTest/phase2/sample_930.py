# Premise: Rajeev invests some money at the beginning, Lakshmi invests double the amount after 6 months, and Muthu invests thrice the amount after 8 months.
# Hypothesis: Rajeev invests some money at the beginning, Lakshmi invests double the amount after more than 2 months, and Muthu invests thrice the amount after 8 months.
# Golden Label: entailment

lakshmi_investment_time_premise = 6
lakshmi_investment_time_hypothesis = 2
muthu_investment_time_premise = 8
muthu_investment_time_hypothesis = 8

# the hypothesis talks about the time at which Lakshmi and Muthu invest, referenced also in the premise
if lakshmi_investment_time_hypothesis > lakshmi_investment_time_premise:
    # check if the time at which Lakshmi invests in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif muthu_investment_time_hypothesis != muthu_investment_time_premise:
    # check if the time at which Muthu invests in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

