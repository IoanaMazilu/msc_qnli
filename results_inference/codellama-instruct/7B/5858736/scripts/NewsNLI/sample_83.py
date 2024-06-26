premise_1 = "two senior National Transitional Council spokesmen said the report was unconfirmed"
premise_2 = "a third reportedly denied the claim"

hypothesis_1 = "Two NTC spokesmen say the report is not confirmed"
hypothesis_2 = "a third denies it"

# the hypothesis mentions the denial of the claim by a third spokesman, which is also mentioned in the premise
if hypothesis_1!= premise_1:
    # check if the denial in the hypothesis contradicts the claim mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
