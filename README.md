# Identification of repeat-associated Pfam domains

Updated 10/21/2020 using Pfam release: 33.1

# How repeat-associated domains were identified
pfamRepeatDomainIdentification.txt


# Create file containing repeat-associated Pfam domains
python collectPfamRepeatDomains.py Pfam-A.hmm > pfamRepeatDomains.v2.txt

pfamRepeatDomains.v2.txt tab-delimited format: 
pfamAccessionID	pfamAccessionDescription	

