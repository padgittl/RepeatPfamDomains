# Identification of repeat-associated Pfam domains

Updated 11/18/2021 using Pfam release: 33.1
## Previously, updated 10/21/2020 using Pfam release: 33.1

# How repeat-associated domains were identified
pfamRepeatDomainIdentification_10212020.txt

# Create file containing repeat-associated Pfam domains
python scripts/collectPfamRepeatDomains_11192021.py Pfam-A.hmm > pfamRepeatDomains.v6.txt

python scripts/collectPfamRepeatDomains_10212020.py Pfam-A.hmm > pfamRepeatDomains.v2.txt

pfamRepeatDomains.v*.txt tab-delimited format:
pfamAccessionID	pfamAccessionDescription	

