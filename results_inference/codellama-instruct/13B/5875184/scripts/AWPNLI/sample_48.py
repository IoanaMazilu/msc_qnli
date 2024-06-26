premise_men = 14797.0
premise_women = 4969.0
hypothesis = 19766.0

# the hypothesis refers to the total number of bathing suits available, which is the sum of the number of bathing suits for men and women
# compute the total number of bathing suits available from the premise
total_premise = premise_men + premise_women
if total_premise!= hypothesis:
    # check if the number of bathing suits in the hypothesis contradicts the number of bathing suits from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
