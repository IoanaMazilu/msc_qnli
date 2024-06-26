lakshmi_investment_time_premise = 3
lakshmi_investment_time_hypothesis = 6
priya_investment_time_premise = 8
priya_investment_time_hypothesis = 8

# the hypothesis talks about the time when Lakshmi and Priya invested, referenced also in the premise
if lakshmi_investment_time_hypothesis <= lakshmi_investment_time_premise:
    # check if the time of Lakshmi's investment in the hypothesis contradicts the time given in the premise
    label = "contradiction"
elif priya_investment_time_hypothesis != priya_investment_time_premise:
    # check if the time of Priya's investment in the hypothesis contradicts the time given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and times do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
