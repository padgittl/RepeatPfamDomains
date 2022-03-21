# Identification of repeat-associated Pfam domains

## Updated 11/18/2021 using Pfam release: 33.1
### Previously, updated 10/21/2020 using Pfam release: 33.1

## Identification of repeat-associated domains
<pre>pfamRepeatDomainIdentification_10212020.txt</pre>

## Create file containing repeat-associated Pfam domains
<pre>python scripts/collectPfamRepeatDomains_11192021.py Pfam-A.hmm > pfamRepeatDomains.v6.txt</pre>
<pre>python scripts/collectPfamRepeatDomains_10212020.py Pfam-A.hmm > pfamRepeatDomains.v2.txt</pre>

### pfamRepeatDomains.v*.txt tab-delimited format:
<pre>pfamAccessionID	pfamAccessionDescription</pre>

