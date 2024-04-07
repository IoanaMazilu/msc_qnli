# Premise: Raman invests some money at the beginning, Lakshmi invests double the amount after 6 months, and Muthu invests thrice the amount after 8 months.
# Hypothesis: Raman invests some money at the beginning, Lakshmi invests double the amount after 8 months, and Muthu invests thrice the amount after 8 months.
# Golden Label: contradiction

raman_investment_premise = 1
lakshmi_investment_premise = 2 * raman_investment_premise
lakshmi_investment_time_premise = 6
muthu_investment_premise = 3 * raman_investment_premise
muthu_investment_time_premise = 8

raman_investment_hypothesis = 1
lakshmi_investment_hypothesis = 2 * raman_investment_hypothesis
lakshmi_investment_time_hypothesis = 8
muthu_investment_hypothesis = 3 * raman_investment_hypothesis
muthu_investment_time_hypothesis = 8

# the hypothesis talks about the investments of Raman, Lakshmi, and Muthu, referenced also in the premise
if lakshmi_investment_hypothesis != lakshmi_investment_premise or muthu_investment_hypothesis != muthu_investment_premise:
    # check if the amounts invested by Lakshmi or Muthu in the hypothesis contradict the amounts mentioned in the premise
    label = "contradiction"
elif lakshmi_investment_time_hypothesis != lakshmi_investment_time_premise or muthu_investment_time_hypothesis != muthu_investment_time_premise:
    # check if the investment times of Lakshmi or Muthu in the hypothesis contradict the times mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

