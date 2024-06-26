picked_pears_keith_premise = 47.0
picked_pears_mike_premise = 12.0
given_pears_keith_premise = 46.0
picked_pears_mike_hypothesis = 13.0

# the hypothesis talks about the number of pears left, which are also referenced in the premise
# compute the total number of pears Keith gave away
total_pears_keith_premise = given_pears_keith_premise + picked_pears_keith_premise
if picked_pears_mike_hypothesis!= total_pears_keith_premise:
    # check if the number of pears from the hypothesis contradicts the number of pears Keith gave away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
