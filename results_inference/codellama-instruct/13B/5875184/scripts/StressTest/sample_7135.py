premise_st = 50
premise_tv = 50
premise_sv = 12

hypothesis_st = 10
hypothesis_tv = 10
hypothesis_sv = 12

# check if the hypothesis values contradict the premise estimates
if hypothesis_st > premise_st or hypothesis_tv > premise_tv:
    label = "contradiction"
elif hypothesis_sv!= premise_sv:
    label = "neutral"
else:
    label = "entailment"

print(label)
