#!/usr/bin/env python
from numpy import * 


data_1=[array([3.689526,4.492594,1.136109,3.01816,2.93801,4.462791,3.22432,2.404226,2.284019,0.448146,2.937133,1.973995,2.556702,0.18022,2.925396,0.449261,0.687029,1.022648,5.201175,1.463196]),
array([2.798002]),
array([0.006389,3.302159,2.683542,1.975041,0.051651,0.946652,0.016477,0]),
array([9.405254,9.864532]),
array([8.565394,9.954958,5.250403]),
array([9.804988]),
array([6.869952,8.406628,6.944539,6.129483,6.008485,7.782962,10.413864,9.964173,10.108603,7.503621,5.488353,7.746764,5.607961,7.573803,10.158234,7.321786,5.026475]),
array([6.806865,10.785595]),
array([0.088372]),
array([0.011182,1.459433,0.521366,7.29898,3.285352,0.001744,2.357811,0.526119,0.010121,0.005332,0.006714,0.995599,2.361626,2.223432,0.12769,3.175287,4.543085,1.008949,0.001347,0.141789,1.487172,2.643907,2.240263,0.201351,1.478869,6.781369,0.612202,0.269929,1.841988]),
array([0.010787,2.067303,1.211627,3.16427,1.218466,0.436438,2.476808,1.963597,1.236269,0.095719,0.094748,0.078854]),
array([13.274239]),
array([13.093788]),
array([3.351617,3.247973,3.250526,3.446989,1.481096,4.257476,4.559546,4.991217,7.853053,6.517742,4.071983,1.294089,1.344027,2.29395,3.378946,0.609582,3.972034,3.920123,4.776917,2.740867,3.155221,2.153593,0.991206,0.868019,3.412347,5.095882,7.804747,2.623679,7.658147,5.080395,3.649608,2.58165,3.292248,8.094071,9.876735,6.943181,5.603161,3.142241,4.472399,3.38862,3.811673,1.687972,1.984743,2.332201]),
array([4.17665,3.211451,4.858943,3.080305]),
array([3.802421,8.489962,8.031509]),
array([7.922971,7.845218,5.801837]),
array([7.989502,32.247771,21.478311,14.907474,16.176662,8.01305,11.884975,5.351904,10.307183,14.856734,18.711864,6.602173,13.047408,10.119477,15.546619,12.877061,15.700938,9.399444,8.253069,6.974851,12.03484,12.443919,6.26924,15.442279,9.985596,2.441011,6.3465,18.937071,6.566066,12.672057,17.24786,7.281935,7.311036,11.643494,18.16148,12.624455,2.625895,1.906717,3.634783,4.037041,3.980844,2.153157,4.868362,3.590209,4.852855,2.340685,4.742492,2.64413,2.557104,3.598114,2.152241,4.291128,4.052752,4.383332,3.5915,3.238982,2.551497,3.932639,4.261479,4.384503,4.32949,3.102636,1.490647,3.991253,3.62752,4.074025,4.177093,1.170873,1.719609,1.700595,0.113285,0.831711,1.577171,0.847674,4.236415,4.006646,0.002758,2.257972,0.005772,5.158124,3.772742,5.219157,4.156771,6.565093,5.931743,4.400132,6.787582,4.235167,2.208975,2.128247,0.117585,1.977624,2.3501,2.552262,2.28255,3.058807,2.858358,3.105009,3.086304,2.842817,2.776111,3.393623,3.120019,2.78836,3.209256,3.548135,2.852019,0.353507,4.966036,3.475647,0.006536,1.535215,20.283717,21.846881,7.813496,4.69795,1.950654,0.941766,4.163689,2.814599,2.847825,2.232367,0.400814,4.159119,6.008775,4.334193,3.94138,16.049163,10.971574,13.353953,17.426769,7.527087,12.214594,3.091642,13.095707,4.540243,6.867273,0.014026,0.096079,0.111384,27.093528,21.588822,4.702885,7.212231,0.096914,0.119383,4.020924,0.031515,0.064879,1.300525,8.946001,16.883852,9.409574,1.329501,1.710267,1.952407]),
array([12.136168,9.997852,8.462259,6.256626,8.789106,3.142325,4.501989,3.408261,4.225896,3.618193,4.281455,3.814503,4.271146,3.562644,4.631706,2.21895,0.45209,1.690577,1.040211,0.351355,1.537745,0.37835,1.808449,1.533798,0.039985,1.857594,5.038838,15.219466,0.109371]),
array([3.033012,2.709761,3.52319,2.682359,3.146831,2.701537,3.26197,2.678677,2.432069,2.644004,3.290948,3.166919,3.256005,2.70927,2.858122,4.831071,2.658568,0.627366,2.341251,4.888714,4.671023,3.317065,5.235065,1.100858,1.205745,5.148305,5.203024,3.378104,3.663132,4.29432,3.930539,0.489941,2.443592,1.066163,0.138872,3.060271,2.801915,3.063045,2.627468,2.997699,3.127012,1.858978,0.78572,5.932801,0.589602,0.336843,0.365422,0.989853,1.45566,0.739066,1.663066,1.262094,1.317739,0.827904,1.401427,5.371046,4.238861,6.194687,4.001744,1.726483,0.379002,0.095552,6.394357,1.433752,2.003946,0.7392,0.723548,0.139227,1.899849,2.157801,0.548889,15.556661,1.909141,1.208054,1.473101,2.249119,0.071996,0.123505,0.039335,5.876309,9.619302,9.943815,9.163466,6.149587,6.228367,3.089961,5.722843,0.004339,0.09498,0.110483,0.102922,16.555439,0.005801,0.00252,3.480757,0.733534,0.523824,8.008784,0.015409,0.047324,0.00283,0.010068,7.866969,5.403698]),
array([0.033289]),
array([3.851718,3.227659,3.099352,4.110061,2.914538,2.881676,4.631965,3.923882,2.07857]),
array([0.01066,0.003301,1.333903,0.011073,0.001973,3.213961,0.633571,0.001505,1.428423,0.003995,1.911048,0.003977,0.002911,2.315881,1.505288,1.390023,2.501848,0.508328,1.217936,2.181897,2.473484,1.705832,0.631438,0.797848,1.540073,1.522014,0.917273,0.006558,0.070886,0.096922,1.296399,0]),
array([2.391937]),
array([4.57325,5.410388,3.1379]),
array([1.242279,0.940591]),
array([7.426277]),
array([6.024696,5.167512,10.183446,5.51902,2.625464,3.405305,1.899897,4.48196,4.845519,2.142495,3.092568,4.137615]),
array([0.588103,1.984893,0.768442,0.002855,0.009872,0.005559,0.006427,3.543781,0.278717,0.208867,2.145002,0.48051,3.498837,0.91068,0.069629,0.345747,2.460087,0.056164,0]),
array([1.352668]),
array([0.710856]),
array([2.95064,1.810759,4.005634,2.181994,3.306444,3.759975,3.611784,3.037725,2.493934,3.777111,2.78469,3.037729,1.520208,0.355837,1.145693,0.452185,4.333092,0.475316,1.306112,0.847112,4.914722,5.065236,3.163794,2.685213,3.286136,2.817937,3.254889,2.609851,3.363318,3.94483,3.428086,8.812127,4.914731,3.687043,6.129312,3.584685,3.54939,1.865849,1.97523,2.13785,2.723743,4.041997,5.135432,0.187752,1.484648,3.358238,3.464468,3.958336,3.497546,4.586954,11.46482,3.901382,3.408775,2.368114,0.784212,4.633078,1.675915,2.682352,2.868498,3.03753,0.679853,2.559682,2.424025,2.166728,1.939921,1.30684,3.097642,3.11838,0.685969,2.16778,0.618376,0.563335,0.321462,0.448035,2.6123,4.406704,4.938846,2.498009,1.920249,0.265397,1.299852,2.171584,1.196843,0.353039,0.137052,1.694678,1.643535,2.264451,2.987632,2.340411,1.939382,1.916332,2.294027,1.225631,1.668448,2.270827,0.554943,0.367969,2.029756,2.527296,1.598966,0.750843,0.270496,0.415562,0.739865,0.184385,0.468202,1.102355,3.626371,2.84585,0.412211,2.400574,0.595423,0.856958,2.964081,1.867372,1.596746,3.049838,2.925898,3.739205]),
array([4.167961]),
array([3.087174,2.427416,2.099598]),
array([2.343942]),
array([1.092089,1.266403,1.616943,0.157376,1.147178,0.041543,0.110711,0.078415,0.848375]),
array([0.30714]),
array([0.042819,0.073395]),
array([1.002888]),
array([0.277156,0.001044,0.002857,0.002675,0.050629,0.064817,0.112762]),
array([0.025198]),
array([2.540393]),
array([1.641585,0.017453,0.009462,0.081705,0.025164,0.111925]),
array([0.215659,3.653273,2.84156,4.014472,4.616335,3.818182,3.945482,0.278026,2.632591,0.466088,2.683029,1.576876,2.203572,1.554979,3.739813,2.895302,4.534497,2.590517,0.058316,3.6381,0.959362,0.164373,1.38525,1.364408,1.74105,2.906466,0.366175,3.434293,2.697704,3.154148,2.895312,1.375435,0.304091,2.495847,0.717777,0.509692,1.3925,2.487523,4.149962,2.87454,5.066391,3.923879,3.829356,4.468457,3.725052,2.248749,0.022474,2.340639,2.376044,2.648647,3.078305,1.990014,2.401073,1.947509,1.041467,2.375083,0.214908,0.473169,0.616909,0.602679,0.258904,0.221236,0.536338,0.636152,0.404607,2.059898,0.500025,0.357956,1.386494,4.592626,3.303725,4.085156,3.385661,1.480304,0.057839,0.033302,0.096415,0.031143,3.258833,0.077088,0.052416]),
array([1.303974,0.06415,0.045882,0.021767]),
array([5.222367]),
array([0.051663,0.324981,0.397122,0.17822,2.733214,1.057767,1.008646,3.431935,4.652742,0.063598,0.244255,0.098318,0.079043]),
array([1.461251,1.055237]),
array([10.102122,5.710456]),
array([2.716213,3.285929,1.971196,3.018676,4.072743,3.154134,0.432481,0.866041,1.379764,0.504871,1.291481,0.531036,1.394461,0.477235,0.316803,0.448101,0.76765,1.255024,0.38053,0.152234,0.523155,1.696933,1.628759,0.676719,0.585539,0.084302,0.089265,0.032257,0.081002,0.123574,0.11317,0.110547,0.079071,1.252648,0.0556,0.251585,0.097148,0.031687,0.075642,0.125363,0.021615,0.053622,0.00527,0.04901,0.241698,0.019192,1.386413,0.220694,0.107514,0.046773,0.098656,0.013138,0.007893,2.529393,0.057703,0.026653,0.108403,0.049467,0.063214,0.098548,0.938072,0]),
array([6.236241,14.850575,4.166706,4.615693,2.383765,0.365249,4.888864,3.331464,1.602619,4.753056,4.642363,5.065214,2.142586,13.031624,24.491765,9.293021,1.578744,0.874254]),
array([6.816564,5.839864,9.762329,5.782442,6.499994,5.182436,9.942829,8.882335,7.114484,9.847048,4.979461,5.621084,7.664744,3.186564,18.203686,6.479554,4.932507,5.387618,19.184944,3.005201,8.507853,4.553988,8.018052,11.018919,8.960062,9.693129,2.697756,7.180727,9.616693,9.637818,11.232636,7.866697,3.883571,6.710421,8.650005,0.625926,0.322816,5.435663,9.053514,6.776719,5.783925,4.767059,8.131885,9.835033,8.2785,10.651645,6.620681,10.321101,8.84456,10.386009,8.221779,7.459115,9.578339,8.00918,7.909931,7.643317,4.929121,3.887046,3.15457,0.351746,5.955474,4.938431,4.168153,5.877901,3.419171,12.231239,5.912457,5.069901,9.992464,10.025138]),
array([5.538858,9.989673,9.819549,8.203608]),
array([4.067886,2.701192,5.197713]),
array([5.313952]),
array([5.847854]),
array([8.478421]),
array([6.92937,3.278615,4.894184,2.942961,3.421309,2.863786,3.748817,4.054405,3.068177,4.464541,0.300361,1.929132,2.326876,1.72792,0.432277,3.174549,4.006203,2.398678,3.548703,1.046614,1.186223,2.240509,5.147999,1.466876,2.813511,2.641007,3.75546,0.903126]),
array([4.18563,1.289112,1.062686,2.324705,1.779558,3.954651,2.479448,0.966374,1.067579]),
array([2.285768,0.857898,4.941714]),
array([8.25938,7.867643,9.629429,3.332837,2.251967,2.468951]),
array([4.852207,3.087789,2.904612,2.280533,2.273513,0.484206,3.042907,2.145646,1.896971,1.934118,2.424303,2.130696]),
array([0.300119]),
array([2.301309,1.235358,1.891102,3.366966,1.841538]),
array([6.539885,9.05391,9.003106,0.352707,8.492513,12.779279,3.412226,5.621035,10.648332,8.515595,5.409832]),
array([10.86027]),
array([1.655764,3.914885,3.49953,1.490043]),
array([3.16853,2.940017,2.814123,0.639142,1.200129,1.256096,0.47182,4.093474,0.047344,0.653529,1.550248,2.434869,0.088571,1.520567,1.509917,1.416188,0.11546,0.057339]),
array([4.576777,2.511707,4.535746,1.729324,1.701956,0.067317,0.071112,0.115819,4.719763]),
array([0.12159]),
array([9.210504,13.519915,8.107435,5.170463,6.245337]),
array([10.711904,6.039372,12.902566]),
array([10.107615]),
array([13.05096,10.558496]),
array([8.65866,9.485236,6.122896,5.694495,8.153102,9.601749,11.981848,10.596495,9.162902]),
array([0.769245,3.214807,3.296699,2.72878,3.044249,2.527306,3.788963,3.5149,1.140865,1.259261,4.804138,1.985321,1.964124,6.137523,3.153881,2.428579,1.245126,0.723129,1.585297,0.427964,2.836996,2.930119,3.119268,2.421331,2.51752,2.527865,2.349637,0.834922,2.438546,0.132475,2.227581,0.064069,1.444731,2.232151,0.056331,0.973233,0.649312,4.82694,2.381421,0.505096,0.435311,0.200055,2.27437,2.195842,0.023282,4.779361,0.035844,1.662589,0.704616]),
array([10.41488,8.900431,10.892055]),
array([3.186672,2.783167,3.193107,3.547453,2.795663,3.176874,3.561843,4.874735,0.914039,0.102061,1.640198,2.37449,1.821286,0.790165,1.668102,0.58177,0.391463,1.844581,2.679922,2.324225,0.445486,0.498074,0.657379,0.294797,0.037115,1.580793,0.540077,0.195879,2.432983,0.491782,2.386897,0.393914,0.569144,0.245978,0.514857,0.314928,1.494139,2.80782,0.885581]),
array([0.030052,0.011346,0.002332,0.284133,0.010108,0.745456,2.420459,1.999756,0.010159,1.988642,0.294517,1.974103,0.402757,0.56032,2.718934,1.961513,1.4188,1.154884,1.399903,0.464253,0.671217,2.050109,2.587925,1.670619,1.866848,1.596995,1.847482,2.247533,0.020885,0.014732,1.210092,1.337723,0.688485,0.771564,0.385542,0.174052,1.093169,0.127297,0.744443,0.270954,0.057784,0.030999,0.252966,0.238059,0.56849,0.331857,0.985813,0.498413,0.348313,0.228509,2.033865,0.292611,0.236102,0.684349,0.381288,0.694883,0.938179,0.946202,0.162065,1.38195,0.052677,0.077092,0.073031,1.030611,0.095697,0.122483,0.070633,0.107145,0.729297,0]),
array([1.330646,1.569069,0.506524,0.791148,0.892737,0.629282,1.393013,0.030181,0.084917,0.043673,0.048148,0.098479,0.020856,0.033923,1.819663,0.154621,0.056047,0.092373,0.024911,0.007845,2.16016,0.009267,1.659141,0.123318,0.088223,0.018447,1.487156]),
array([1.612549,0.937795,1.625884,1.469107,1.547841,0.852309,1.519697,2.57445,0.187658,0.873674,0.855024,0.829316,0.179595,0.697028,1.760551,0.067228,0.073954,0.087743,0.032952,0.058339,0.005134,0.009989,0.010072,2.521523,1.153952,1.002076,0.16512,0.436405,0.909274,0.022529,0.026953,2.064277,0.019154,0.080636,0.112153,0.099798,0.309034,0.746704,2.468238,0.957458,1.233672,0.09418,2.122554,0.880128,2.306379,0.032162,0.054849,0.214917,0.09118,1.706936,2.488885,2.459332,0.047091,0.012177,0.042296,0.101522,0.055621,0]),
array([0.683664,0.010553,0.008368,2.246293,0.697444,0.916139,0.52938,1.800054,1.112146,1.199312,0.833943,0.007187,2.53938,0.004516,0.257466,0.00112,0.001416,2.440318,2.046162,0.994397,0.132689,3.120048,3.388905,5.26459,2.122955,1.72284,4.637206,5.309207,0.663721,1.397863,0.006095,0.085445,2.038612,0.004073,2.211586,0.816829,0.939195,2.055035,5.287642,1.67748,3.476131,2.815984,3.635303,4.727657,3.36799,0.716294,0.234527,0.201151,0.13811,0.372388,0.715119,0.51042,0.017306,0.100146,0.086356,1.347738,1.577691,0.457544,0.599808,0.487328,0.708333,0.098511,0.32796,0.598224,0.533757,0.959114,0.440104,1.656102,0.342081,0.766767,1.210795,0.346097,0.004904,1.250177,1.320311,0.101563,0.009467,1.253817,1.999373,1.78448,0]),
array([0.605545,0.011621,0.702364,0.946376,0.139106,0.158395,0.906043,0.064599,0.064851,1.421698,2.535984,0.031613,0.083278,0.066482,0.019554,0.322068,0]),
array([6.185435,1.149514,7.080873,5.67138,7.686604]),
array([7.870951]),
array([1.537706]),
array([12.29463,10.402926,15.946297,13.671987,15.538684,15.631043,11.619168,9.886963,10.152805,13.031027,10.846596,6.500087,15.723441,15.841016,12.015243,8.180305,11.548872,8.824692,7.631474,8.462414,7.519556,7.938542,5.985559,0.745796,16.166076,12.859986,16.283821,15.875114,12.44587,21.260734,16.024196,15.910568,13.753644,16.832417]),
array([13.784364,14.447449]),
array([18.434117,19.023764,20.738381]),
array([14.896772,10.583028,15.075841,5.375247,15.316035,12.547361,18.164405,14.39562,14.740491]),
array([14.879033,16.407775,16.193873,11.841082,16.110065,15.762808,15.150847,14.096277,14.296986]),
array([15.647291,19.675188,13.837703,13.715445,13.649042]),
array([12.949403,8.51368,14.9353,14.687765,15.724413,13.82233]),
array([16.809238,16.608139,15.550504]),
array([13.975741,13.839996]),
array([22.523729,13.416671,15.684963]),
array([14.855494,20.236401,19.960638,16.153481,19.326955,16.051129,15.051421]),
array([1.193125,0.009546,0.251609,3.352963]),
array([3.056103,2.298091,3.68139,2.867838,2.829304,2.094164,4.212541,1.730457,1.629663,1.065549,1.265472,0.157953,0.106552,0.039313,0.046233,0.001595,0.005599,0.002169,0.007776,0.775087,1.651538,0.027227,0.589008,0.108949,0.027635,0.0618,0.248417,0.070947,0.013034,1.338641,0.013394,0.02294,0.124741,0.100713,0.039421,0.005133,0.104102,0.034431,0.095999,0.053286,0.069868,0.108203,0.005929]),
array([0.003619,0.005276,0.003333,0.117282,0.112378,0.025345]),
array([3.044667,4.438482,1.748906,0.707323,0.046487,0.53371,1.183883,2.583761,1.052037,0.082896,1.780302,0.025352,0.430024,1.986986,0.055236,0.045888,0.126062,1.122585,0.924046,0.992817,1.074796,0.086139,0.095184]),
array([0.99903,1.728711,0.925494,1.790715,1.137024,1.230567,0.811017,0.088084,0.063462,0.021388,0.086936,0.103498,0.088696,0.035729,0.117635,0.07142,0.039905,0.118173,0.03973,0.081398,0.023055,0.069303,0.569851,0.033707,0.087319,2.528424,2.212224,0.078575,0.069855,0.101022,0.101568]),
array([3.504255,3.0764,2.217954,1.845895,0.762908,1.337952,0.67466,1.728683,1.315292,1.143262,0.494699,0.809159,1.122822,3.667212,1.548619,0.509046,1.635312,0.387161,1.655459,4.346654,0.111638,0.515157,0.463556]),
array([0.062115,0.077698,0.564267,1.541854,0.440811,0.397828,0.610887,0.027063,0.034475,0.115995,0.075407,0.671018,2.017091,0.022987,2.032992,0.077001,0.030302,2.367445,2.134792,0.094047,0.009186]),
array([1.016123]),
array([2.721758]),
array([0.91495]),
array([0.178094]),
array([11.301535]),
array([2.128897]),
array([12.258131]),
array([1.1208,0.741178])
]

