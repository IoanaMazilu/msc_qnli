pounds_premise = 45.0
bags_hypothesis = 1.4

# the hypothesis refers to the number of bags, which is also mentioned in the premise
# compute the total number of pounds of oranges in the premise
total_pounds_premise = pounds_premise * bags_hypothesis

# check if the number of bags in the hypothesis contradicts the number of bags in the premise
if bags_hypothesis!= math.ceil(pounds_premise / 23.0):
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
