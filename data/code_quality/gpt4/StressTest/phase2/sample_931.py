lakshmi_investment_time_premise = 2
lakshmi_investment_time_hypothesis = 6
muthu_investment_time_premise = 8
muthu_investment_time_hypothesis = 8

# the hypothesis refers to the investment time of Lakshmi and Muthu mentioned in the premise
if lakshmi_investment_time_hypothesis <= lakshmi_investment_time_premise:
    # check if the investment time of Lakshmi in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif muthu_investment_time_hypothesis != muthu_investment_time_premise:
    # check if the investment time of Muthu in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
