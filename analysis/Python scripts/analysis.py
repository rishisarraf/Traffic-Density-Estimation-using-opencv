import math
import matplotlib.pyplot as plt
import pandas as pd
import sys

baseline = [0.093991,0.112429,0.126093,0.127441,0.127406,0.137042,0.144355,0.144159,0.143089,0.137477,0.134307,0.130706,0.134813,0.136948,0.135573,0.139495,0.147529,0.161158,0.172554,0.168714,0.166174,0.171829,0.182276,0.191807,0.194593,0.194989,0.19051,0.19192,0.188648,0.188828,0.188135,0.18192,0.186293,0.174647,0.173941,0.170485,0.173491,0.171892,0.173443,0.172989,0.172432,0.170783,0.170685,0.170532,0.170254,0.171531,0.171621,0.172734,0.168071,0.165034,0.167393,0.167268,0.16918,0.168537,0.166437,0.165273,0.167146,0.169039,0.168255,0.165845,0.166221,0.16628,0.1682,0.190819,0.169341,0.168561,0.167503,0.169446,0.173016,0.17641,0.196352,0.174341,0.175701,0.176163,0.177523,0.176488,0.194401,0.178887,0.205573,0.187904,0.191873,0.214865,0.22184,0.224132,0.236465,0.253115,0.273634,0.298283,0.309142,0.305442,0.312735,0.326553,0.326815,0.327916,0.323755,0.320553,0.323661,0.324068,0.320867,0.319354,0.327046,0.359929,0.382638,0.394237,0.406511,0.421045,0.42755,0.422805,0.42757,0.440498,0.435529,0.434302,0.435474,0.437418,0.431653,0.446819,0.464853,0.479411,0.498852,0.544783,0.562488,0.571913,0.591459,0.624589,0.626779,0.628872,0.634797,0.636811,0.636631,0.697046,0.695753,0.693594,0.690925,0.652251,0.65104,0.65327,0.653673,0.673353,0.668992,0.645479,0.645805,0.648661,0.650252,0.650652,0.652847,0.658066,0.657835,0.660559,0.65838,0.679161,0.679486,0.679627,0.682194,0.683178,0.682206,0.684675,0.680697,0.678934,0.679972,0.677731,0.674631,0.672072,0.670124,0.681058,0.689013,0.701349,0.706467,0.707376,0.708238,0.705091,0.704817,0.705213,0.704664,0.702564,0.705452,0.712345,0.704253,0.705675,0.705902,0.70455,0.704621,0.705334,0.704907,0.705914,0.703598,0.703661,0.703539,0.708826,0.713027,0.712478,0.712545,0.716287,0.715202,0.708826,0.709053,0.708387,0.705781,0.709457,0.703504,0.702811,0.703128,0.707121,0.702822,0.704213,0.707725,0.704127,0.704997,0.699229,0.703136,0.703057,0.704017,0.704891,0.702666,0.696415,0.69551,0.699719,0.698378,0.712698,0.705836,0.70131,0.702203,0.696932,0.698116,0.697422,0.698398,0.701263,0.69926,0.708285,0.701894,0.701553,0.701588,0.702195,0.706232,0.705526,0.697132,0.699209,0.699601,0.706463,0.707446,0.706463,0.708026,0.708834,0.70812,0.696454,0.699186,0.696262,0.696446,0.69977,0.69765,0.700416,0.700553,0.698351,0.694389,0.697109,0.697661,0.698002,0.699311,0.70421,0.698382,0.699182,0.70187,0.703453,0.701854,0.694883,0.696525,0.696388,0.699088,0.695663,0.699002,0.699617,0.700585,0.702485,0.706412,0.710597,0.711079,0.709559,0.710205,0.707297,0.710229,0.711138,0.711436,0.712447,0.743957,0.707094,0.713348,0.717459,0.719116,0.724062,0.762795,0.769805,0.779289,0.756489,0.72735,0.784077,0.790053,0.797374,0.778693,0.808793,0.828775,0.854407,0.800246,0.738459,0.815502,0.781424,0.801751,0.737319,0.758382,0.766157,0.700914,0.721883,0.733651,0.697834,0.662181,0.727193,0.726182,0.724042,0.701094,0.72838,0.74422,0.816544,0.655194,0.662777,0.647639,0.627053,0.647411,0.604501,0.573915,0.610414,0.581949,0.581247,0.565067,0.578669,0.612711,0.67706,0.657961,0.657859,0.656471,0.65327,0.630043,0.593595,0.573813,0.642125,0.563491,0.626089,0.605273,0.625619,0.568594,0.506693,0.458011,0.460687,0.356766,0.339626,0.331996,0.317849,0.332286,0.36411,0.330209,0.323727,0.293757,0.258159,0.254072,0.262215,0.259742,0.250188,0.251313,0.23217,0.222291,0.247045,0.233569,0.22291,0.196443,0.170618,0.168596,0.154461,0.184624,0.178005,0.20399,0.215382,0.248785,0.254714,0.302123,0.381662,0.377857,0.328394,0.316834,0.296852,0.240916,0.231178,0.215868,0.188535,0.161632,0.137266,0.127465,0.105011,0.0846135,0.0735979,0.073304,0.0684408,0.0680137,0.0674141,0.0686799,0.104799,0.12078,0.151142,0.182339,0.234897,0.260173,0.231629,0.241394,0.227381,0.22666,0.176641,0.128347,0.112703,0.113463,0.0932308,0.0788098,0.0745423,0.0733863,0.0741974,0.079425,0.0983134,0.132649,0.191458,0.253989,0.309784,0.35974,0.380616,0.369843,0.312379,0.288302,0.265075,0.247414,0.235669,0.233863,0.204586,0.159826,0.136435,0.112052,0.0918592,0.0772737,0.072579,0.0625039,0.062406,0.0617045,0.0619475,0.0632759,0.0630486,0.0629977,0.0627155,0.0631701,0.0650002,0.0661562,0.0683859,0.0885087,0.112229,0.122856,0.124412,0.134664,0.122347,0.13531,0.137093,0.134628,0.116014,0.103514,0.0980116,0.0889241,0.0779751,0.0782729,0.0737468,0.0780065,0.0753378,0.071568,0.0730845,0.0730414,0.0743581,0.0707999,0.103623,0.135091,0.143685,0.143747,0.111986,0.104595,0.117699,0.0970124,0.0743189,0.065153,0.0858048,0.0923216,0.0934581,0.0891122,0.0755181,0.0924157,0.0852836,0.0747186,0.0697105,0.0749342,0.0731864,0.0736998,0.0735783,0.0757963,0.0777439,0.102996,0.125553,0.128974,0.139738,0.135573,0.11737,0.120294,0.114694,0.113357,0.106163,0.0805615,0.0644829,0.0633112,0.0631466,0.0630917,0.0609678,0.0613949,0.0613205,0.0612695,0.061293,0.0606386,0.0604074,0.0612695,0.0774461,0.0952411,0.0875525,0.124851,0.169897,0.176046,0.179702,0.208105,0.176222,0.171355,0.194252,0.194993,0.159281,0.178303,0.161052,0.117801,0.129334,0.106186,0.126987,0.106394,0.123491,0.139331,0.130357,0.14142,0.130502,0.134311,0.135522,0.136341,0.140526,0.142286,0.143833,0.141086,0.129522,0.131286,0.128848,0.129863,0.130306,0.122586,0.132477,0.133061,0.13386,0.134107,0.126336,0.125952,0.13283,0.132528,0.141298,0.136302,0.135667,0.134773,0.136407,0.140738,0.145377,0.163839,0.144033,0.143152,0.143426,0.14912,0.141862,0.148289,0.164078,0.142258,0.134307,0.136744,0.143751,0.161915,0.175681,0.220794,0.241539,0.267956,0.296515,0.316427,0.372226,0.397251,0.418788,0.459163,0.49219,0.520064,0.57861,0.616065,0.637234,0.680011,0.691575,0.688883,0.681191,0.6873,0.692344,0.722584,0.677323,0.704241,0.700428,0.726574,0.796664,0.765648,0.753296,0.750486,0.744866,0.748801,0.740838,0.688143,0.701415,0.701008,0.674486,0.698151,0.69214,0.716052,0.714359,0.699084,0.743146,0.716393,0.714265,0.722733,0.703696,0.723693,0.719524,0.718203,0.719649,0.703136,0.694287,0.699213,0.69906,0.69995,0.688758,0.693911,0.70613,0.685168,0.682127,0.685925,0.693711,0.692877,0.693057,0.689017,0.685866,0.688895,0.689722,0.691348,0.688495,0.692199,0.682359,0.683307,0.691485,0.685756,0.6815,0.707556,0.70466,0.67844,0.683099,0.708673,0.706177,0.703571,0.682782,0.686599,0.693002,0.688887,0.689843,0.691478,0.729062,0.732922,0.72358,0.723392,0.726154,0.726554,0.741716,0.742719,0.706682,0.741794,0.742911,0.704433,0.743307,0.741257,0.699781,0.703939,0.700118,0.698492,0.701278,0.702364,0.701866,0.742974,0.743048,0.704966,0.733588,0.701972,0.699374,0.70343,0.741453,0.743632,0.744263,0.741896,0.740987,0.706721,0.706612,0.744984,0.747296,0.747461,0.745341,0.740505,0.705248,0.708775,0.742045,0.713861,0.714002,0.708904,0.708571,0.712576,0.713187,0.721272,0.721099,0.720731,0.718474,0.7093,0.704276,0.707921,0.70939,0.712639,0.705287,0.704597,0.706377,0.696164,0.696889,0.702344,0.694522,0.696207,0.699025,0.69877,0.700545,0.699531,0.700534,0.705616,0.702505,0.694303,0.69799,0.7006,0.704938,0.706298,0.700855,0.700381,0.699652,0.700785,0.699115,0.703959,0.704974,0.702101,0.705938,0.706333,0.706302,0.709672,0.701098,0.7496,0.747868,0.71171,0.716836,0.754887,0.752128,0.748836,0.703116,0.700361,0.70696,0.749099,0.746367,0.751736,0.74092,0.741167,0.74576,0.757069,0.715966,0.71086,0.698645,0.701572,0.703645,0.719116,0.834555,0.833787,0.832211,0.836024,0.71037,0.711436,0.709049,0.712212,0.712478,0.758719,0.750545,0.747359,0.750349,0.746669,0.752285,0.7531,0.753766,0.754017,0.715041,0.726985,0.715386,0.71633,0.882528,0.714179,0.708826,0.713654,0.707709,0.700702,0.700248,0.708728,0.701298,0.709406,0.70999,0.716358,0.837443,0.898328,0.889354,0.884809,0.885608,0.808107,0.810721,0.819714,0.797679,0.790242,0.806896,0.822567,0.824954,0.799647,0.768042,0.785951,0.804275,0.855108,0.808377,0.807241,0.791401,0.78019,0.754875,0.797115,0.80797,0.765475,0.729599,0.773814,0.784587,0.86331,0.729227,0.791766,0.80971,0.651679,0.655778,0.661938,0.602969,0.544247,0.529065,0.522063,0.50779,0.486853,0.494192,0.462341,0.455934,0.445933,0.453888,0.456972,0.467349,0.450843,0.413866,0.412628,0.387838,0.378715,0.398426,0.434463,0.424611,0.412259,0.40019,0.463031,0.437316,0.425618,0.429224,0.424067,0.442692,0.481884,0.488714,0.455036,0.435153,0.395542,0.418114,0.431947,0.485305,0.563217,0.606225,0.747535,0.763006,0.769923,0.774426,0.75928,0.698135,0.653219,0.694072,0.665771,0.506043,0.450491,0.428091,0.413694,0.430964,0.417334,0.507732,0.478459,0.459907,0.589551,0.532271,0.450463,0.346926,0.34421,0.35213,0.388347,0.382896,0.397568,0.42967,0.41713,0.429862,0.387912,0.32109,0.287028,0.237589,0.301696,0.264468,0.256948,0.246148,0.295677,0.335907,0.375266,0.348795,0.349802,0.343066,0.293674,0.288925,0.271988,0.231504,0.184741,0.160637,0.154285,0.141145,0.120207,0.0963736,0.0805458,0.0662894,0.0643222,0.0647102,0.0645377,0.0636639,0.061873,0.0617476,0.0614772,0.0635737,0.0642007,0.063848,0.0638363,0.063656,0.0644398,0.0639578,0.0651922,0.0649962,0.0643026,0.061971,0.062308,0.0621865,0.0617398,0.0615752,0.0615125,0.063174,0.0888888,0.0960797,0.142779,0.149398,0.140988,0.165986,0.14122,0.115724,0.115826,0.10965,0.136282,0.13908,0.148748,0.147192,0.138488,0.113467,0.110556,0.11768,0.0996222,0.090182,0.0820467,0.0763175,0.0745462,0.0748009,0.0733784,0.0730336,0.0945631,0.122355,0.157075,0.19308,0.238287,0.2552,0.243648,0.20301,0.175183,0.156738,0.134217,0.105728,0.0956251,0.104152,0.0870744,0.0632563,0.0610736,0.0578053,0.0579621,0.0579503,0.0580052,0.0580366,0.0588791,0.0588164,0.0587067,0.0585852,0.0583657,0.0577779,0.0576995,0.0584441,0.0584833,0.058303,0.0584402,0.0584284,0.0577701,0.0580522,0.0580914,0.0580757,0.0579739,0.0580209,0.0581737,0.058013,0.093603,0.118546,0.125427,0.130717,0.132426,0.128527,0.14533,0.159548,0.168059,0.184545,0.189459,0.178103,0.173361,0.170281,0.178303,0.189448,0.183236,0.185948,0.183495,0.204178,0.22617,0.216648,0.207117,0.20667,0.205001,0.199436,0.229395,0.246144,0.248922,0.246211,0.255192,0.255933,0.293075,0.295395,0.293247,0.294231,0.304043,0.2909,0.31694,0.321286,0.316999,0.332897,0.344481,0.344277,0.343458,0.356131,0.369659,0.367484,0.408415,0.425411,0.450683,0.466385,0.477981,0.482671,0.523759,0.555732,0.584237,0.606429,0.649124,0.659595,0.6655,0.661597,0.64711,0.675238,0.681042,0.681673,0.685643,0.671441,0.68402,0.680536,0.676367,0.655445,0.689828,0.693496,0.688848,0.693817,0.694287,0.709668,0.713415,0.715664,0.715958,0.716957,0.718027,0.721664,0.723282,0.719622,0.718842,0.723486,0.78347,0.800066,0.827654,0.791786,0.850853,0.849187,0.834429,0.792405]

