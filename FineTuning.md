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



best BIC Dirichlet pseudo count = 2

estimated best BDs SL ess = 40

# 100 lines:

## k2:

### PE: dirichlet:





## 1 run on 1000 lines: 

## Chow-Liu:

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

## Bic: ( 1000 lines)

###  PE: K2:

#### loglikelihood:
full: -3354.1064,
desired: -215.67294,

#### Correlation:
accuracy: 0.26955602536997886,
f1: 

### PE: Dirichlet:

#### PC = 1:

#### loglikelihood:
full: -4609.8145,-3833.783, -4986.578,
desired: -204.12698,-207.75345,-187.47717,

#### Correlation:
accuracy: 0.3422459893048128,0.22424242424242424,
f1: 

#### PC = 2:

#### loglikelihood:
full: -2748.2375, -3562.1167, -4981.162,-4172.831
desired: -241.49637,-191.83185,-213.23575,-209.65623,

#### Correlation:
accuracy: 0.4458874458874459,0.45566502463054187,
f1: 0.14671814671814673,

#### PC = 4:
full LL: -3702.5244      Correlation accuracy: 0.2901849217638691

### PE: BDeu:

#### ess = 4:

#### loglikelihood:
full: -4629.703, 
desired:-227.79189,

#### Correlation:
accuracy: 
f1: 

#### ess = 20:

#### loglikelihood:
full: -4629.703, -4998.1416,
desired:-227.79189,-216.04884,

#### Correlation:
accuracy: 
f1: 

## BIC (10 000):


### PE: Dirichlet

#### PC = 1:
#### loglikelihood:
full: -56926.695,-56256.75,
desired: -2033.4395,-1921.3824,

#### Correlation:
accuracy: 0.40117593848937133,0.4014423076923077,
f1: 

#### PC = 2:
#### loglikelihood:
full: -57771.395,-57338.297,
desired: -1936.9526,-1978.389,

#### Correlation:
accuracy: 0.37622377622377623,
f1: 

#### PC = 3:
#### loglikelihood:
full: -48451.414,-58102.453,-57590.438,-57000.21,
desired: -1979.2112,-2107.7673,-1977.4451,

#### Correlation:
accuracy:0.3643574828133263,
f1:

#### PC = 4:
#### loglikelihood:
full: -59532.39,-54274.383,
desired: -2043.9198,-2054.8022,

#### Correlation:
accuracy:0.40792540792540793,
f1:




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

## BDS SL differnt amount of lines:
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