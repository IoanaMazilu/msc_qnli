dimes_premise = 7.0
dimes_given_by_dad = 8.0
dimes_given_by_mom = 4.0
total_dimes_hypothesis = 18.0

# compute the total number of dimes in the premise
total_dimes_premise = dimes_premise + dimes_given_by_dad + dimes_given_by_mom

if total_dimes_hypothesis > total_dimes_premise:
    # check if the number of dimes in the hypothesis contradicts the number of dimes from the premise
    label = "contradiction"
elif total_dimes_hypothesis < total_dimes_premise:
    # check if the number of dimes in the hypothesis is less than the number of dimes from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
