text = "English=68 Logic=75 Uml=87 Code=80"
notes = [int(s[-2:]) for s in text.split()]

print("Total is: {} - Average is: {}".format(sum(notes), sum(notes)/len(notes)))
