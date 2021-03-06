#!/bin/python2

import random

#[fracA, propA, LowToneAdur, HighToneAdur, maxStartHTA] 
a=[
["5-8", 0.625, 2472, 1546, 886], 
["6-8", 0.75, 2060, 1546, 474], 
["4-8", 0.5, 2622, 1312, 1270], 
["5-8", 0.625, 2098, 1312, 746], 
["2-8", 0.25, 3348, 838, 2470], 
["3-8", 0.375, 2232, 838, 1354], 
["5-8", 0.625, 2614, 1634, 940], 
["7-8", 0.875, 1866, 1632, 194], 
["3-8", 0.375, 3066, 1150, 1876], 
["5-8", 0.625, 1840, 1150, 650], 
["2-8", 0.25, 3594, 898, 2656], 
["4-8", 0.5, 1798, 900, 858], 
["4-8", 0.5, 2922, 1462, 1420], 
["7-8", 0.875, 1670, 1462, 168], 
["3-8", 0.375, 3222, 1208, 1974], 
["6-8", 0.75, 1610, 1208, 362], 
["2-8", 0.25, 3772, 944, 2788], 
["5-8", 0.625, 1508, 942, 526], 
["5-8", 0.625, 2024, 1266, 718], 
["6-8", 0.75, 1688, 1266, 382], 
["4-8", 0.5, 2062, 1032, 990], 
["5-8", 0.625, 1650, 1032, 578], 
["2-8", 0.25, 2228, 558, 1630], 
["3-8", 0.375, 1484, 556, 888], 
["5-8", 0.625, 2166, 1354, 772], 
["7-8", 0.875, 1546, 1352, 154], 
["3-8", 0.375, 2320, 870, 1410], 
["5-8", 0.625, 1392, 870, 482], 
["2-8", 0.25, 2474, 618, 1816], 
["4-8", 0.5, 1238, 620, 578], 
["4-8", 0.5, 2362, 1182, 1140], 
["7-8", 0.875, 1350, 1182, 128], 
["3-8", 0.375, 2474, 928, 1506], 
["6-8", 0.75, 1238, 928, 270], 
["2-8", 0.25, 2652, 664, 1948], 
["5-8", 0.625, 1060, 662, 358], 
["5-8", 0.625, 2920, 1826, 1054], 
["6-8", 0.75, 2434, 1826, 568], 
["4-8", 0.5, 3182, 1592, 1550], 
["5-8", 0.625, 2546, 1592, 914], 
["2-8", 0.25, 4468, 1118, 3310], 
["3-8", 0.375, 2978, 1116, 1822], 
["5-8", 0.625, 3062, 1914, 1108], 
["7-8", 0.875, 2186, 1912, 234], 
["3-8", 0.375, 3814, 1430, 2344], 
["5-8", 0.625, 2288, 1430, 818], 
["2-8", 0.25, 4714, 1178, 3496], 
["4-8", 0.5, 2358, 1180, 1138], 
["4-8", 0.5, 3482, 1742, 1700], 
["7-8", 0.875, 1990, 1742, 208], 
["3-8", 0.375, 3968, 1488, 2440], 
["6-8", 0.75, 1984, 1488, 456], 
["2-8", 0.25, 4892, 1224, 3628], 
["5-8", 0.625, 1956, 1222, 694], 
["5-8", 0.625, 2024, 1266, 718], 
["6-8", 0.75, 1688, 1266, 382], 
["4-8", 0.5, 2062, 1032, 990], 
["5-8", 0.625, 1650, 1032, 578], 
["2-8", 0.25, 2228, 558, 1630], 
["3-8", 0.375, 1484, 556, 888], 
["5-8", 0.625, 2166, 1354, 772], 
["7-8", 0.875, 1546, 1352, 154], 
["3-8", 0.375, 2320, 870, 1410], 
["5-8", 0.625, 1392, 870, 482], 
["2-8", 0.25, 2474, 618, 1816], 
["4-8", 0.5, 1238, 620, 578], 
["4-8", 0.5, 2362, 1182, 1140], 
["7-8", 0.875, 1350, 1182, 128], 
["3-8", 0.375, 2474, 928, 1506], 
["6-8", 0.75, 1238, 928, 270], 
["2-8", 0.25, 2652, 664, 1948], 
["5-8", 0.625, 1060, 662, 358], 
["5-8", 0.625, 3368, 2106, 1222], 
["6-8", 0.75, 2808, 2106, 662], 
["4-8", 0.5, 3742, 1872, 1830], 
["5-8", 0.625, 2994, 1872, 1082], 
["2-8", 0.25, 5588, 1398, 4150], 
["3-8", 0.375, 3724, 1396, 2288], 
["5-8", 0.625, 3510, 2194, 1276], 
["7-8", 0.875, 2506, 2192, 274], 
["3-8", 0.375, 4560, 1710, 2810], 
["5-8", 0.625, 2736, 1710, 986], 
["2-8", 0.25, 5834, 1458, 4336], 
["4-8", 0.5, 2918, 1460, 1418], 
["4-8", 0.5, 4042, 2022, 1980], 
["7-8", 0.875, 2310, 2022, 248], 
["3-8", 0.375, 4714, 1768, 2906], 
["6-8", 0.75, 2358, 1768, 550], 
["2-8", 0.25, 6012, 1504, 4468], 
["5-8", 0.625, 2404, 1502, 862], 
["5-8", 0.625, 2024, 1266, 718], 
["6-8", 0.75, 1688, 1266, 382], 
["4-8", 0.5, 2062, 1032, 990], 
["5-8", 0.625, 1650, 1032, 578], 
["2-8", 0.25, 2228, 558, 1630], 
["3-8", 0.375, 1484, 556, 888], 
["5-8", 0.625, 2166, 1354, 772], 
["7-8", 0.875, 1546, 1352, 154], 
["3-8", 0.375, 2320, 870, 1410], 
["5-8", 0.625, 1392, 870, 482], 
["2-8", 0.25, 2474, 618, 1816], 
["4-8", 0.5, 1238, 620, 578], 
["4-8", 0.5, 2362, 1182, 1140], 
["7-8", 0.875, 1350, 1182, 128], 
["3-8", 0.375, 2474, 928, 1506], 
["6-8", 0.75, 1238, 928, 270], 
["2-8", 0.25, 2652, 664, 1948], 
["5-8", 0.625, 1060, 662, 358]]
b=[
["6-8", 0.75, 1688, 1266, 382], 
["5-8", 0.625, 2024, 1266, 718], 
["5-8", 0.625, 1650, 1032, 578], 
["4-8", 0.5, 2062, 1032, 990], 
["3-8", 0.375, 1484, 556, 888], 
["2-8", 0.25, 2228, 558, 1630], 
["7-8", 0.875, 1546, 1352, 154], 
["5-8", 0.625, 2166, 1354, 772], 
["5-8", 0.625, 1392, 870, 482], 
["3-8", 0.375, 2320, 870, 1410], 
["4-8", 0.5, 1238, 620, 578], 
["2-8", 0.25, 2474, 618, 1816], 
["7-8", 0.875, 1350, 1182, 128], 
["4-8", 0.5, 2362, 1182, 1140], 
["6-8", 0.75, 1238, 928, 270], 
["3-8", 0.375, 2474, 928, 1506], 
["5-8", 0.625, 1060, 662, 358], 
["2-8", 0.25, 2652, 664, 1948], 
["6-8", 0.75, 2060, 1546, 474], 
["5-8", 0.625, 2472, 1546, 886], 
["5-8", 0.625, 2098, 1312, 746], 
["4-8", 0.5, 2622, 1312, 1270], 
["3-8", 0.375, 2232, 838, 1354], 
["2-8", 0.25, 3348, 838, 2470], 
["7-8", 0.875, 1866, 1632, 194], 
["5-8", 0.625, 2614, 1634, 940], 
["5-8", 0.625, 1840, 1150, 650], 
["3-8", 0.375, 3066, 1150, 1876], 
["4-8", 0.5, 1798, 900, 858], 
["2-8", 0.25, 3594, 898, 2656], 
["7-8", 0.875, 1670, 1462, 168], 
["4-8", 0.5, 2922, 1462, 1420], 
["6-8", 0.75, 1610, 1208, 362], 
["3-8", 0.375, 3222, 1208, 1974], 
["5-8", 0.625, 1508, 942, 526], 
["2-8", 0.25, 3772, 944, 2788], 
["6-8", 0.75, 1688, 1266, 382], 
["5-8", 0.625, 2024, 1266, 718], 
["5-8", 0.625, 1650, 1032, 578], 
["4-8", 0.5, 2062, 1032, 990], 
["3-8", 0.375, 1484, 556, 888], 
["2-8", 0.25, 2228, 558, 1630], 
["7-8", 0.875, 1546, 1352, 154], 
["5-8", 0.625, 2166, 1354, 772], 
["5-8", 0.625, 1392, 870, 482], 
["3-8", 0.375, 2320, 870, 1410], 
["4-8", 0.5, 1238, 620, 578], 
["2-8", 0.25, 2474, 618, 1816], 
["7-8", 0.875, 1350, 1182, 128], 
["4-8", 0.5, 2362, 1182, 1140], 
["6-8", 0.75, 1238, 928, 270], 
["3-8", 0.375, 2474, 928, 1506], 
["5-8", 0.625, 1060, 662, 358], 
["2-8", 0.25, 2652, 664, 1948], 
["6-8", 0.75, 2434, 1826, 568], 
["5-8", 0.625, 2920, 1826, 1054], 
["5-8", 0.625, 2546, 1592, 914], 
["4-8", 0.5, 3182, 1592, 1550], 
["3-8", 0.375, 2978, 1116, 1822], 
["2-8", 0.25, 4468, 1118, 3310], 
["7-8", 0.875, 2186, 1912, 234], 
["5-8", 0.625, 3062, 1914, 1108], 
["5-8", 0.625, 2288, 1430, 818], 
["3-8", 0.375, 3814, 1430, 2344], 
["4-8", 0.5, 2358, 1180, 1138], 
["2-8", 0.25, 4714, 1178, 3496], 
["7-8", 0.875, 1990, 1742, 208], 
["4-8", 0.5, 3482, 1742, 1700], 
["6-8", 0.75, 1984, 1488, 456], 
["3-8", 0.375, 3968, 1488, 2440], 
["5-8", 0.625, 1956, 1222, 694], 
["2-8", 0.25, 4892, 1224, 3628], 
["6-8", 0.75, 1688, 1266, 382], 
["5-8", 0.625, 2024, 1266, 718], 
["5-8", 0.625, 1650, 1032, 578], 
["4-8", 0.5, 2062, 1032, 990], 
["3-8", 0.375, 1484, 556, 888], 
["2-8", 0.25, 2228, 558, 1630], 
["7-8", 0.875, 1546, 1352, 154], 
["5-8", 0.625, 2166, 1354, 772], 
["5-8", 0.625, 1392, 870, 482], 
["3-8", 0.375, 2320, 870, 1410], 
["4-8", 0.5, 1238, 620, 578], 
["2-8", 0.25, 2474, 618, 1816], 
["7-8", 0.875, 1350, 1182, 128], 
["4-8", 0.5, 2362, 1182, 1140], 
["6-8", 0.75, 1238, 928, 270], 
["3-8", 0.375, 2474, 928, 1506], 
["5-8", 0.625, 1060, 662, 358], 
["2-8", 0.25, 2652, 664, 1948], 
["6-8", 0.75, 2808, 2106, 662], 
["5-8", 0.625, 3368, 2106, 1222], 
["5-8", 0.625, 2994, 1872, 1082], 
["4-8", 0.5, 3742, 1872, 1830], 
["3-8", 0.375, 3724, 1396, 2288], 
["2-8", 0.25, 5588, 1398, 4150], 
["7-8", 0.875, 2506, 2192, 274], 
["5-8", 0.625, 3510, 2194, 1276], 
["5-8", 0.625, 2736, 1710, 986], 
["3-8", 0.375, 4560, 1710, 2810], 
["4-8", 0.5, 2918, 1460, 1418], 
["2-8", 0.25, 5834, 1458, 4336], 
["7-8", 0.875, 2310, 2022, 248], 
["4-8", 0.5, 4042, 2022, 1980], 
["6-8", 0.75, 2358, 1768, 550], 
["3-8", 0.375, 4714, 1768, 2906], 
["5-8", 0.625, 2404, 1502, 862], 
["2-8", 0.25, 6012, 1504, 4468]]
c=[
["5-8", 0.625, 1335, 835, 460], 
["6-8", 0.75, 1112, 835, 238], 
["4-8", 0.5, 1416, 708, 667], 
["5-8", 0.625, 1133, 708, 384], 
["2-8", 0.25, 1808, 453, 1315], 
["3-8", 0.375, 1205, 453, 713], 
["5-8", 0.625, 1412, 882, 489], 
["7-8", 0.875, 1008, 881, 86], 
["3-8", 0.375, 1656, 621, 995], 
["5-8", 0.625, 994, 621, 333], 
["2-8", 0.25, 1941, 485, 1416], 
["4-8", 0.5, 971, 486, 445], 
["4-8", 0.5, 1578, 789, 748], 
["7-8", 0.875, 902, 789, 72], 
["3-8", 0.375, 1740, 652, 1048], 
["6-8", 0.75, 869, 652, 177], 
["2-8", 0.25, 2037, 510, 1487], 
["5-8", 0.625, 814, 509, 266], 
["5-8", 0.625, 1093, 684, 369], 
["6-8", 0.75, 912, 684, 188], 
["4-8", 0.5, 1113, 557, 516], 
["5-8", 0.625, 891, 557, 294], 
["2-8", 0.25, 1203, 301, 862], 
["3-8", 0.375, 801, 300, 461], 
["5-8", 0.625, 1170, 731, 398], 
["7-8", 0.875, 835, 730, 65], 
["3-8", 0.375, 1253, 470, 743], 
["5-8", 0.625, 752, 470, 242], 
["2-8", 0.25, 1336, 334, 962], 
["4-8", 0.5, 669, 335, 294], 
["4-8", 0.5, 1275, 638, 597], 
["7-8", 0.875, 729, 638, 51], 
["3-8", 0.375, 1336, 501, 795], 
["6-8", 0.75, 669, 501, 127], 
["2-8", 0.25, 1432, 359, 1034], 
["5-8", 0.625, 572, 357, 175], 
["5-8", 0.625, 1577, 986, 551], 
["6-8", 0.75, 1314, 986, 288], 
["4-8", 0.5, 1718, 860, 819], 
["5-8", 0.625, 1375, 860, 475], 
["2-8", 0.25, 2413, 604, 1769], 
["3-8", 0.375, 1608, 603, 965], 
["5-8", 0.625, 1653, 1034, 580], 
["7-8", 0.875, 1180, 1032, 108], 
["3-8", 0.375, 2060, 772, 1247], 
["5-8", 0.625, 1236, 772, 423], 
["2-8", 0.25, 2546, 636, 1869], 
["4-8", 0.5, 1273, 637, 596], 
["4-8", 0.5, 1880, 941, 900], 
["7-8", 0.875, 1075, 941, 94], 
["3-8", 0.375, 2143, 804, 1299], 
["6-8", 0.75, 1071, 804, 228], 
["2-8", 0.25, 2642, 661, 1941], 
["5-8", 0.625, 1056, 660, 356], 
["5-8", 0.625, 1093, 684, 369], 
["6-8", 0.75, 912, 684, 188], 
["4-8", 0.5, 1113, 557, 516], 
["5-8", 0.625, 891, 557, 294], 
["2-8", 0.25, 1203, 301, 862], 
["3-8", 0.375, 801, 300, 461], 
["5-8", 0.625, 1170, 731, 398], 
["7-8", 0.875, 835, 730, 65], 
["3-8", 0.375, 1253, 470, 743], 
["5-8", 0.625, 752, 470, 242], 
["2-8", 0.25, 1336, 334, 962], 
["4-8", 0.5, 669, 335, 294], 
["4-8", 0.5, 1275, 638, 597], 
["7-8", 0.875, 729, 638, 51], 
["3-8", 0.375, 1336, 501, 795], 
["6-8", 0.75, 669, 501, 127], 
["2-8", 0.25, 1432, 359, 1034], 
["5-8", 0.625, 572, 357, 175], 
["5-8", 0.625, 1819, 1137, 641], 
["6-8", 0.75, 1516, 1137, 339], 
["4-8", 0.5, 2021, 1011, 970], 
["5-8", 0.625, 1617, 1011, 566], 
["2-8", 0.25, 3018, 755, 2223], 
["3-8", 0.375, 2011, 754, 1217], 
["5-8", 0.625, 1895, 1185, 671], 
["7-8", 0.875, 1353, 1184, 130], 
["3-8", 0.375, 2462, 923, 1499], 
["5-8", 0.625, 1477, 923, 514], 
["2-8", 0.25, 3150, 787, 2323], 
["4-8", 0.5, 1576, 788, 747], 
["4-8", 0.5, 2183, 1092, 1051], 
["7-8", 0.875, 1247, 1092, 116], 
["3-8", 0.375, 2546, 955, 1551], 
["6-8", 0.75, 1273, 955, 279], 
["2-8", 0.25, 3246, 812, 2394], 
["5-8", 0.625, 1298, 811, 447], 
["5-8", 0.625, 1093, 684, 369], 
["6-8", 0.75, 912, 684, 188], 
["4-8", 0.5, 1113, 557, 516], 
["5-8", 0.625, 891, 557, 294], 
["2-8", 0.25, 1203, 301, 862], 
["3-8", 0.375, 801, 300, 461], 
["5-8", 0.625, 1170, 731, 398], 
["7-8", 0.875, 835, 730, 65], 
["3-8", 0.375, 1253, 470, 743], 
["5-8", 0.625, 752, 470, 242], 
["2-8", 0.25, 1336, 334, 962], 
["4-8", 0.5, 669, 335, 294], 
["4-8", 0.5, 1275, 638, 597], 
["7-8", 0.875, 729, 638, 51], 
["3-8", 0.375, 1336, 501, 795], 
["6-8", 0.75, 669, 501, 127], 
["2-8", 0.25, 1432, 359, 1034], 
["5-8", 0.625, 572, 357, 175]]
d=[
["6-8", 0.75, 912, 684, 188], 
["5-8", 0.625, 1093, 684, 369], 
["5-8", 0.625, 891, 557, 294], 
["4-8", 0.5, 1113, 557, 516], 
["3-8", 0.375, 801, 300, 461], 
["2-8", 0.25, 1203, 301, 862], 
["7-8", 0.875, 835, 730, 65], 
["5-8", 0.625, 1170, 731, 398], 
["5-8", 0.625, 752, 470, 242], 
["3-8", 0.375, 1253, 470, 743], 
["4-8", 0.5, 669, 335, 294], 
["2-8", 0.25, 1336, 334, 962], 
["7-8", 0.875, 729, 638, 51], 
["4-8", 0.5, 1275, 638, 597], 
["6-8", 0.75, 669, 501, 127], 
["3-8", 0.375, 1336, 501, 795], 
["5-8", 0.625, 572, 357, 175], 
["2-8", 0.25, 1432, 359, 1034], 
["6-8", 0.75, 1112, 835, 238], 
["5-8", 0.625, 1335, 835, 460], 
["5-8", 0.625, 1133, 708, 384], 
["4-8", 0.5, 1416, 708, 667], 
["3-8", 0.375, 1205, 453, 713], 
["2-8", 0.25, 1808, 453, 1315], 
["7-8", 0.875, 1008, 881, 86], 
["5-8", 0.625, 1412, 882, 489], 
["5-8", 0.625, 994, 621, 333], 
["3-8", 0.375, 1656, 621, 995], 
["4-8", 0.5, 971, 486, 445], 
["2-8", 0.25, 1941, 485, 1416], 
["7-8", 0.875, 902, 789, 72], 
["4-8", 0.5, 1578, 789, 748], 
["6-8", 0.75, 869, 652, 177], 
["3-8", 0.375, 1740, 652, 1048], 
["5-8", 0.625, 814, 509, 266], 
["2-8", 0.25, 2037, 510, 1487], 
["6-8", 0.75, 912, 684, 188], 
["5-8", 0.625, 1093, 684, 369], 
["5-8", 0.625, 891, 557, 294], 
["4-8", 0.5, 1113, 557, 516], 
["3-8", 0.375, 801, 300, 461], 
["2-8", 0.25, 1203, 301, 862], 
["7-8", 0.875, 835, 730, 65], 
["5-8", 0.625, 1170, 731, 398], 
["5-8", 0.625, 752, 470, 242], 
["3-8", 0.375, 1253, 470, 743], 
["4-8", 0.5, 669, 335, 294], 
["2-8", 0.25, 1336, 334, 962], 
["7-8", 0.875, 729, 638, 51], 
["4-8", 0.5, 1275, 638, 597], 
["6-8", 0.75, 669, 501, 127], 
["3-8", 0.375, 1336, 501, 795], 
["5-8", 0.625, 572, 357, 175], 
["2-8", 0.25, 1432, 359, 1034], 
["6-8", 0.75, 1314, 986, 288], 
["5-8", 0.625, 1577, 986, 551], 
["5-8", 0.625, 1375, 860, 475], 
["4-8", 0.5, 1718, 860, 819], 
["3-8", 0.375, 1608, 603, 965], 
["2-8", 0.25, 2413, 604, 1769], 
["7-8", 0.875, 1180, 1032, 108], 
["5-8", 0.625, 1653, 1034, 580], 
["5-8", 0.625, 1236, 772, 423], 
["3-8", 0.375, 2060, 772, 1247], 
["4-8", 0.5, 1273, 637, 596], 
["2-8", 0.25, 2546, 636, 1869], 
["7-8", 0.875, 1075, 941, 94], 
["4-8", 0.5, 1880, 941, 900], 
["6-8", 0.75, 1071, 804, 228], 
["3-8", 0.375, 2143, 804, 1299], 
["5-8", 0.625, 1056, 660, 356], 
["2-8", 0.25, 2642, 661, 1941], 
["6-8", 0.75, 912, 684, 188], 
["5-8", 0.625, 1093, 684, 369], 
["5-8", 0.625, 891, 557, 294], 
["4-8", 0.5, 1113, 557, 516], 
["3-8", 0.375, 801, 300, 461], 
["2-8", 0.25, 1203, 301, 862], 
["7-8", 0.875, 835, 730, 65], 
["5-8", 0.625, 1170, 731, 398], 
["5-8", 0.625, 752, 470, 242], 
["3-8", 0.375, 1253, 470, 743], 
["4-8", 0.5, 669, 335, 294], 
["2-8", 0.25, 1336, 334, 962], 
["7-8", 0.875, 729, 638, 51], 
["4-8", 0.5, 1275, 638, 597], 
["6-8", 0.75, 669, 501, 127], 
["3-8", 0.375, 1336, 501, 795], 
["5-8", 0.625, 572, 357, 175], 
["2-8", 0.25, 1432, 359, 1034], 
["6-8", 0.75, 1516, 1137, 339], 
["5-8", 0.625, 1819, 1137, 641], 
["5-8", 0.625, 1617, 1011, 566], 
["4-8", 0.5, 2021, 1011, 970], 
["3-8", 0.375, 2011, 754, 1217], 
["2-8", 0.25, 3018, 755, 2223], 
["7-8", 0.875, 1353, 1184, 130], 
["5-8", 0.625, 1895, 1185, 671], 
["5-8", 0.625, 1477, 923, 514], 
["3-8", 0.375, 2462, 923, 1499], 
["4-8", 0.5, 1576, 788, 747], 
["2-8", 0.25, 3150, 787, 2323], 
["7-8", 0.875, 1247, 1092, 116], 
["4-8", 0.5, 2183, 1092, 1051], 
["6-8", 0.75, 1273, 955, 279], 
["3-8", 0.375, 2546, 955, 1551], 
["5-8", 0.625, 1298, 811, 447], 
["2-8", 0.25, 3246, 812, 2394]] 

