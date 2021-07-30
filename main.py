import sys
import math
dataawal = []
dataurut = []
datahslperkalian = 1
# parse data dari command line
for i in range(1, len(sys.argv)):
    dataawal.append(int(sys.argv[i]))

# sorting data dari terkecil ke terbesar
for i in dataawal:
    dataurut.append(i)
for i in dataurut[:-1]:
    for j in dataurut[(dataurut.index(i)+1):]:
        if i > j:
            temp = i
            idx1 = dataurut.index(i)
            idx2 = dataurut.index(j)
            dataurut[idx1] = j
            dataurut[idx2] = temp
        else:
            continue

# operasi untuk mencari mean
Jumlah = 0
for i in dataurut:
    Jumlah += i
datamean = Jumlah/len(dataurut)

# operasi untuk mencari median
if len(dataurut) % 2 != 0:
    idxdian = math.floor(len(dataurut)/2)
    datamedian = dataurut[idxdian]
else:
    idxdian = len(dataurut)/2
    jumlah2 = 0
    for i in dataurut[int(idxdian-1):int(idxdian-1+2)]:
        jumlah2 += i
    datamedian = jumlah2/2

# operasi perkalian keseluruhan data
for j in range(len(dataawal)):
    datahslperkalian = datahslperkalian*dataawal[j]

# print output hasil keseluruhan
print("\n\tdata input: ", *dataawal, "\n\tdata pengurutan: ",
      *dataurut, "\n\trata-rata data: ", datamean, "\n\tnilai tengah data: ",
      datamedian, "\n\thasil kali keseluruhan data: ", datahslperkalian)
