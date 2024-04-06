# Premise: A restaurant served 6.0 cakes during lunch and 9.0 during dinner today.
# Hypothesis: 12.0 cakes were served today.
# Golden Label: contradiction

cakes_lunch_premise = 6.0
cakes_dinner_premise = 9.0
total_cakes_hypothesis = 12.0

# the hypothesis refers to the total number of cakes served, which are also mentioned in the premise
# compute the total number of cakes served in the premise
total_cakes_premise = cakes_lunch_premise + cakes_dinner_premise
if total_cakes_hypothesis != total_cakes_premise:
    # check if the total number of cakes in the hypothesis contradicts the number of cakes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

