<!---# 1 run on 10 000 lines


## k2 sccore for parameter estimation

### ess=10 for structure learning priors:

random:
- full: -83716.11
- desired: -5498.7417

BIC:
- full: -96348.92
- desired: -2750.0156

Bdeu:\
this score was estimated to take 33 days to complete the variable elimination of the desired distribution so I stopped it.
- full:
- desired: 

BDs:
- full: -97380.44
- desired: -2769.0144

K2:
- full: -99207.66
- desired: -2794.0796

### ess=100 for structure learning priors:

these ran quicker with the prior, decreseing the prior might make it more accurate but run quicker

Bdeu:
- full: -82066.55
- desired: -2948.395

BDs:
- full: -97783.914
- desired: -2694.8018

### ess=50 for structure learning priors:

Bdeu:
- full: -81801.016
- desired: -2977.7705

BDs:
- full: -98273.375
- desired: -2764.6963

### ess=1000 for structure learning priors:

Bdeu:
- full: 
- desired: 

BDs:
- full: -101985.39
- desired: -2875.7534


## BDeu score for parameter estimation, ess=5:

###  ess=10 for structure learning priors

BIC:
- full: -98327.16,
- desired: -2823.7607,

Bdeu:
- full:
- desired: 

BDs:
- full:
- desired: 

K2:
- full: -97256.83
- desired: -2687.0728

## BDeu with ess=1000 for parameter estimation:

### ess=1000 for structure learning

#### LogLikelihood:
random:
- ran into error 

BIC:
- full: -101404.875
- desired: -3206.0286

Bdeu:
- full: -86472.68
- desired: ran into error, int_rate not in graph

BDs:
- full: -103673.555
- desired: -3013.8362

K2:
- full: -98227.16
- desired: -3059.7332

Chow-Liu:
- full: -103353.125
- desired: -3203.9448

#### Correlation:

random:
- ran into error

BIC:
- accuracy: 0.5525150905432595
- f1: 0.0

Bdeu:
- ran into error

BDs:
- accuracy: 0.42160493827160495
- f1: 0.0

K2:
- accuracy: 0.4560126582278481
- f1: 0.07030827474310439

Chow-Liu:
- accuracy: 0.44537037037037036
- f1: 0.0


## ess=50 for structure learning:

### BDeu with ess=50 for parameter estimation:

#### LogLikelihood:
BIC:
- full: -95383.305,
- desired: -2759.7083,

Bdeu:
- full: -80765.58,
- desired: -2874.6968,

BDs:
- full: -inf,
- desired: nan,

K2:
- full: -97868.92,
- desired: -2827.8086,


#### Correlation:

BIC:
- accuracy: 0.5205479452054794,
- f1: 0.0,

Bdeu:
- accuracy: 0.5916515426497277,
- f1: 0.0425531914893617,

BDs:
- accuracy: 0.4661392405063291,
- f1: 0.0,

K2:
- accuracy: 0.4800389483933788,
- f1: 0.011111111111111112,


### Dirichelet with psuedo counts = 2 for parameter estimation:

#### LogLikelihood:

BIC:
- full: -97932.11,
- desired: -2815.4355,

Bdeu:
- full: -73792.07,
- desired: -2880.5122,

BDs:
- full: -inf,
- desired: nan,

K2:
- full: -99350.445,
- desired: -3041.5918,


#### Correlation:

BIC:
- accuracy: 0.4825700615174299,
- f1: 0.0,

Bdeu:
- accuracy: 0.6275331935709294,
- f1: 0.049910873440285206,

BDs:
- accuracy: 0.43148148148148147,
- f1: 0.0,

K2:
- accuracy:  0.5075187969924813,
- f1: 0.03223640026863667,




### Dirichelet with psuedo counts = 5 for parameter estimation:

#### LogLikelihood:

BIC:
- full: -100938.25,
- desired:  -2822.3438,

Bdeu:
- full: -84097.87,
- desired: -2912.1455,

BDs:
- full: -inf,
- desired: nan,

K2:
- full: -101178.82,
- desired: -2706.6191,


#### Correlation:

BIC:
- accuracy: 0.5309076682316118,
- f1: 0.0,

Bdeu:
- accuracy: 0.662083553675304,
- f1: 0.22919179734620024,

BDs:
- accuracy: 0.4398148148148148,
- f1: 0.0,

K2:
- accuracy:  0.47685185185185186,
- f1: 0.10648392198207696,



-->


## 1 run on 1000 lines: 

### Chow-Liu:

#### loglikelihood:
full: -6212.54,\
desired: -234.32318, 

#### Correlation:
accuracy: 0.1311871227364185,\
f1: 0.0,


## BDeu:( max_indegree = 4,3 - not much difference)


### SL: ess=5, PE: K2:

#### loglikelihood:
full: -5370.0, -5300.0, -5650.0, -5356.0\
desired: 

#### Correlation:
accuracy: 0.18275058275058276,0.16298076923076923,\
f1: 0.0,

### SL: ess=4, PE: K2:

#### loglikelihood:
full:  -5324.0, -5384.0, -4936.0, -5416.0\
desired: nan,

#### Correlation:
accuracy: 0.14451345755693581,0.16687370600414078,\
f1: 0.0,

### SL: ess=3, PE: K2:

#### loglikelihood:
full: -5300.0, -5132.0, -5516.0, -5290.0\
desired:

#### Correlation:
accuracy: 0.13193473193473193,0.19296066252587993,0.14699231117141565\
f1: 

### SL: ess=2, PE: K2:

#### loglikelihood:
full: -5230.0, -5344.0\
desired:


### SL: ess=10, PE: K2:

#### loglikelihood:
full: -5668.0, -5652.0\
desired:

### PE = BDeu

#### SL: ess = 4, ess =5
full: -5420.0, -5236.0

#### SL: ess = 4, PE = BDeu, ess =4
full: -5444.0

#### SL: ess = 4, PE = BDeu, ess = 10
full: -5604.0

#### SL: ess = 4, PE = BDeu, ess = 50
full: -5224.0

#### SL: ess = 4, PE = BDeu, ess = 20
full: -4870.0

### PE = Dirichlet

#### SL: ess = 4, pc = 1
full: -5304.0

#### SL: ess = 4, pc = 2
full: -5680.0, -5610.0

#### SL: ess = 4, pc = 0.25
full: -5100.0



## BIC ( BDeu 10 000 lines):

10 000 Lines:
ess =10
full LL: -58253.395	 Correlation accuracy: 0.3850815850815851
ess =10
full LL: -58855.836	 Correlation accuracy: 0.3805970149253731
ess =30
full LL: -59010.008	 Correlation accuracy: 0.45848757271285034
ess =30
full LL: -59599.25	 Correlation accuracy: 0.38269230769230766
ess =50
full LL: -59110.477	 Correlation accuracy: 0.34527162977867204
ess =50
full LL: -59044.062	 Correlation accuracy: 0.40048076923076925
ess =80
full LL: -59663.125	 Correlation accuracy: 0.4228855721393035
ess =80
full LL: -59668.28	 Correlation accuracy: 0.38849868305531166
ess =100
full LL: -59877.94	 Correlation accuracy: 0.3958041958041958
ess =100
full LL: -58866.535	 Correlation accuracy: 0.41025641025641024
ess =125
full LL: -59389.227	 Correlation accuracy: 0.38715513342379015
ess =125
full LL: -59054.258	 Correlation accuracy: 0.3808857808857809
ess =150
full LL: -59323.773	 Correlation accuracy: 0.4330357142857143
ess =150
full LL: -59314.305	 Correlation accuracy: 0.42950819672131146
ess =200
full LL: -59752.89	 Correlation accuracy: 0.35403726708074534
ess =200
full LL: -59979.96	 Correlation accuracy: 0.40576923076923077
ess =225
full LL: -60107.938	 Correlation accuracy: 0.4131944444444444
ess =225
full LL: -58344.05	 Correlation accuracy: 0.383989145183175
ess =250
full LL: -60501.19	 Correlation accuracy: 0.3929606625258799
ess =250
full LL: -59741.086	 Correlation accuracy: 0.446853516657853
ess =300
full LL: -59105.074	 Correlation accuracy: 0.4177683765203596
ess =300
full LL: -57862.1	 Correlation accuracy: 0.4341618191433104
ess =325
full LL: -61194.49	 Correlation accuracy: 0.4219114219114219
ess =325
full LL: -60493.06	 Correlation accuracy: 0.417306052855925
ess =350
full LL: -60133.98	 Correlation accuracy: 0.4352278545826933
ess =350
full LL: -60335.18	 Correlation accuracy: 0.4375
ess =400
full LL: -60095.773	 Correlation accuracy: 0.40029761904761907
ess =400
full LL: -56884.93	 Correlation accuracy: 0.43738656987295826



## BDS ( 10 000 lines):