#Relevant Praat function:
#Create Sound as pure tone: $NAME, $CHAN, $START, $END, $SAMPRATE, $FREQ, 0.2, 0.01, 0.01
#Coda for the a,b matrices: [fracA, propA, LowToneAdur, HighToneAdur, maxStartHTA] 
for x,datae in enumerate(zip(a,b)):
	"""
		Creates a praat script in the most unelegant and nonsofisticated way, 
		csndXY creates the pairs of sounds; selsX creates every stimuli pairs
		cat concatenates them with the delay, and savW saves a .wav of this concatenation
		The script creates needs to be deleted after every change to avoid repetition, it only
		appends new lines, doesn't care about file history...
	"""
	dataA=datae[0]; dataB=datae[1]
	isiA=random.randint(0,dataA[4])/1000.0
	lenAH=isiA+dataA[3]/1000.0
	lenAL=dataA[2]/1000.0
	namAH="toneHigh"+str(dataA[0])
	namAL="toneLow"+str(dataA[0])
	isiB=random.randint(0,dataB[4])/1000.0
	lenBH=isiB+dataB[3]/1000.0
	lenBL=dataB[2]/1000.0
	namBH="toneHigh"+str(dataB[0])
	namBL="toneLow"+str(dataB[0])
	csndAL= 'Create Sound as pure tone: "' + namAL + '", 1, 0, '+str(lenAL)+", 44100, 440, 0.2, 0.01, 0.01"
	csndAH= 'Create Sound as pure tone: "' + namAH + '", 1, '+str(isiA)+", "+str(lenAH)+", 44100, 660, 0.2, 0.01, 0.01"
	csndBL= 'Create Sound as pure tone: "' + namBL + '", 1, 0, '+str(lenBL)+", 44100, 440, 0.2, 0.01, 0.01"
	csndBH= 'Create Sound as pure tone: "' + namBH + '", 1, '+str(isiB)+", "+str(lenBH)+", 44100, 660, 0.2, 0.01, 0.01"
	selsA='selectObject: "Sound '+namAL+'"\n'+'plusObject: "Sound '+namAH+'"\n'+"Combine to stereo\n"+'selectObject: "Sound combined_2"\n'+"Convert to mono\n"+'selectObject: "Sound combined_2_mono"\n'+'Rename: "combined_2_mono_A"\n'+'selectObject: "Sound combined_2"\nRemove\n'
	selsB='selectObject: "Sound '+namBL+'"\n'+'plusObject: "Sound '+namBH+'"\n'+"Combine to stereo\n"+'selectObject: "Sound combined_2"\n'+"Convert to mono\n"+'selectObject: "Sound combined_2_mono"\n'+'Rename: "combined_2_mono_B"\n'+'selectObject: "Sound combined_2"\nRemove\n'
	delay='Create Sound from formula: "delay", 1, 0, 0.75, 44100, "0"\n'
	cat='selectObject: "Sound combined_2_mono_A"\n'+'plusObject: "Sound delay"\n'+'plusObject: "Sound combined_2_mono_B"\n'+'Concatenate\n'+'selectObject: "Sound chain"\n'
	savW='Save as WAV file: "/Personal/scripKidd/git/praat/Sounds/2/'+'Stim_'+str(x)+'_'+str(dataA[0])+'_'+str(dataB[0])+'.wav"\n'+'select all\nRemove\n'
	with  open("/Personal/scripKidd/git/praat/praatScript_oneXoneX2.p","a+") as f:
		f.write(csndAL+"\n"+csndAH+"\n"+csndBL+"\n"+csndBH+"\n"+selsA+delay+selsB+cat+savW)
		f.close()
	#print csndAL+"\n"+csndAH+"\n"+csndBL+"\n"+csndBH+"\n"+selsA+selsB+delay+cat+savW
	
