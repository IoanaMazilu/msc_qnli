seniors_premise = 300
seniors_hypothesis = 500
cars_owned_premise = 0.5 * seniors_premise
cars_owned_hypothesis = 0.5 * seniors_hypothesis

# the hypothesis talks about the number of seniors and the percentage of them with cars
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of'seniors_premise'
    label = "contradiction"
elif cars_owned_hypothesis!= cars_owned_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