ess: 10
full LL: -57693.5	 Correlation accuracy: 0.2885426809477442
ess: 10
full LL: -57314.96	 Correlation accuracy: 0.34209552017771194
ess: 10
full LL: -58014.79	 Correlation accuracy: 0.3013653013653014
ess: 20
full LL: -56909.555	 Correlation accuracy: 0.3246846846846847
ess: 20
full LL: -57566.586	 Correlation accuracy: 0.3017771701982228
ess: 20
full LL: -57558.312	 Correlation accuracy: 0.26358024691358023
ess: 30
full LL: -57016.035	 Correlation accuracy: 0.2957042957042957
ess: 30
full LL: -57331.42	 Correlation accuracy: 0.287893541058098
ess: 30
full LL: -57050.69	 Correlation accuracy: 0.2983595352016405
ess: 40
full LL: -57861.363	 Correlation accuracy: 0.28860759493670884
ess: 40
full LL: -57482.93	 Correlation accuracy: 0.2977022977022977
ess: 40
full LL: -57295.113	 Correlation accuracy: 0.31859649122807016
ess: 50
full LL: -57505.812	 Correlation accuracy: 0.2947052947052947
ess: 50
full LL: -57199.055	 Correlation accuracy: 0.3156843156843157
ess: 50
full LL: -56679.242	 Correlation accuracy: 0.3004101161995899



##  BIC ( Dirichlet different amount of lines):


1000 Lines:
pseudo count =1
full LL: -4927.0576	 Correlation accuracy: 0.22193877551020408
pseudo count =1
full LL: -3715.243	 Correlation accuracy: 0.2860215053763441
pseudo count =2
full LL: -4338.8643	 Correlation accuracy: 0.26666666666666666
pseudo count =2
full LL: -4483.0674	 Correlation accuracy: 0.2808080808080808
pseudo count =3
full LL: -4552.53	 Correlation accuracy: 0.25809435707678074
pseudo count =3
full LL: -4847.2197	 Correlation accuracy: 0.25795918367346937
pseudo count =4
full LL: -5053.7314	 Correlation accuracy: 0.1832579185520362
pseudo count =4
full LL: -4335.826	 Correlation accuracy: 0.23183673469387756
pseudo count =10
full LL: -3779.857	 Correlation accuracy: 0.30049261083743845
pseudo count =10
full LL: -5399.365	 Correlation accuracy: 0.216255442670537
pseudo count =30
full LL: -4918.598	 Correlation accuracy: 0.22028985507246376
pseudo count =30
full LL: -6344.2847	 Correlation accuracy: 0.21551020408163266
pseudo count =50
full LL: -1714.4171	 Correlation accuracy: 0.3717948717948718
pseudo count =50
full LL: -3294.9114	 Correlation accuracy: 0.4152046783625731
pseudo count =80
full LL: -8738.496	 Correlation accuracy: 0.2004675628287551
pseudo count =80
full LL: -4678.9546	 Correlation accuracy: 0.44333333333333336
pseudo count =100
full LL: -4290.1206	 Correlation accuracy: 0.3007246376811594
pseudo count =100
full LL: -2190.753	 Correlation accuracy: 0.3619047619047619
pseudo count =150
full LL: -6630.7363	 Correlation accuracy: 0.2661290322580645
pseudo count =150
full LL: -9837.79	 Correlation accuracy: 0.2613430127041742
pseudo count =200
full LL: -9054.832	 Correlation accuracy: 0.27040816326530615
pseudo count =200
full LL: -8659.652	 Correlation accuracy: 0.22606382978723405
pseudo count =250
full LL: -7910.7354	 Correlation accuracy: 0.2833333333333333
pseudo count =250
full LL: -10057.412	 Correlation accuracy: 0.19636617749825297
pseudo count =300
full LL: -9185.021	 Correlation accuracy: 0.2463768115942029
pseudo count =300
full LL: -9821.793	 Correlation accuracy: 0.233843537414966
pseudo count =350
full LL: -9638.411	 Correlation accuracy: 0.314975845410628
pseudo count =350
full LL: -5734.1064	 Correlation accuracy: 0.36

