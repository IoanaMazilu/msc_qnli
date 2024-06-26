premise_poll_bin_laden_death = 69
hypothesis_poll_bin_laden_death = 12

if hypothesis_poll_bin_laden_death > premise_poll_bin_laden_death:
    label = "contradiction"
else:
    label = "entailment"

print(label)