for x,datae in enumerate(zip(c,d)):
	"""
		Creates a praat script in the most unelegant and nonsofisticated way, 
		csndXY creates the pairs of sounds; selsX creates every stimuli pairs
		cat concatenates them with the delay, and savW saves a .wav of this concatenation
		The script creates needs to be deleted after every change to avoid repetition, it only
		appends new lines, doesn't care about file history...
	"""
	dataA=datae[0]; dataB=datae[1]
	isiA=random.randint(0,dataA[4])/1000.0
	lenAH=isiA+dataA[3]/1000.0
	lenAL=dataA[2]/1000.0
	namAH="toneHigh"+str(dataA[0])
	namAL="toneLow"+str(dataA[0])
	isiB=random.randint(0,dataB[4])/1000.0
	lenBH=isiB+dataB[3]/1000.0
	lenBL=dataB[2]/1000.0
	namBH="toneHigh"+str(dataB[0])
	namBL="toneLow"+str(dataB[0])
	csndAL= 'Create Sound as pure tone: "' + namAL + '", 1, 0, '+str(lenAL)+", 44100, 440, 0.2, 0.01, 0.01"
	csndAH= 'Create Sound as pure tone: "' + namAH + '", 1, '+str(isiA)+", "+str(lenAH)+", 44100, 660, 0.2, 0.01, 0.01"
	csndBL= 'Create Sound as pure tone: "' + namBL + '", 1, 0, '+str(lenBL)+", 44100, 440, 0.2, 0.01, 0.01"
	csndBH= 'Create Sound as pure tone: "' + namBH + '", 1, '+str(isiB)+", "+str(lenBH)+", 44100, 660, 0.2, 0.01, 0.01"
	selsA='selectObject: "Sound '+namAL+'"\n'+'plusObject: "Sound '+namAH+'"\n'+"Combine to stereo\n"+'selectObject: "Sound combined_2"\n'+"Convert to mono\n"+'selectObject: "Sound combined_2_mono"\n'+'Rename: "combined_2_mono_A"\n'+'selectObject: "Sound combined_2"\nRemove\n'
	selsB='selectObject: "Sound '+namBL+'"\n'+'plusObject: "Sound '+namBH+'"\n'+"Combine to stereo\n"+'selectObject: "Sound combined_2"\n'+"Convert to mono\n"+'selectObject: "Sound combined_2_mono"\n'+'Rename: "combined_2_mono_B"\n'+'selectObject: "Sound combined_2"\nRemove\n'
	delay='Create Sound from formula: "delay", 1, 0, 0.75, 44100, "0"\n'
	cat='selectObject: "Sound combined_2_mono_A"\n'+'plusObject: "Sound delay"\n'+'plusObject: "Sound combined_2_mono_B"\n'+'Concatenate\n'+'selectObject: "Sound chain"\n'
	savW='Save as WAV file: "/Personal/scripKidd/git/praat/Sounds/1.1/'+'Stim_'+str(x)+'_'+str(dataA[0])+'_'+str(dataB[0])+'.wav"\n'+'select all\nRemove\n'
	with  open("/Personal/scripKidd/git/praat/praatScript_oneXoneX1.1.p","a+") as f:
		f.write(csndAL+"\n"+csndAH+"\n"+csndBL+"\n"+csndBH+"\n"+selsA+delay+selsB+cat+savW)
		f.close()
	#print csndAL+"\n"+csndAH+"\n"+csndBL+"\n"+csndBH+"\n"+selsA+selsB+delay+cat+savW

