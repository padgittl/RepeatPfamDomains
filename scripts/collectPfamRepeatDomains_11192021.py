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
                    if 'DUF1758' in accessionDesc or 'PF05585' in accessionID or 'PF01385' in accessionID or 'PF01526' in accessionID or 'PF05380' in accessionID or 'DUF1258' in accessionDesc or 'PF06869' in accessionID or 'PF02992' in accessionID or 'DUF1280' in accessionDesc or 'PF06918' in accessionID or 'PF12017' in accessionID or 'DUF659' in accessionDesc or 'PF00336' in accessionID or 'PF13333' in accessionID or 'PF13683' in accessionID or 'PF17917' in accessionID or 'PF12784' in accessionID or 'DUF1092' in accessionDesc or 'PF06485' in accessionID or 'gag-' in accessionDesc or 'gag ' in accessionDesc or 'GAG-' in accessionDesc or 'GAG ' in accessionDesc or 'ransposase' in accessionDesc or 'LTR' in accessionDesc or 'Ty1' in accessionDesc or 'Ty3' in accessionDesc or 'etrotrans' in accessionDesc or 'etroviral aspartyl protease' in accessionDesc or 'everse transcriptase' in accessionDesc or 'lant transposon protein' in accessionDesc or 'ntegrase core domain' in accessionDesc or 'aspartyl' in accessionDesc or "PF00075" in accessionID or "PF03184" in accessionID or "PF13976" in accessionID or "PF00665" in accessionID or "PF07727" in accessionID or "PF05699" in accessionID or "PF03004" in accessionID or "PF05699" in accessionID or "PF13359" in accessionID or "PF00078" in accessionID or "PF12784" in accessionID or "PF00077" in accessionID or "PF13650" in accessionID or "DUF4219" in accessionDesc or "PF01107" in accessionID or "PF13610" in accessionID or "PF09668" in accessionID or "PF00770" in accessionID or "PF10860" in accessionID or "PF17921" in accessionID or "PF18697" in accessionID or "PF17055" in accessionID or "PF09337" in accessionID or "PF05878" in accessionID or "PF13358" in accessionID or "PF05414" in accessionID or "PF17241" in accessionID or "PF01443" in accessionID or "PF06096" in accessionID or "PF02160" in accessionID or "PF16506" in accessionID or "PF13613" in accessionID or "PF04195" in accessionID or "PF05528" in accessionID or "PF00680" in accessionID or "PF03434" in accessionID or "PF05105" in accessionID or "PF07953" in accessionID or "PF01104" in accessionID or "PF02438" in accessionID or "PF14214" in accessionID or "PF06053" in accessionID or "PF09959" in accessionID or "PF18175" in accessionID or "PF13670" in accessionID or "PF12259" in accessionID or "PF10536" in accessionID or "PF10549" in accessionID or "PF04513" in accessionID or "PF05975" in accessionID or "PF06092" in accessionID or "PF05840" in accessionID or "PF04736" in accessionID or "PF05377" in accessionID or "PF09657" in accessionID or "PF13960" in accessionID or "PF13952" in accessionID or "PF14291" in accessionID or "PF04937" in accessionID or "PF18340" in accessionID or "PF09634" in accessionID or "PF08830" in accessionID or "PF13799" in accessionID or "PF14111" in accessionID or "PF00098" in accessionID or "PF13696" in accessionID or "PF16641" in accessionID or "PF12353" in accessionID or "PF15288" in accessionID or "PF14392" in accessionID or "PF03372" in accessionID or "PF15136" in accessionID or "PF01693" in accessionID:
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
