premise = "Instagram got so popular so fast that Facebook took notice and purchased the company for a billion dollars -- (yes, $1 billion) -- to bolster its own smart phone presence shortly before its IPO."
hypothesis = "Rushkoff:Facebook paid $1 billion for Instagram and needs a return."

# extract the numerical entities from the premise
premise_billion = premise.split("$")[1].split(" ")[0]

# extract the numerical entities from the hypothesis
hypothesis_billion = hypothesis.split("$")[1].split(" ")[0]

# compare the numerical entities
if premise_billion!= hypothesis_billion:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