for x,datae in enumerate(zip(c,d)):
    """
        Creates a praat script in the most unelegant and nonsofisticated way, 
        csndXY creates the pairs of sounds; selsX creates every stimuli pairs
        cat concatenates them with the delay, and savW saves a .wav of this concatenation
        The script creates needs to be deleted after every change to avoid repetition, it only
        appends new lines, doesn't care about file history...
    """
    dataA=datae[0]; dataB=datae[1]
    isiA=(40+random.randint(0,dataA[4]))/1000.0
    lenAH=isiA+dataA[3]/1000.0
    lenAL=dataA[2]/1000.0
    namAH="toneHigh"+str(dataA[0])
    namAL="toneLow"+str(dataA[0])
    isiB=(40+random.randint(0,dataB[4]))/1000.0
    lenBH=isiB+dataB[3]/1000.0
    lenBL=dataB[2]/1000.0
    namBH="toneHigh"+str(dataB[0])
    namBL="toneLow"+str(dataB[0])
    csndAL= 'Create Sound as pure tone: "' + namAL + '", 1, 0, '+str(lenAL)+", 44100, 440, 0.2, 0.01, 0.01"
    csndAH= 'Create Sound as pure tone: "' + namAH + '", 1, '+str(isiA)+", "+str(lenAH)+", 44100, 660, 0.2, 0.01, 0.01"
    csndBL= 'Create Sound as pure tone: "' + namBL + '", 1, 0, '+str(lenBL)+", 44100, 440, 0.2, 0.01, 0.01"
    csndBH= 'Create Sound as pure tone: "' + namBH + '", 1, '+str(isiB)+", "+str(lenBH)+", 44100, 660, 0.2, 0.01, 0.01"
    selsA='selectObject: "Sound '+namAL+'"\n'+'plusObject: "Sound '+namAH+'"\n'+"Combine to stereo\n"+'selectObject: "Sound combined_2"\n'+"Convert to mono\n"+'selectObject: "Sound combined_2_mono"\n'+'Rename: "combined_2_mono_A"\n'+'selectObject: "Sound combined_2"\n'+'Remove\nselectObject: "Sound combined_2_mono_A"\n'
    selsB='selectObject: "Sound '+namBL+'"\n'+'plusObject: "Sound '+namBH+'"\n'+"Combine to stereo\n"+'selectObject: "Sound combined_2"\n'+"Convert to mono\n"+'selectObject: "Sound combined_2_mono"\n'+'Rename: "combined_2_mono_B"\n'+'selectObject: "Sound combined_2"\n'+'Remove\nselectObject: "Sound combined_2_mono_B"\n'
    delay='Create Sound from formula: "delay", 1, 0, 0.75, 44100, "0"\n'
    #cat='selectObject: "Sound combined_2_mono_A"\n'+'plusObject: "Sound delay"\n'+'plusObject: "Sound combined_2_mono_B"\n'+'Concatenate\n'+'selectObject: "Sound chain"\n'
    savWA='Save as WAV file: "/Personal/scripKidd/git/praat/Sounds/comp1.1/'+str(x)+'A_'+str(dataA[0])+'-part'+'.wav"\n'+'select all\nRemove\n'
    savWB='Save as WAV file: "/Personal/scripKidd/git/praat/Sounds/comp1.1/'+str(x)+'B_'+str(dataB[0])+'-part'+'.wav"\n'+'select all\nRemove\n'
    with  open("/Personal/scripKidd/git/praat/praatScript_AravaEP2CompatX1.1.p","a+") as f:
        f.write(csndAL+"\n"+csndAH+"\n"+selsA+savWA+csndBL+"\n"+csndBH+"\n"+selsB+savWB)
        f.close()
        #print csndAL+"\n"+csndAH+"\n"+csndBL+"\n"+csndBH+"\n"+selsA+selsB+delay+cat+savW
