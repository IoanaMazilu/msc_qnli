premise_members = 770
premise_lists = 10
premise_threshold = premise_members * premise_lists / 4

hypothesis_members = 770
hypothesis_lists = 10
hypothesis_threshold = hypothesis_members * hypothesis_lists / 4

if hypothesis_threshold < premise_threshold:
    label = "contradiction"
else:
    label = "neutral"

print(label)
