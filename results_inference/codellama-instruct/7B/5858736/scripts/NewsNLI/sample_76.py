premise_favor_war = 52
premise_oppose_war = 46
hypothesis_favor_war = 52

if hypothesis_favor_war!= premise_favor_war:
    label = "contradiction"
else:
    label = "entailment"

print(label)