11000 Lines:
pseudo count =1
full LL: -62635.055	 Correlation accuracy: 0.3878787878787879
pseudo count =1
full LL: -61936.215	 Correlation accuracy: 0.4214029697900666
pseudo count =2
full LL: -62264.92	 Correlation accuracy: 0.39254079254079255
pseudo count =2
full LL: -62831.047	 Correlation accuracy: 0.3812754409769335
pseudo count =3
full LL: -63335.438	 Correlation accuracy: 0.3613682092555332
pseudo count =3
full LL: -62016.047	 Correlation accuracy: 0.393006993006993
pseudo count =4
full LL: -61947.223	 Correlation accuracy: 0.44137224782386075
pseudo count =4
full LL: -62308.465	 Correlation accuracy: 0.42345110087045573
pseudo count =10
full LL: -63226.406	 Correlation accuracy: 0.44769140853302164
pseudo count =10
full LL: -64350.973	 Correlation accuracy: 0.3916083916083916
pseudo count =30
full LL: -66841.54	 Correlation accuracy: 0.4072420634920635
pseudo count =30
full LL: -66548.58	 Correlation accuracy: 0.40326340326340326
pseudo count =50
full LL: -69604.81	 Correlation accuracy: 0.4177683765203596
pseudo count =50
full LL: -69943.586	 Correlation accuracy: 0.36479367866549606
pseudo count =80
full LL: -73417.234	 Correlation accuracy: 0.4393241167434716
pseudo count =80
full LL: -71866.555	 Correlation accuracy: 0.4207650273224044
pseudo count =100
full LL: -74927.03	 Correlation accuracy: 0.4225277630883131
pseudo count =100
full LL: -75355.266	 Correlation accuracy: 0.40240384615384617
pseudo count =150
full LL: -78955.51	 Correlation accuracy: 0.43317972350230416
pseudo count =150
full LL: -79619.8	 Correlation accuracy: 0.42089093701996927
pseudo count =200
full LL: -82478.31	 Correlation accuracy: 0.4453551912568306
pseudo count =200
full LL: -83692.31	 Correlation accuracy: 0.43676395289298514
pseudo count =250
full LL: -86751.375	 Correlation accuracy: 0.3753957485300769
pseudo count =250
full LL: -88473.09	 Correlation accuracy: 0.4153846153846154
pseudo count =300
full LL: -93130.66	 Correlation accuracy: 0.365445499773858
pseudo count =300
full LL: -90310.266	 Correlation accuracy: 0.38846153846153847
pseudo count =350
full LL: -94332.39	 Correlation accuracy: 0.3388937664618086
pseudo count =350
full LL: -94059.3	 Correlation accuracy: 0.386250565355043

21000 Lines:
pseudo count =1
full LL: -118177.12	 Correlation accuracy: 0.4128772635814889
pseudo count =1
full LL: -118504.94	 Correlation accuracy: 0.4289855072463768
pseudo count =2
full LL: -118340.19	 Correlation accuracy: 0.44596273291925465
pseudo count =2
full LL: -118107.33	 Correlation accuracy: 0.44776119402985076
pseudo count =3
full LL: -118990.42	 Correlation accuracy: 0.41730382293762575
pseudo count =3
full LL: -119114.66	 Correlation accuracy: 0.4552238805970149
pseudo count =4
full LL: -118935.766	 Correlation accuracy: 0.4525879917184265
pseudo count =4
full LL: -118441.91	 Correlation accuracy: 0.42581211589113255
pseudo count =10
full LL: -119888.3	 Correlation accuracy: 0.46442307692307694
pseudo count =10
full LL: -120344.016	 Correlation accuracy: 0.41821946169772256
pseudo count =30
full LL: -124356.31	 Correlation accuracy: 0.4411764705882353
pseudo count =30
full LL: -124829.44	 Correlation accuracy: 0.4426501035196687
pseudo count =50
full LL: -127341.234	 Correlation accuracy: 0.443307757885763
pseudo count =50
full LL: -126650.586	 Correlation accuracy: 0.4894230769230769
pseudo count =80
full LL: -131378.94	 Correlation accuracy: 0.45816372682044326
pseudo count =80
full LL: -132969.67	 Correlation accuracy: 0.44323835368611486
pseudo count =100
full LL: -133885.67	 Correlation accuracy: 0.468997668997669
pseudo count =100
full LL: -136230.88	 Correlation accuracy: 0.462111801242236
pseudo count =150
full LL: -142236.53	 Correlation accuracy: 0.4358974358974359
pseudo count =150
full LL: -143107.23	 Correlation accuracy: 0.46132971506105835
pseudo count =200
full LL: -149401.31	 Correlation accuracy: 0.4376646180860404
pseudo count =200
full LL: -150364.69	 Correlation accuracy: 0.43975155279503103
pseudo count =250
full LL: -152142.52	 Correlation accuracy: 0.4626865671641791
pseudo count =250
full LL: -155298.44	 Correlation accuracy: 0.4442493415276558
pseudo count =300
full LL: -162230.9	 Correlation accuracy: 0.4178053830227743
pseudo count =300
full LL: -161150.81	 Correlation accuracy: 0.4240165631469979
pseudo count =350
full LL: -163511.75	 Correlation accuracy: 0.44306418219461696
pseudo count =350
full LL: -164484.97	 Correlation accuracy: 0.4441602728047741

