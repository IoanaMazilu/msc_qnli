# Premise: Raman invests some money at the beginning, Lakshmi invests double the amount after 6 months, and Muthu invests thrice the amount after 8 months.
# Hypothesis: Raman invests some money at the beginning, Lakshmi invests double the amount after more than 5 months, and Muthu invests thrice the amount after 8 months.
# Golden Label: entailment

raman_investment_premise = 1
lakshmi_investment_premise = 2
muthu_investment_premise = 3
lakshmi_investment_time_premise = 6
muthu_investment_time_premise = 8

raman_investment_hypothesis = 1
lakshmi_investment_hypothesis = 2
muthu_investment_hypothesis = 3
lakshmi_investment_time_hypothesis = 5
muthu_investment_time_hypothesis = 8

# the hypothesis refers to the investments and timings mentioned in the premise
if raman_investment_premise != raman_investment_hypothesis or lakshmi_investment_premise != lakshmi_investment_hypothesis or muthu_investment_premise != muthu_investment_hypothesis:
    # check if the investments in the hypothesis contradict the investments in the premise
    label = "contradiction"
elif lakshmi_investment_time_hypothesis >= lakshmi_investment_time_premise or muthu_investment_time_hypothesis != muthu_investment_time_premise:
    # check if the investment timings in the hypothesis contradict the investment timings in the premise
    label = "contradiction"
else:
    # if the hypothesis investments and timings do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

