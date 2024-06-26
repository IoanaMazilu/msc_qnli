people_premise = 219.0
sandwiches_per_person_premise = 3.0
total_sandwiches_hypothesis = 657.0

# the hypothesis refers to the total number of sandwiches, which are also mentioned in the premise
# compute the total number of sandwiches in the premise
total_sandwiches_premise = people_premise * sandwiches_per_person_premise
if total_sandwiches_hypothesis != total_sandwiches_premise:
    # check if the total number of sandwiches in the hypothesis contradicts the number of sandwiches from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)