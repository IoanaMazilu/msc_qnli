top_percentage_premise = 0.1
bottom_percentage_premise = 90
top_percentage_hypothesis = 0.1
bottom_percentage_hypothesis = 90

# the hypothesis and premise mention the distribution of wealth between the top and bottom percentages of the population
if top_percentage_premise != top_percentage_hypothesis or bottom_percentage_premise != bottom_percentage_hypothesis:
    # check if the top or bottom percentages in the hypothesis contradict the percentages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
