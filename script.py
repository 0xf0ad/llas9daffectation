import matplotlib.pyplot as plt

MP, PSI, TSI = 0, 1, 2
title = ["MP", "PSI", "TSI"]

litayban = TSI # beddl hada bach tbeddl lfilliere

L = [
        #AIAC: GEET, GIP, GI
        [[163, 1977], [275, 398], [63, 175], "AIAC: GEET"], [[369, 1741], [78, 356], [125, 320], "AIAC: GIP"], [[1061, 1429], [240, 287], [247, 269], "AIAC: GI"],
        #EHTP: CE, EEE, TLE, CS, GIS, MSE, MSD, MSE, HWRE
        [[58, 1615], [18, 90], [83, 177], "EHTP: Civil Engi"], [[138, 1801], [26, 180], [73, 105], "EHTP: E&EE"], [[626, 1820], [65, 217], [76, 117], "EHTP: T&LE"],
        [[629, 1217], [137, 184], [70, 71], "EHTP: CS"], [[1303, 1904], [199, 233], [299, 300], "EHTP: G&IS"], [[1720, 1777], [210, 312], [0, 0], "EHTP: Materials"],
        [[1204, 1800], [251, 400], [308, 309], "EHTP: M&SD"], [[80, 1177], [0, 0], [0, 0], "EHTP: M&SE"], [[193, 1939], [32, 120],[210, 212], "EHTP: Hydrau"],
        #EMI: GInd, GInf, GM, GE, GPI, GMIS, GC, GM, GRT
        [[93, 1014], [20, 38], [10, 61], "EMI: Genie Indus"], [[58, 833], [36, 146], [92, 111], "EMI: Genie Info"], [[309, 1330], [52, 171], [51, 122], "Genie Meca"],
        [[305, 1513], [24, 188], [8, 64], "EMI: Genie Elec"], [[1236, 1596], [172, 292], [151, 251], "EMI: G Proc Indus"], [[370, 955], [9, 117], [110, 111], "EMI: Genie MIS"],
        [[36, 1441], [85, 145], [54, 160], "EMI: Genie Civil"], [[1457, 1732], [194, 391], [185, 288], "EMI: G Mineral"], [[896, 1253], [178, 206], [140, 199], "EMI: Genie R&T"],
        #ENSEM: CMPI, GSM, QMSI, GP2A, GSERI, GESET, IARCI, DPI, GIL, GLD
        [[1420, 2125], [365, 505], [128, 337], "ENSEM: CMPI"], [[1738, 2137], [355, 500], [181, 333], "ENSEM: GSM"], [[1820, 2187], [474, 537], [347, 378], "ENSEM: QMSI"],
        [[1629, 2194], [437, 545], [257, 365], "ENSEM: GP2A"], [[1495, 2042], [198, 471], [226, 306], "ENSEM: GSERI"], [[1627, 1993], [207, 464], [249, 328], "ENSEM: GESET"],
        [[1964, 2176], [473, 522], [278, 353], "ENSEM: IARCI"], [[1736, 2193], [425, 539], [0,0], "ENSEM: DPI"],
        [[1470, 2026], [375, 467], [324, 363], "ENSEM: GIL"], [[1368, 1639], [313, 334], [342, 352], "ENSEM: GLD"],
        #ENSIAS: 2IA, GL, D2S, BI&A, CSCMC, GD, IDF, 2SCL
        [[12, 760], [2, 48], [41, 53], "ENSIAS: 2IA"], [[82, 844], [13, 133], [133, 315], "ENSIAS: GL"], [[47, 953], [136, 179], [189, 319], "ENSIAS: D2S"],
        [[104, 887], [47, 164], [77, 273], "ENSIAS: BI&A"], [[44, 726], [56, 140], [3, 237], "ENSIAS: CSCMC"], [[161, 773], [27, 120], [136, 164], "ENSIAS: GD"],
        [[263, 1068], [23, 84], [16, 330], "ENSIAS: IDF"], [[768, 1192], [187, 205], [267, 329], "ENSIAS: 2SCL"],
        #ENSMR: electrmec, ESI, EEIER, EG, GI, GInd, IPI, AES, GP, MI, MCQ
        [[280, 1594], [29, 30], [83, 250], "ENSMR: Elecromec"], [[1863, 1966], [306, 402], [0,0], "ENSMR: Envirenement"], [[997, 1818], [308, 352], [189, 350], "ENSMR: EE&IER"],
        [[842, 1913], [235, 264], [94, 350], "ENSMR: G Energ"], [[1273, 1561], [39, 268], [0,0], "ENSMR: GC & Min"], [[549, 1327], [39, 268], [205, 275], "ENSMR: G Info"],
        [[378, 1390], [53, 98], [128, 129], "ENSMR: G Indus"], [[1268, 1926], [240, 282], [201, 270], "ENSMR: IPI"], [[1173, 1975], [328, 422], [344, 370], "ENSMR: A&ES"],
        [[1420, 1610], [238, 276], [207, 360], "ENSMR: G Prod"], [[1613, 1880], [127, 266], [181, 342], "ENSMR: Mainten"], [[1760, 1992], [295, 300], [148, 375], "ENSMR: M&CQ"],
        #ESI: ICSD, ISSIC, ISITD, IIN
        [[1191, 2255], [0, 0], [0, 0], "ESI: ICSD"], [[1268, 2169], [0, 0], [0, 0], "ESI: ISSIC"], [[1436, 2310], [319, 464], [0, 0], "ESI: ISITD"], [[1403, 2266], [295, 495], [0, 0], "ESI: IIN"],
        #ESITH: GI, IMS
#        [[2142, 2467], [523, 848], [440, 592], "ESITH: GI"], [[2356, 2395], [609, 759], [525, 595], "ESITH: IMS"], [[0, 0], [0, 0], [0, 0], "ESITH: TTI"], [[0, 0], [0, 0], [0, 0], "ESITH: CTM"],
        #IAV: gr-eau, gr-ener, sc geo
        [[1556, 1950], [350, 372], [222, 321], "IAV: GR-EAU"], [[0, 0], [369, 389], [371, 518], "IAV: GR-ENER"], [[287, 1815], [0, 0], [0, 0], "IAV: Science Geomatique"],
        #INPT: ASEDS, DATA, ICCN, CLOUD, AMOA, SESNUM, SMART
        [[56, 306], [3, 76], [34, 87], "INPT: ASEDS"], [[102, 355], [19, 122], [25, 252], "INPT: DATA"], [[128, 431], [14, 109], [7, 121], "INPT: ICCN"],
        [[360, 567], [15, 129], [62, 222], "INPT: CLOUD"], [[438, 843], [98, 169], [118, 276], "INPT: AMOA"],
        [[428, 1048], [110, 193], [113, 242], "INPT: SESNUM"], [[365, 1019], [82, 200], [195, 318], "INPT: SMART"],
        #INSEA: AF, DS, D&SE, SD&RO, BDBD, EASBD
        [[440, 1249], [30, 301], [0,0], "INSEA: Act-Fin"], [[65, 1190], [212, 252], [0, 0], "INSEA: Data Scien"], [[612, 1326], [160, 262], [0, 0], "INSEA: D&SE"],
        [[1080, 1881], [269, 408], [0, 0], "INSEA: SD&RO"], [[1362, 1954], [284, 439], [0, 0], "INSEA: BD&BD"], [[823, 1817], [132, 387], [0, 0], "INSEA: EA&BD"],
        #ENSAM-R: GEIN, ISEE, GBM, INDIA, IMQ, GM, IAA
#        [[2290, 2292], [520, 574], [397, 422], "ENSAM-R: GEIN"], [[2280, 2323], [598, 610], [393, 436], "ENSAM-R: ISEE"], [[1986, 2303], [499, 627], [443, 471], "ENSAM-R: GBM"],
#        [[1641, 2162], [0, 0], [0, 0], "ENSAM-R: INDIA"], [[2080, 2299], [477, 629], [0, 0], "ENSAM-R: IMQ"], [[2134, 2551], [0, 0], [383, 453], "ENSAM-R: GM"],
#        [[1906, 2308], [0, 0], [402, 449], "ENSAM-R: IAA"]
    ]

