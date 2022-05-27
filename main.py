import json

<<<<<<< HEAD

def loadTXTData(filename):
	txtlines = []
	with open(file=filename, mode='r', encoding='utf-8') as txtData:
		lines = txtData.readlines()
		for line in lines:
			lineData = line.strip()
			if lineData == "\n":
				continue
			else:
				txtlines.append(lineData)
	return txtlines


def loadJSONData(filename):
	jsonword = []
	with open(file=filename, mode='r', encoding='utf-8') as jsonData:
		jData = json.load(jsonData)
	for j in jData:
		jsonword.append(j['word'])
	return jsonword


def idiomMatch(dictPath, idiomPath):
	txtWrite = []

	dictData = loadTXTData(dictPath)[0]
	idiomData = loadJSONData(idiomPath)

	for idiom in idiomData:
		i = ''
		for im in idiom:
			if im in dictData:
				i += im
			else:
				i = ''
				break
		if i != '':
			txtWrite.append(i)

	return txtWrite


def poetryMatch(dictPath, qtsPath):
	txtWrite = []
	qtsData = loadTXTData(qtsPath)
	dictData = loadTXTData(dictPath)[0]

	for line in qtsData:
		l = ''
		for s in line:
			if s in dictData:
				l += s
			else:
				l = ''
				break
		if l != '':
			txtWrite.append(l)

	return txtWrite


def statsDup(dictData, txtWrite):
	stats = []
	for s in dictData:
		scount = 0
		for line in txtWrite:
			scount += line.count(s)
		# t = (s , ':' , scount)
		t = f'{s}:{scount}'
		stats.append(t)

	return stats


dictPath = 'data/dict.txt'
qtsPath = 'data/cy.txt'
idiomPath = 'data/idiom.json'

# idiom = idiomMatch(dictPath, idiomPath)
# print(idiom)
=======
def loadTXTData(filename):
    txtlines = []
    with open(file=filename, mode='r', encoding='utf-8') as txtData:
        lines = txtData.readlines()
        for line in lines:
            lineData = line.strip()
            if lineData == "\n":
                continue
            else:
                txtlines.append(lineData)
    return txtlines


def loadJSONData(filename):
    jsonword = []
    with open(file=filename, mode='r',encoding='utf-8') as jsonData:
        jData = json.load(jsonData)
    for j in jData:
        jsonword.append(j['word'])
    return jsonword


def idiomMatch(dictPath, idiomPath):
    txtWrite = []
    
    dictData = loadTXTData(dictPath)[0]
    idiomData = loadJSONData(idiomPath)
    
    for idiom in idiomData:
        i = ''
        for im in idiom:
            if im in dictData:
                i += im
            else:
                i = ''
                break
        if i != '':
            txtWrite.append(i)
            
    return txtWrite
    
def poetryMatch(dictPath, qtsPath):
    txtWrite = []
    qtsData = loadTXTData(qtsPath)
    dictData = loadTXTData(dictPath)[0]
    
    for line in qtsData:
        l = ''
        for s in line:
            if s in dictData:
                l += s
            else:
                l = ''
                break
        if l != '':
            txtWrite.append(l)
    
    return txtWrite

def statsDup(dictData, txtWrite):
    stats = []
    for s in dictData:
        scount = 0
        for line in txtWrite:
            scount += line.count(s)
        # t = (s , ':' , scount)
        t = f'{s}:{scount}'
        stats.append(t)
    
    return stats


dictPath ='data/dict.txt'
qtsPath = 'data/qts.txt'
idiomPath = 'data/idiom.json'

idiom = idiomMatch(dictPath, idiomPath)
print(idiom)
>>>>>>> 4cc802f (Initial commit)

poetry = poetryMatch(dictPath, qtsPath)
print(poetry)

dictData = loadTXTData(dictPath)[0]

<<<<<<< HEAD
# idiomstats = statsDup(dictData, idiom)
# print(idiomstats)

print(statsDup(dictData, poetry))
=======
idiomstats=statsDup(dictData, idiom)
poetrystats=statsDup(dictData, poetry)
>>>>>>> 4cc802f (Initial commit)
