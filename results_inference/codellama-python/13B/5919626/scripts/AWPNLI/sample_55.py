gems_premise = 5155.0
gems_hypothesis = 5108.0
diamonds_premise = 45.0
rubies_premise = gems_premise - diamonds_premise

# the hypothesis talks about the number of rubies, which are also referenced in the premise
# find the total number of rubies from the premise 
total_rubies_premise = rubies_premise
if gems_hypothesis >= total_rubies_premise:
    # check if the total rubies from the hypothesis contradict the estimate of less than 'rubies_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