d=[data_1]
names=[ 'felidae_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Acinonyx','Acinonyx_aicha','Acinonyx_jubatus','Adelphailurus','Adelphailurus_kansensis','Amphimachairodus','Amphimachairodus_coloradensis','Amphimachairodus_giganteus','Caracal','Caracal_caracal','Caracal_serval','Diamantofelis_ferox','Diamantofelis_minor','Dinofelis','Dinofelis_palaeoonca','Drepanodon','Epimachairodus','Felidae','Felinae','Felis','Felis_domesticus','Felis_lacustris','Felis_libyca','Felis_nigripes','Felis_obscura','Felis_platensis','Felis_prisca','Felis_rexroadensis','Felis_silvestris','Felis_youngi','Herpailurus','Homotherium','Homotherium_crusafonti','Homotherium_idahoensis','Homotherium_johnstoni','Homotherium_serum','Homotherium_venezuelensis','Leopardus','Leopardus_braccatus','Leopardus_pardalis','Leopardus_tigrinus','Leopardus_vorohuensis','Leopardus_wiedii','Lynx','Lynx_canadensis','Lynx_longignathus','Lynx_lynx','Lynx_pardinus','Lynx_proterolyncis','Lynx_rufus','Machairodontinae','Machairodus','Machairodus_catocopis','Machairodus_irtyschensis','Machairodus_ischimicus','Machairodus_kabir','Machairodus_kurteni','Megantereon','Megantereon_cultridens','Megantereon_eurynodon','Megantereon_hesperus','Megantereon_megantereon','Megantereon_nihowanensis','Megantereon_whitei','Metailurus','Miomachairodus','Miracinonyx','Miracinonyx_inexpectatus','Miracinonyx_studeri','Neofelis_nebulosa','Nimravides','Nimravides_galiani','Nimravides_hibbardi','Nimravides_pedionomus','Nimravides_thinobates','Panthera','Panthera_blytheae','Panthera_gombaszoegensis','Panthera_leo','Panthera_leo_atrox','Panthera_onca','Panthera_pardus','Panthera_tigris','Paramachaerodus','Pratifelis_martini','Prionailurus_bengalensis','Pseudaelurus','Pseudaelurus_aeluroides','Pseudaelurus_africanus','Pseudaelurus_intrepidus','Pseudaelurus_lorteti','Pseudaelurus_marshi','Pseudaelurus_quadridentatus','Pseudaelurus_romieviensis','Pseudaelurus_stouti','Pseudaelurus_turnauensis','Pseudaelurus_validus','Puma','Puma_concolor','Puma_yagouaroundi','Smilodon','Smilodon_fatalis','Smilodon_gracilis','Smilodon_populator','Smilodon_riggii','Therailurus','Uncia_mercerii','Uncia_spelea','Vinayakia','Viretailurus','Vishnufelis','Xenosmilus_hodsonae']
def get_taxa_names(): return taxa_names