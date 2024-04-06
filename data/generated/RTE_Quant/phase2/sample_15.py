# Premise: The American computer company Apple has reached 78 percent increase in its profits during the last quarter, which ended December 30, 2006.
# Hypothesis: Apple's profits rose by 78 percent during the last quarter of 2006.
# Golden Label: entailment

profit_increase_percentage_premise = 78
profit_increase_percentage_hypothesis = 78
quarter_end_year_premise = 2006
quarter_end_year_hypothesis = 2006

# the hypothesis talks about the percent increase in profits that Apple has experienced in a given quarter of a year
# first we check if the profit increase percentage from the hypothesis contradicts the percent increase in profits from the premise
if profit_increase_percentage_hypothesis != profit_increase_percentage_premise:
    label = "contradiction"
# next we check if the quarter end year from the hypothesis contradicts the quarter end year from the premise
elif quarter_end_year_hypothesis != quarter_end_year_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