skip_factor = int(sys.argv[2])

data = pd.read_csv(sys.argv[1], usecols = ['queue density'])

data1 = []

for e in data['queue density']:
    data1.append(e)

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147]

out = []
computations = 0

for i in range(0, len(data1), skip_factor):
    if computations == len(baseline):
            break
    out.append(data1[i])
    computations += 1
    for j in range(1, skip_factor):
        print(j)
        if ((computations == len(baseline)) or (i + skip_factor >= len(baseline))):
            break
        print(i + skip_factor)
        val = (j*data1[i] + (skip_factor - j)*data1[i + skip_factor])/skip_factor
        
        out.append(val)
        print(val)
        computations += 1

if len(out) != len(data1):
    diff = len(data1) - len(out)
    for i in range(0 , diff):
        out.append(data1[len(data1) - 1 - i])

error = 0

for i in range(0, len(out)):
    error += (baseline[i] - data1[i])*(baseline[i] - data1[i])

error = error/len(baseline)

error = math.sqrt(error)

print(len(baseline))
print(len(data1))
print(len(out))

print("error is = ")
print(error)

plt.plot(x, baseline, label = "line 1")
plt.plot(x, out, label = "line 2")

plt.title('Baseline and for n == ' + str(skip_factor))
  
plt.legend()
plt.show()
