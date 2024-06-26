dimes_premise_melanie = 7.0
dimes_given_by_dad = 8.0
dimes_given_by_mom = 4.0
total_dimes_premise = dimes_premise_melanie + dimes_given_by_dad + dimes_given_by_mom

# the hypothesis refers to the total number of dimes, which is also mentioned in the premise
# compute the total number of dimes in the premise
total_dimes_hypothesis = total_dimes_premise

if total_dimes_hypothesis!= total_dimes_premise:
    # check if the number of dimes in the hypothesis contradicts the number of dimes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
