gallons_premise = 20.0
gallons_hypothesis = 4.0 * 5.0

# the hypothesis refers to the number of gas cans, which are also mentioned in the premise
# compute the total number of gas cans in the premise
total_cans_premise = gallons_premise / gallons_hypothesis

if total_cans_premise!= 4.0:
    # check if the number of gas cans in the hypothesis contradicts the number of gas cans from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