31000 Lines:
pseudo count =1
full LL: -173807.48	 Correlation accuracy: 0.4978050921861282
pseudo count =1
full LL: -173473.34	 Correlation accuracy: 0.4616368286445013
pseudo count =2
full LL: -172677.97	 Correlation accuracy: 0.4676044330775789
pseudo count =2
full LL: -173937.56	 Correlation accuracy: 0.5442908346134152
pseudo count =3
full LL: -173750.28	 Correlation accuracy: 0.5092718227046585
pseudo count =3
full LL: -174131.88	 Correlation accuracy: 0.4608695652173913
pseudo count =4
full LL: -174138.3	 Correlation accuracy: 0.48946444249341525
pseudo count =4
full LL: -174192.69	 Correlation accuracy: 0.463768115942029
pseudo count =10
full LL: -175652.81	 Correlation accuracy: 0.4683229813664596
pseudo count =10
full LL: -176348.38	 Correlation accuracy: 0.47784679089026916
pseudo count =30
full LL: -181383.25	 Correlation accuracy: 0.45311871227364187
pseudo count =30
full LL: -181308.08	 Correlation accuracy: 0.4482897384305835



## BDS SL different amount of lines:


lines: 1000
ess: 10
full LL: -5633.155	 Correlation accuracy: 0.14791133844842286
ess: 30
full LL: -6067.4917	 Correlation accuracy: 0.12617220801364024
ess: 50
full LL: -6257.605	 Correlation accuracy: 0.1658141517476556
ess: 70
full LL: -6276.558	 Correlation accuracy: 0.17715617715617715
ess: 80
full LL: -6040.6074	 Correlation accuracy: 0.13995859213250517
ess: 90
full LL: -6193.904	 Correlation accuracy: 0.1577152600170503
ess: 100
full LL: -6109.6514	 Correlation accuracy: 0.14020805065581185
ess: 120
full LL: -6290.4424	 Correlation accuracy: 0.15897435897435896
ess: 140
full LL: -6310.0786	 Correlation accuracy: 0.16154521510096576
ess: 150
full LL: -6264.8364	 Correlation accuracy: 0.15524475524475526
ess: 200
full LL: -6205.9146	 Correlation accuracy: 0.16734509271822703
lines: 11000
ess: 10
full LL: -62723.164	 Correlation accuracy: 0.2874231032125769
ess: 30
full LL: -62789.223	 Correlation accuracy: 0.29730606945796817
ess: 50
full LL: -62879.29	 Correlation accuracy: 0.34594594594594597
ess: 70
full LL: -63222.836	 Correlation accuracy: 0.32604237867395763
ess: 80
full LL: -63025.95	 Correlation accuracy: 0.32809295967190705
ess: 90
full LL: -63456.61	 Correlation accuracy: 0.3007518796992481
ess: 100
full LL: -62922.465	 Correlation accuracy: 0.30553656869446344
ess: 120
full LL: -63428.54	 Correlation accuracy: 0.307026307026307
ess: 140
full LL: -63644.418	 Correlation accuracy: 0.31035631035631034
ess: 150
full LL: -63531.54	 Correlation accuracy: 0.31868131868131866
ess: 200
full LL: -62797.875	 Correlation accuracy: 0.28594612138915937
lines: 21000
ess: 10
full LL: -119014.875	 Correlation accuracy: 0.3776223776223776
ess: 30
full LL: -118899.78	 Correlation accuracy: 0.35540408958130476
ess: 50
full LL: -119729.96	 Correlation accuracy: 0.3567023693605972
ess: 70
full LL: -119346.53	 Correlation accuracy: 0.35572865952612787
ess: 80
full LL: -119002.53	 Correlation accuracy: 0.37162837162837165
ess: 90
full LL: -119513.14	 Correlation accuracy: 0.3625446283674132
ess: 100
full LL: -119690.016	 Correlation accuracy: 0.3528481012658228
ess: 120
full LL: -118428.47	 Correlation accuracy: 0.345679012345679
ess: 140
full LL: -118871.39	 Correlation accuracy: 0.35345666991236613
ess: 150
full LL: -120011.04	 Correlation accuracy: 0.37867395762132605
ess: 200
full LL: -119206.75	 Correlation accuracy: 0.335126582278481
lines: 31000
ess: 10
full LL: -176207.92	 Correlation accuracy: 0.4008438818565401
ess: 30
full LL: -175520.27	 Correlation accuracy: 0.3778481012658228
ess: 50
full LL: -175430.03	 Correlation accuracy: 0.37468354430379747
ess: 70
full LL: -175389.3	 Correlation accuracy: 0.38727938727938727
ess: 80
full LL: -175566.69	 Correlation accuracy: 0.373904576436222
ess: 90
full LL: -176728.88	 Correlation accuracy: 0.4063615709185329
ess: 100
full LL: -176262.53	 Correlation accuracy: 0.37056962025316453
ess: 120



