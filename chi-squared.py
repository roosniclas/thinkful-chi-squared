import scipy.stats as stats
import collections
import matplotlib.pyplot as plt

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

ls = [x for x in freq.values()]

chi, p = stats.chisquare(ls)

print('The chi value is %f and the p value is %f' % (chi, p))
