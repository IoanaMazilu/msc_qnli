candy_first_night_premise = 25.0
candy_given_premise = 40.0
total_candy_premise = 47.0
total_candy_hypothesis = 65.0

# the hypothesis refers to the total number of candy, which is also mentioned in the premise
# compute the total number of candy in the premise
total_candy_premise = candy_first_night_premise + candy_given_premise + total_candy_premise
if total_candy_hypothesis!= total_candy_premise:
    # check if the number of candy in the hypothesis contradicts the number of candy from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