## BDS SL ess = 40,  PE = BDeu: 

lines: 1000
ess: 10
full LL: -6070.295	 Correlation accuracy: 0.21729587357330993
ess: 30
full LL: -6365.802	 Correlation accuracy: 0.1619718309859155
ess: 40
full LL: -6312.0713	 Correlation accuracy: 0.1255533199195171
ess: 50
full LL: -6250.9336	 Correlation accuracy: 0.16981891348088532
ess: 80
full LL: -6319.778	 Correlation accuracy: 0.14366197183098592
ess: 90
full LL: -6412.3145	 Correlation accuracy: 0.19053708439897699
ess: 100
full LL: -6403.5576	 Correlation accuracy: 0.15942028985507245
ess: 120
full LL: -6418.952	 Correlation accuracy: 0.15015829941203077
ess: 140
full LL: -6702.4097	 Correlation accuracy: 0.14906832298136646
ess: 150
full LL: -6482.485	 Correlation accuracy: 0.1613394216133942
ess: 200
full LL: -6693.6797	 Correlation accuracy: 0.11847463902258423
lines: 11000
ess: 10
full LL: -63845.586	 Correlation accuracy: 0.3209159261790841
ess: 30
full LL: -64375.203	 Correlation accuracy: 0.310663021189337
ess: 40
full LL: -64032.47	 Correlation accuracy: 0.3412612612612613
ess: 50
full LL: -63977.906	 Correlation accuracy: 0.322011322011322
ess: 80
full LL: -64716.918	 Correlation accuracy: 0.322011322011322
ess: 90
full LL: -64283.414	 Correlation accuracy: 0.3196803196803197
ess: 100
full LL: -64010.598	 Correlation accuracy: 0.32167832167832167
ess: 120
full LL: -64408.66	 Correlation accuracy: 0.3226225251541707
ess: 140
full LL: -64558.258	 Correlation accuracy: 0.32434232434232435
ess: 150
full LL: -64861.766	 Correlation accuracy: 0.3073677377474846
ess: 200
full LL: -64417.98	 Correlation accuracy: 0.29562542720437457
lines: 21000
ess: 10
full LL: -121425.0	 Correlation accuracy: 0.35832521908471276
ess: 30
full LL: -121641.5	 Correlation accuracy: 0.38331710483609216
ess: 40
full LL: -121587.445	 Correlation accuracy: 0.37626582278481013
ess: 50
full LL: -121269.27	 Correlation accuracy: 0.34746835443037977
ess: 80
full LL: -121994.555	 Correlation accuracy: 0.3670886075949367
ess: 90
full LL: -122762.63	 Correlation accuracy: 0.36550632911392406
ess: 100
full LL: -121338.03	 Correlation accuracy: 0.3812853812853813
ess: 120
full LL: -121329.984	 Correlation accuracy: 0.3782883782883783
ess: 140
full LL: -121967.58	 Correlation accuracy: 0.3702963702963703
ess: 150
full LL: -121350.67	 Correlation accuracy: 0.3469652710159039
ess: 200
full LL: -122159.84	 Correlation accuracy: 0.3603063603063603
lines: 31000
ess: 10
full LL: -178910.9	 Correlation accuracy: 0.40279130152547876
ess: 30
full LL: -178726.31	 Correlation accuracy: 0.4022151898734177
ess: 40
full LL: -178796.78	 Correlation accuracy: 0.3845679012345679
ess: 50
full LL: -179097.66	 Correlation accuracy: 0.4190197987666342
ess: 80
full LL: -178468.39	 Correlation accuracy: 0.41125541125541126
ess: 90
full LL: -178405.1	 Correlation accuracy: 0.40759493670886077
ess: 100
full LL: -179040.12	 Correlation accuracy: 0.41609866926322625
ess: 120
full LL: -179708.03	 Correlation accuracy: 0.4148003894839338
ess: 140
full LL: -179650.5	 Correlation accuracy: 0.4070107108081792
ess: 150
full LL: -179588.78	 Correlation accuracy: 0.4225774225774226
ess: 200
full LL: -179824.64	 Correlation accuracy: 0.3977848101265823
lines: 41000
ess: 10
full LL: -236040.73	 Correlation accuracy: 0.41645569620253164
ess: 30
full LL: -235746.02	 Correlation accuracy: 0.4475819539110678
ess: 40
full LL: -236018.11	 Correlation accuracy: 0.41360759493670884
ess: 50
full LL: -235781.84	 Correlation accuracy: 0.4021604938271605
ess: 80
full LL: -236261.94	 Correlation accuracy: 0.43005517689061995
ess: 90
full LL: -235537.61	 Correlation accuracy: 0.419620253164557
ess: 100
full LL: -236883.5	 Correlation accuracy: 0.4300632911392405
ess: 120
full LL: -235831.9	 Correlation accuracy: 0.408641975308642
ess: 140
full LL: -235886.34	 Correlation accuracy: 0.4408924408924409
ess: 150
full LL: -236558.34	 Correlation accuracy: 0.42810775722168126
ess: 200
full LL: -237099.25	 Correlation accuracy: 0.43102888672508927
lines: 51000
ess: 10
full LL: -293911.06	 Correlation accuracy: 0.445253164556962
ess: 30
full LL: -292486.72	 Correlation accuracy: 0.4262658227848101
ess: 40
full LL: -293892.16	 Correlation accuracy: 0.43291139240506327
ess: 50
full LL: -292736.53	 Correlation accuracy: 0.42685185185185187
ess: 80
full LL: -293428.9	 Correlation accuracy: 0.4433544303797468
ess: 90
full LL: -293125.3	 Correlation accuracy: 0.4612138915936384
ess: 100
full LL: -294698.7	 Correlation accuracy: 0.46139240506329116
ess: 120
full LL: -295014.25	 Correlation accuracy: 0.43209876543209874
ess: 140
full LL: -294451.16	 Correlation accuracy: 0.439873417721519
ess: 150
full LL: -292563.03	 Correlation accuracy: 0.44746835443037974
ess: 200
full LL: -295305.75	 Correlation accuracy: 0.43259493670886073
lines: 61000
ess: 10
full LL: -350646.5	 Correlation accuracy: 0.45771604938271604
ess: 30
full LL: -350807.8	 Correlation accuracy: 0.4521604938271605
ess: 40
full LL: -350391.94	 Correlation accuracy: 0.4496835443037975
ess: 50
full LL: -350650.03	 Correlation accuracy: 0.4563291139240506
ess: 80
full LL: -349517.88	 Correlation accuracy: 0.4524691358024691
ess: 90
full LL: -350399.8	 Correlation accuracy: 0.47030185004868547
ess: 100
full LL: -351432.88	 Correlation accuracy: 0.43919753086419755
ess: 120
full LL: -351802.38	 Correlation accuracy: 0.45221518987341774
ess: 140
full LL: -350478.3	 Correlation accuracy: 0.4563291139240506
ess: 150
full LL: -350671.4	 Correlation accuracy: 0.4572784810126582
ess: 200
full LL: -352092.88	 Correlation accuracy: 0.4462025316455696
lines: 71000
ess: 10
full LL: -408305.78	 Correlation accuracy: 0.4771178188899708
ess: 30
full LL: -407651.4	 Correlation accuracy: 0.47563291139240504
ess: 40
full LL: -407942.94	 Correlation accuracy: 0.4813372281726712
ess: 50
full LL: -406616.2	 Correlation accuracy: 0.48393378773125606
ess: 80
full LL: -408062.3	 Correlation accuracy: 0.4506172839506173
ess: 90
full LL: -407767.38	 Correlation accuracy: 0.4469135802469136
ess: 100
full LL: -408022.34	 Correlation accuracy: 0.4738721194417397
ess: 120
full LL: -409453.06	 Correlation accuracy: 0.4689873417721519
ess: 140
full LL: -407429.72	 Correlation accuracy: 0.44135802469135804
ess: 150
full LL: -408704.06	 Correlation accuracy: 0.4651898734177215
ess: 200
full LL: -409090.7	 Correlation accuracy: 0.45092592592592595
lines: 81000
ess: 10
full LL: -464450.4	 Correlation accuracy: 0.48037974683544304
ess: 30
full LL: -465727.22	 Correlation accuracy: 0.49050632911392406
ess: 40
full LL: -465323.9	 Correlation accuracy: 0.475
ess: 50
full LL: -466527.38	 Correlation accuracy: 0.4835443037974684
ess: 80
full LL: -465775.06	 Correlation accuracy: 0.46645569620253163
ess: 90
full LL: -465619.16	 Correlation accuracy: 0.47341772151898737
ess: 100
full LL: -465540.62	 Correlation accuracy: 0.4829113924050633
ess: 120
full LL: -465069.47	 Correlation accuracy: 0.4802469135802469
ess: 140
full LL: -465055.2	 Correlation accuracy: 0.46740506329113923
ess: 150
full LL: -463808.75	 Correlation accuracy: 0.48481012658227846
ess: 200
full LL: -463668.22	 Correlation accuracy: 0.4737341772151899
lines: 91000
ess: 10
full LL: -522366.56	 Correlation accuracy: 0.4778481012658228
ess: 30
full LL: -523048.75	 Correlation accuracy: 0.4719135802469136
ess: 40
full LL: -522355.06	 Correlation accuracy: 0.4737654320987654
ess: 50
full LL: -522413.25	 Correlation accuracy: 0.48860759493670886
ess: 80
full LL: -522772.6	 Correlation accuracy: 0.4601851851851852
ess: 90
full LL: -524727.75	 Correlation accuracy: 0.48148148148148145
ess: 100
full LL: -521196.34	 Correlation accuracy: 0.4908227848101266
ess: 120
full LL: -521419.2	 Correlation accuracy: 0.48481012658227846
ess: 140
full LL: -523275.47	 Correlation accuracy: 0.4860759493670886
ess: 150
full LL: -521059.03	 Correlation accuracy: 0.4728395061728395
ess: 200
full LL: -523943.5	 Correlation accuracy: 0.48670886075949366


