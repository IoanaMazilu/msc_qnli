read_pages_premise = 147.0
total_pages = 563.0
read_pages = total_pages - read_pages_premise
if read_pages == 416.0:
    label = "entailment"
else:
    label = "contradiction"
print(label)
