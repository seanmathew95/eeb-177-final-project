# 1 files combined:
# 	/home/eeb177-student/Desktop/eeb-177/eeb177-final-project/PyRate/pyrate_mcmc_logs/felidae_occ_1_marginal_rates.log

# 95% HPDs calculated using code from Biopy (https://www.cs.auckland.ac.nz/~yhel002/biopy/)

pdf(file='/home/eeb177-student/Desktop/eeb-177/eeb177-final-project/PyRate/pyrate_mcmc_logs/felidae_occ_1_marginal_rates_RTT.pdf',width=0.6*9, height=16.8)
par(mfrow=c(4,1))
library(scales)
L_hpd_m95=c(0.189933991535, 0.189933991535,0.189933991535,0.189933991535,0.189933991535,0.189933991535,0.190320076427,0.190320076427,0.190320076427,0.190320076427,0.189933991535,0.189598610689,0.189598610689,0.189598610689,0.189598610689,0.188656977923,0.18622394335,0.185008219733,0.188656977923,0.188430005236,0.187317462067,0.184568748957,0.182293957061,0.182480516066,0.182480516066,0.182480516066,0.182480516066,0.182293957061,0.182293957061,0.182293957061,0.182293957061,0.182293957061)
L_hpd_M95=c(0.269133362199, 0.269133362199,0.269133362199,0.269133362199,0.269133362199,0.269133362199,0.269133362199,0.269133362199,0.269133362199,0.269133362199,0.269133362199,0.268994558019,0.268994558019,0.269079618768,0.269079618768,0.269133362199,0.269133362199,0.269133362199,0.273746139454,0.273746139454,0.273746139454,0.273746139454,0.272935246199,0.273746139454,0.273746139454,0.273746139454,0.273746139454,0.273746139454,0.273746139454,0.273746139454,0.273746139454,0.273746139454)
M_hpd_m95=c(0.894557782143, 0.894557782143,0.0799828255066,0.0805199821199,0.0805199821199,0.0799828255066,0.0820781590757,0.0796068970946,0.0805199821199,0.0677515102863,0.067434952117,0.067434952117,0.067434952117,0.067434952117,0.067434952117,0.067434952117,0.0618894237202,0.0594240964506,0.0453571947198,0.0361080345959,0.0318163967011,0.0290204890739,0.0280649201221,0.0280649201221,0.0310716010589,0.0302806915023,0.0290204890739,0.0290204890739,0.0290204890739,0.0290204890739,0.0290204890739,0.0290204890739)
M_hpd_M95=c(1.54585806887, 1.54585806887,0.157488273542,0.157488273542,0.157488273542,0.157488273542,0.15853890996,0.15458869998,0.157488273542,0.152350693553,0.152350693553,0.152350693553,0.152350693553,0.152350693553,0.152350693553,0.152350693553,0.153898799768,0.155752870596,0.149644439668,0.148094236261,0.148094236261,0.148094236261,0.148094236261,0.148094236261,0.152323772724,0.152323772724,0.152323772724,0.152323772724,0.152323772724,0.152323772724,0.152323772724,0.152323772724)
R_hpd_m95=c(-1.31588923894, -1.31588923894,0.0425282576045,0.0459652041292,0.0439428732907,0.0439428732907,0.0439428732907,0.0455206400799,0.0510807241298,0.0628787562193,0.0597892005303,0.0628787562193,0.0560489530272,0.0560489530272,0.0560489530272,0.0555073777179,0.0561368572764,0.0555073777179,0.0439428732907,0.0597892005303,0.057421351097,0.0555073777179,0.0553585194663,0.0536996284452,0.0528178844863,0.0536996284452,0.0553585194663,0.0547689914833,0.0547689914833,0.0547689914833,0.0547689914833,0.0547689914833)
R_hpd_M95=c(-0.663915166126, -0.663915166126,0.15849695532,0.161153326328,0.159154132711,0.159154132711,0.15929284008,0.160588164267,0.165523194524,0.174103436934,0.174103436934,0.176227514811,0.170162613831,0.170162613831,0.170162613831,0.170748108606,0.179177304642,0.180963303867,0.180963303867,0.203636843996,0.204360153781,0.204360153781,0.206809738006,0.206809738006,0.206809738006,0.20962159484,0.211748493347,0.211748493347,0.211748493347,0.211748493347,0.211748493347,0.211748493347)
L_mean=c(0.226635340245, 0.226635340245,0.226635340245,0.226614797294,0.22662048526,0.226606484153,0.226529001027,0.22655635137,0.226248477402,0.226213788475,0.226253281048,0.226126885904,0.226144672149,0.226080198877,0.226104569279,0.226291462897,0.226984928819,0.227505452246,0.227550115517,0.227702374287,0.227852765419,0.228389481423,0.228398463756,0.228481628471,0.228505303672,0.228505303672,0.228505303672,0.228405278104,0.228350858735,0.228350858735,0.228350858735,0.228350858735)
M_mean=c(1.20684374009, 1.20684374009,0.11831694232,0.118241628909,0.118329102061,0.118359307926,0.118265637408,0.117709431728,0.116117085054,0.112700407493,0.111969191199,0.111641376578,0.111578897775,0.111508680317,0.111522065707,0.111167762486,0.109651012021,0.108093379401,0.107070148051,0.106157865653,0.105424967211,0.104330749538,0.1040446206,0.103982379447,0.103702358084,0.103680093422,0.103835579876,0.103819054632,0.103819054632,0.103819054632,0.103819054632,0.103819054632)
R_mean=c(-0.980208399849, -0.980208399849,0.108318397925,0.108373168385,0.108291383199,0.108247176227,0.108263363619,0.108846919642,0.110131392348,0.113513380983,0.11428408985,0.114485509326,0.114565774374,0.11457151856,0.114582503572,0.115123700411,0.117333916798,0.119412072845,0.120479967467,0.121544508634,0.122427798208,0.124058731885,0.124353843156,0.124499249023,0.124802945587,0.124825210249,0.124669723795,0.124586223472,0.124531804103,0.124531804103,0.124531804103,0.124531804103)
trans=0.5
age=(0:(32-1))* -1
plot(age,age,type = 'n', ylim = c(0, 0.301120753399), xlim = c(-33.6,1.6), ylab = 'Speciation rate', xlab = 'Ma',main='felidae' )
polygon(c(age, rev(age)), c(L_hpd_M95, rev(L_hpd_m95)), col = alpha("#4c4cec",trans), border = NA)
lines(rev(age), rev(L_mean), col = "#4c4cec", lwd=3)
plot(age,age,type = 'n', ylim = c(0, 1.70044387575), xlim = c(-33.6,1.6), ylab = 'Extinction rate', xlab = 'Ma' )
polygon(c(age, rev(age)), c(M_hpd_M95, rev(M_hpd_m95)), col = alpha("#e34a33",trans), border = NA)
lines(rev(age), rev(M_mean), col = "#e34a33", lwd=3)
plot(age,age,type = 'n', ylim = c(-1.44747816283, 0.232923342682), xlim = c(-33.6,1.6), ylab = 'Net diversification rate', xlab = 'Ma' )
abline(h=0,lty=2,col="darkred")
polygon(c(age, rev(age)), c(R_hpd_M95, rev(R_hpd_m95)), col = alpha("#504A4B",trans), border = NA)
lines(rev(age), rev(R_mean), col = "#504A4B", lwd=3)
plot(age,age,type = 'n', ylim = c(0, max(1/M_mean)), xlim = c(-33.6,1.6), ylab = 'Longevity (Myr)', xlab = 'Ma' )
lines(rev(age), rev(1/M_mean), col = "#504A4B", lwd=3)
n <- dev.off()