## Bdeu SL different amount of lines:

lines: 1000
ess: 10
full LL: -5620.0	 Correlation accuracy: 0.13704206241519673
ess: 40
full LL: -5764.0	 Correlation accuracy: 0.1453028972783143
ess: 50
full LL: -6004.0	 Correlation accuracy: 0.14285714285714285
ess: 80
full LL: -5932.0	 Correlation accuracy: 0.15583845478489902
ess: 100
full LL: -6064.0	 Correlation accuracy: 0.15188762071992976
ess: 200
full LL: -6070.0	 Correlation accuracy: 0.17598343685300208
lines: 11000
ess: 10
full LL: -60320.0	 Correlation accuracy: 0.3017771701982228
ess: 40
full LL: -60770.0	 Correlation accuracy: 0.2857142857142857
ess: 50
full LL: -60260.0	 Correlation accuracy: 0.3014354066985646
ess: 80
full LL: -61020.0	 Correlation accuracy: 0.3036963036963037
ess: 100
full LL: -60600.0	 Correlation accuracy: 0.2913752913752914
ess: 200
full LL: -60600.0	 Correlation accuracy: 0.3089542036910458
lines: 21000
ess: 10
full LL: -inf	 Correlation accuracy: 0.3281645569620253
ess: 40
full LL: -inf	 Correlation accuracy: 0.3726315789473684
ess: 50
full LL: -inf	 Correlation accuracy: 0.35919343814080656
ess: 80
full LL: -inf	 Correlation accuracy: 0.33449367088607596
ess: 100
full LL: -inf	 Correlation accuracy: 0.3563777994157741
ess: 200
full LL: -inf	 Correlation accuracy: 0.35832521908471276
lines: 31000
ess: 10
full LL: -inf	 Correlation accuracy: 0.3953261927945472
ess: 40
full LL: -inf	 Correlation accuracy: 0.38461538461538464
ess: 50
full LL: -inf	 Correlation accuracy: 0.37595737595737594
ess: 80
full LL: -inf	 Correlation accuracy: 0.4043062200956938
ess: 100
full LL: -inf	 Correlation accuracy: 0.38069620253164554
ess: 200
full LL: -inf	 Correlation accuracy: 0.3651898734177215
lines: 41000
ess: 10
full LL: -inf	 Correlation accuracy: 0.4057124310288867
ess: 40
full LL: -inf	 Correlation accuracy: 0.41325341325341325
ess: 50
full LL: -inf	 Correlation accuracy: 0.42324342324342323
ess: 80

