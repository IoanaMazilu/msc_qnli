pears_premise = 47.0
pears_given_away_premise = 46.0
pears_hypothesis = 13.0

# compute the total number of pears picked by Keith in the premise
total_pears_premise = pears_premise + pears_given_away_premise

if pears_hypothesis > total_pears_premise:
    # check if the number of pears in the hypothesis contradicts the number of pears from the premise
    label = "contradiction"
elif pears_hypothesis < total_pears_premise:
    # check if the number of pears in the hypothesis is less than the number of pears from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
