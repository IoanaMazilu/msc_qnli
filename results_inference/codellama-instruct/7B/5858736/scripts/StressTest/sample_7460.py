premise_members = 770
premise_lists = 10
premise_threshold = premise_lists / premise_members

hypothesis_members = 770
hypothesis_lists = 10
hypothesis_threshold = hypothesis_lists / hypothesis_members

if hypothesis_threshold >= premise_threshold:
    label = "entailment"
elif hypothesis_threshold < premise_threshold:
    label = "contradiction"
else:
    label = "neutral"

print(label)
