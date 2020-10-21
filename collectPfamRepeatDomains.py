import sys, re, os


###############
# SUBROUTINES #
###############


def readPfamFile(pfamFile):
    repeatDict = {}
    with open(pfamFile,'r') as PFAM:
        for line in PFAM:
            if 'ACC ' in line:
                getAccessionID = re.search('\s(.+)',line)
                accessionID = getAccessionID.group(1)
                accessionID = accessionID.strip()
                fullAccessionDescription = PFAM.next().strip().split('DESC')
                accessionDesc = fullAccessionDescription[1].strip()
                if "PF11474" not in accessionID and "PF06550" not in accessionID and "PF00026" not in accessionID and "PF17984" not in accessionID and "PF16828" not in accessionID and "PF16770" not in accessionID:
                    if 'DUF1758' in accessionDesc or 'PF05585' in accessionID or 'PF01385' in accessionID or 'PF01526' in accessionID or 'PF05380' in accessionID or 'DUF1258' in accessionDesc or 'PF06869' in accessionID or 'PF02992' in accessionID or 'DUF1280' in accessionDesc or 'PF06918' in accessionID or 'PF12017' in accessionID or 'DUF659' in accessionDesc or "PF04937" in accessionID or 'DUF4371' in accessionDesc or 'PF14291' in accessionID or 'PF00336' in accessionID or 'PF13333' in accessionID or 'PF13683' in accessionID or 'PF17917' in accessionID or 'PF12784' in accessionID or 'DUF1092' in accessionDesc or 'PF06485' in accessionID or 'gag-' in accessionDesc or 'gag ' in accessionDesc or 'GAG-' in accessionDesc or 'GAG ' in accessionDesc or 'ransposase' in accessionDesc or 'LTR' in accessionDesc or 'Ty1' in accessionDesc or 'Ty3' in accessionDesc or 'etrotrans' in accessionDesc  or 'etroviral aspartyl protease' in accessionDesc or 'everse transcriptase' in accessionDesc or 'lant transposon protein' in accessionDesc or 'ntegrase core domain' in accessionDesc or 'aspartyl' in accessionDesc or "PF00075" in accessionID or "PF03184" in accessionID or "PF13976" in accessionID or "PF00665" in accessionID or "PF07727" in accessionID or "PF05699" in accessionID or "PF14372" in accessionID or "PF03004" in accessionID or "PF05699" in accessionID or "PF14372" in accessionID or "PF13359" in accessionID or "PF13917" in accessionID or "PF13837" in accessionID or "PF12776" in accessionID or "PF00078" in accessionID or "PF12784" in accessionID or "PF00077" in accessionID or "DUF4283" in accessionDesc or "PF14111" in accessionID or "DUF4216" in accessionDesc or "PF13952" in accessionID or "PF13650" in accessionID or "DUF4219" in accessionDesc or "DUF4218" in accessionDesc or "PF01107" in accessionID or "PF13610" in accessionID or "PF14392" in accessionID or "PF09668" in accessionID or "PF00098" in accessionID or "PF00770" in accessionID:
                        if accessionID not in repeatDict:
                            repeatDict[accessionID] = accessionDesc
    return(repeatDict)


############
### MAIN ###
############


usage = "Usage: " + sys.argv[0] + " <pfam file> "
if len(sys.argv) != 2:
    print usage
    sys.exit()

pfamFile = sys.argv[1]

repeatDict = readPfamFile(pfamFile)
for accessionID in repeatDict:
    accessionDesc = repeatDict[accessionID]
    print("%s\t%s\t" % (accessionID,accessionDesc))
