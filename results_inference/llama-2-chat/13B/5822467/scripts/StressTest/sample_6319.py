maddie_apples_premise = 7 - 2 # calculate the number of apples Maddie has left after giving 2 to Mike
hypothesis_apples = 4 - 2 # calculate the number of apples Maddie has left after giving 2 to Mike

# check if the hypothesis value contradicts the estimate of'maddie_apples_premise'
if hypothesis_apples <= maddie_apples_premise:
    label = "contradiction"
elif hypothesis_apples!= maddie_apples_premise:
    # check if the number of apples left in the hypothesis contradicts the number of apples left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
