# airlineDelay

This model minimizes the total travel time from Madison to different destinations based on the given 
travel time data.

Henry hates flying United airlines through O’Hare (ORD). This is a problem, as he is a soughtafter
lecturer who frequently must make trips from his home base in Madison (MSN) to San Francisco
(SFO), Houston (IAH), Washington DC (DCA), and Orlando (MCO). If he flies United, he
must travel through ORD, if he travels Delta he can choose to go via Detriot (DTW) or Minneapolis
(MSP).

The travel times between various locations in minutes are:
MSN.ORD 22, MSN.DTW 65, MSN.MSP 46,
MSP.SFO 213, MSP.IAH 139, MSP.DCA 125, MSP.MCO 176,
ORD.SFO 247, ORD.IAH 124, ORD.DCA 82, ORD.MCO 135,
DTW.SFO 280, DTW.IAH 147, DTW.DCA 53, DTW.MCO 130

The expected delay times are 3 hours, 1.5 hours and 2 hours at ORD, DTW and MSP repectively. 
Assuming Henry takes 1 trip to each location every year should he switch to Delta? In order to benefit
from frequent flyer miles he would like to fly only one airline.
