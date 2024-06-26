lakshmi_investment_time_premise = 5
lakshmi_investment_time_hypothesis = 6
muthu_investment_time_premise = 8
muthu_investment_time_hypothesis = 8

# the hypothesis talks about the time after which Lakshmi and Muthu make their investments, referenced also in the premise
if lakshmi_investment_time_hypothesis <= lakshmi_investment_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'lakshmi_investment_time_premise' months
    label = "contradiction"
elif muthu_investment_time_hypothesis != muthu_investment_time_premise:
    # check if the time after which Muthu invests in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
