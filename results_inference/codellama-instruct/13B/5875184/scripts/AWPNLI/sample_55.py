premise_total_gems = 5155.0
premise_diamonds = 45.0
premise_rubies = premise_total_gems - premise_diamonds

hypothesis_rubies = 5108.0
hypothesis_diamonds = premise_diamonds
hypothesis_total_gems = hypothesis_rubies + hypothesis_diamonds

if hypothesis_total_gems > premise_total_gems:
    label = "contradiction"
elif hypothesis_rubies < premise_rubies:
    label = "contradiction"
else:
    label = "entailment"

print(label)