for i in range(len(L)):
    for j in range(i, len(L)):
        if L[i][litayban][1] > L[j][litayban][1]:
            tmp = L[i]
            L[i] = L[j]
            L[j] = tmp

y_min = [i[litayban][0] for i in L if i[litayban][0] != 0]
y_max = [i[litayban][1] for i in L if i[litayban][0] != 0]
labels =[i[3] for i in L if i[litayban][0] != 0]

fig, ax = plt.subplots(figsize=(15, 15))
x = range(len(y_min))

if litayban == MP:
    ax.hlines([500*i for i in range(1, (y_max[-1]//500)+1)], xmin=0 ,xmax=len(y_max), linewidth=1, color="gray")
else:
    ax.hlines([100*i for i in range(1, (y_max[-1]//100)+1)], xmin=0 ,xmax=len(y_max), linewidth=1, color="gray")


ax.vlines(x, ymin=y_min, ymax=y_max, linewidth=4)
ax.vlines(x, ymin=[y_max[-1]]*len(y_min), ymax=y_max, linewidth=1, color="gray")
ax.plot(x, y_min, '_', linewidth=4, markersize=20)
ax.plot(x, y_max, '_', linewidth=4, markersize=20)
ax.set_xticks(x, labels, rotation='vertical')
plt.title(title[litayban])

plt.ylim(y_max[-1], 0)
plt.savefig(title[litayban]+".png") 
#plt.show()
