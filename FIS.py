pmtb=5000
pmtk=1000
psdb=600
psdk=100
prdmax=7000
prdmin=2000
xpmt=int(input("Masukan inputan Permintaan : "))
xpsd=int(input("Masukan inputan Persediaan : "))

#fungsi permintaan linear turun
if (xpmt<=pmtk): pmtt=1
elif (xpmt>pmtk and xpmt<pmtb): pmtt=(pmtb-xpmt)/(pmtb-pmtk)
else: pmtt=0

#fungsi permintaan linear naik
if (xpmt<=pmtk): pmtn=0
elif (xpmt>pmtk and xpmt<pmtb): pmtn=(xpmt-pmtk)/(pmtb-pmtk)
else: pmtn=1
#fungsi persediaan sedikit
if (xpsd<=psdk): psds=1
elif(xpsd>psdk and xpsd<psdb): psds=(psdb-xpsd)/(psdb-psdk)
else: psds=0
#fungsi persediaan banyak
if (xpsd<=psdk): psdba=0
elif(xpsd>psdk and xpsd<psdb): psdba=(xpsd-psdk)/(psdb-psdk)
else: psdba=1

#IMPLIKASI
#Rule 1 : IF permintaan turun and persediaan banyak then produksi barang berkurang
prdk1=min(pmtt,psdba)
#Rule 2 : IF permintaan turun and persediaan sedikit then produksi barang berkurang
prdk2=min(pmtt,psds)
#Rule 3 : IF permintaan naik and persediaan banyak then produksi barang bertambah
prdb1=min(pmtn,psdba)
#Rule 4 : IF permintaan naik and persediaan sedikit THEN produksi barang bertambah
prdb2=min(pmtn,psds)

#AGREGASI
prdk=max(prdk1,prdk2)
prdb=max(prdb1,prdb2)
if (prdk>prdb):
    a1=prdmax-(prdk*(prdmax-prdmin))
    a2=prdmax-(prdb*(prdmax-prdmin))
    def m(z):
        if (z<=a1): mz=prdk
        elif (z>a1 and z<a2): mz=(prdmax-z)/(prdmax-prdmin)
        else:mz=prdb
        return mz
elif (prdk==prdb):
    a1=prdmax-(prdk*(prdmax-prdmin))
    a2=a1
    def m(z):
        mz=prdk
        return mz
else :
    a1=(prdk*(prdmax-prdmin))+prdmin
    a2=(prdb*(prdmax-prdmin))+prdmin
    def m(z):
        if (z<=a1): mz=prdk
        elif (z>a1 and z<a2): mz=(z-prdmin)/(prdmax-prdmin)
        else: mz=prdb
        return mz

print ("berikut nilai a1 = ", a1," dari derajat keanggotaan = ", prdk)
print ("dan nilai a2 = ", a2," dari derajat keanggotaan = ", prdb)