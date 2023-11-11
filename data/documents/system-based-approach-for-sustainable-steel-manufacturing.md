# System-based approach for sustainable steel manufacturing

## Chinese Steel Manufacturing
Traditionally, steel manufacturing involves two kinds of processes. These 
processes include Blast Furnace (BF)-Basic Oxygen Furnace (BOF) which is named the 
“long process” or the Electric Arc Furnace (EAF) which is named the “short process”. The 
long process involves processes such as sintering, coking, and use of the BF which pollute 
far greater amounts than the short process, which is more reliant on scrap. Alternatively, 
there is also a direct smelting reduction route that is not utilized on a wide scale. Figure 4
illustrates the current steel production routes available throughout the world today.

China’s high energy consumption and heavy pollution within its steel manufacturing 
industry is primarily due to the lack of scrap supply, resulting in over 91% of the steel 
manufacturing reliant upon the long process (China Iron and Steel Association, 2011). 
Realizing the overwhelming majority of steel being reliant upon the long process, this 
thesis will investigate the steel product lifecycle from a systems level, evaluating the 
system’s structure using ecologically-inspired metrics to provide quantitative insight into 
potential areas for sustainable improvement. Figure 5 illustrates the raw materials and 
differing processes involved with the BOF steel manufacturing route. 

Figure 5 demonstrates the process order, layout, and raw materials used in the 
historical BOF steel making process. The raw material stores consist of raw water, lime, 
coal, and iron ore. The main processes contributing flows to the long process of steel 
manufacturing include the coking plant, sintering plant, lime plant, oxygen plant and water 
treatment plant. The core functions after the contributing flows involved in the long process 
include coke making, sintering, BF iron-making, BOF steel making, and steel rolling. 
Secondary processes that vary from plant to plant include types of hot metal pre-treatment, 
differing types of secondary metallurgy, and methods of reheating before the rolling or 
plate mills.

In coke making, a carbon product is formed by the thermal distillation of coal at 
high temperatures in the absence of air. Coke is usually produced in a series of coke ovens. 
Coke’s main function in the iron making process is to reduce the atmosphere in a BF, but 
also acts as a source of fuel. A key characteristic in coke is its porosity, which allows for 
gas exchanges throughout the BF. Newer steel plants use the combustion waste heat in the 
coke-making process to generate steam and electricity.

In sintering, iron-ore fines, iron laden wastes, and dust from the coke manufacturing 
process are blended and combusted. The heat from the process fuses these constituents 
together to form lumps of sinter. This sinter is then used as a charging component in the 
blast furnace. The sintering process as a whole allows for wastes generated in the iron and 
steel making process to be recycled that would otherwise be discarded as unusable.

A component not pictured in Figure 5 is pelletizing. In pelletizing, iron ore is 
crushed and ground to remove impurities. The resulting ore is mixed with a binding agent 
and then heated to create pellets. These pellets are used in both the BF and BOF. Due to 
this process occurring at mining sites, in modelling it is usually accounted for as a raw 
material input.

In the BF, iron ore, coke, and limestone form alternating layers in the furnace atop 
a bed of incandescent coke. Hot air, or blast, is blown through small openings and through 
this bed of coke. The coke combusts, producing heat and gasses. The heat melts the sinter 
charge and the carbon monoxide gasses produced remove the oxygen from the iron ore. 
This process combined forms hot metal which flows to the bottom of the blast furnace and 
through the coke bed. The hot metal is held here until transported to the BOF where it is 
further refined into steel. Iron making using a BF is the most energy intensive process and 
is also the largest emitter of CO2 in steel manufacturing (American Iron and Steel Institute, 
1999).

When the hot metal is then transferred to the BOF, the metal is then refined into 
steel. Oxygen is added to remove the 4% carbon remaining in the molten metal after leaving 
the BF. The BOF process does not consume or produce energy (International Energy 
Agency, 2007). After the metal is refined into steel, it is transferred to the continuous 
casting process and subsequently to rolling and finishing.

During continuous casting, steel is formed into general shapes such as slabs, 
blooms, billets, or rounds. After casting, specific products can be formed in rolling mills 
to produce final shapes such as strips, rails, rods, bars, or sheets. The steel from continuous 
casting is reheated before rolling, which consumes electricity in addition to further the 
shaping of the steel. Finally, the products from rolling can be further processed to hot 
forming, cold rolling, annealing, galvanizing, and other refined products.

### Challenges and Limitations in the Chinese Steel Industry
Some scientists argue the current CSI is progressing on an unsustainable route
(Zhang & Wang, 2007). When evaluating this assertion, one cannot overlook the 
importance of the entire life cycle of the finished product. This importance stems from steel 
being the most recycled material in the world (Bureau of International Recycling Ferrous 
Division, 2015). Metals do not degrade due to recycling, thus the flows of materials exiting 
the steel manufacturing process and then being recycled later in the products life in the 
form of scrap is important in the flow analysis especially in regards to feedback loops of 
material flows. Figure 6 illustrates the inputs of energy, water, raw materials, and scrap 
into the steel manufacturing process along with the other processes involved from the 
lifecycle of steel. 

Understanding the full impact and uses outside of the system boundaries of the steel 
manufacturing process results in a more accurate analysis of the systems within the network 
structure. To accurately model the changes of the steel manufacturing process one must 
first define the system boundaries. Observing the transfer of core materials and energy, one 
can then investigate how the embedded processes within the boundaries have progressed 
throughout time.

### Historical Progress of the Chinese Steel Industry
There have been major gains in efficiency in the CSI from the year 1980. Energy 
consumption per tonne of steel dropped 20.9% from 1285 kgce/t to 1017 kgce/t from 1980 
to 1990 (Sun, Cai, & Ye, 2013). During this time, China developed strategies to improve 
energy efficiency and energy conservation management, offer financial incentives, direct
R&D, initiate IT services, and improve education and training (Sinton & Levine, 1998). 
Many of these strategies focus on optimization of the steel making process such as retiring 
energy intensive mechanical and electrical devices, incorporation of continuous casting
technologies, controls technologies, and investigating the use of by-product gasses as fuel.

### Current State of the Chinese Steel Industry
Since 1990, major gains in energy conservation in CSI came about through 
structural adjustment as well as energy and material flow optimization. The CSI focused 
on waste heat recovery and re-use technology, raw material and fuel pre-treatment 
technologies, plant layout optimization, energy management and controls using automation 
technology (Sun et al., 2013).

One of the largest gains in efficiency in the BOF process has occurred through using 
byproduct gasses and the optimization of material flows. The byproduct gasses are 
transported to boilers in the power plant to produce steam, which is then converted to 
electricity through turbines in addition to reuse in the reheating furnace. This reduces the 
overall energy consumption used in the steel making process, and is consistent with 
literature in direct observations showing that in 2007, 90% of the BF’s larger than 1000 m3
were equipped with a Top gas pressure Recovery Turbine (TRT). Further, by the end of 
2006, 77% of key Chinese steel enterprises had also installed BFG recovery equipment and 
64% had installed recovery equipment for other gas recovery such as Coke Oven Gas 
(COG) and Basic Oxygen Furnace Gas (BOFG) (Song & Liu, 2012). Also, by the end of 
2004, nearly 25% of the CSI had Coke Dry Quenching (CDQ) units installed and in 
operation (International Energy Agency, 2007; Song & Liu, 2012). The addition of CDQ 
reduces the amount of water consumed by the steel making process and improves the 
overall water quality used throughout the manufacturing process.


## SYSTEM DESCRIPTION

### Steel Industry: Plant Scale Analysis
In this section, the CSI models structure and materials flow construction from past 
until present is discussed, assumptions listed, and data is presented.

### Historical Model Data Acquisition and Assumptions
For the historical analysis, the major process level material flow values were chosen
from the Yearbook of China’s Steel Industry (Mettalurgical Economic R&D Centre of 
China, 1988) for the 1988 Anshan Iron and Steel Corporation’s BOF plants statistics. 
Values such as coking rate, continuous casting yield, external scrap use fractions and each 
stage material flow values in the production levels as well as all model configurations are
available and listed in A.1 CSI Historical Data. However, some values needed to be 
acquired from sources throughout literature as a single source could not be located.
The assumptions of the historical model are as follows:

• The use of by-product gasses such as Coke Oven Gas (COG), Blast Furnace Gas 
(BFG), and Basic Oxygen Furnace Gas (BOFG) are not utilized for power 
generation in 1988 and are instead released to the environment (Sun et al., 2013)
• The use of pellets, anthracite, oxygen blast air from oxygen generation plant, or 
lime is not used in iron making. (Rosst & Feng, 1991)
• Water is consumed at 210m 3 per tonne crude steel as estimate from 1998, due to 
lack of data in 1988 (The Editorial Board of the Yearbook of Iron and Steel Industry 
of China (ISIC), 1998)
• BOF slag is assumed to be 0.0085 tonne per tonne crude steel due to lack of data in 
1988 (R. Yin, 2013)
• Mill scale is not recycled into the sinter plant (Umadevi, Kumar, Mahapatra, Babu, 
& Ranjan, 2009)
• The distribution of water flows throughout the plant are the same percentages from 
current day though usage rates differ greatly (Worrell, Blinde, Neelis, Blomen, & 
Masanet, 2010)
• The flows from the lime plant, iron ore powder and lime from the raw material yard 
to the sinter plant remain unchanged from current day amounts
• The co-location of industries that could benefit from the products or waste streams 
of this historical plant are outside of the historical system boundaries
• Due to the steel manufacturing fuel use being represented largely by coal, a 
conversion of off-gasses into coal equivalent is assumed.

The assumptions above are largely due to data scarcity during the late 1980’s for the CSI. 
Where values must be assumed (lime flows, emission amounts), conservative estimates 
were taken as to not distort the model.

### Historical Model Structure and Flow Construction

The simplified structural configuration of the historical model is demonstrated in 
Figure 7. 

Figure 7 - Historical Integrated Steel Making Process
Due to the complexity of the steel manufacturing process and the diversity of industry size 
and configurations, only major flows are considered. This approach allows for a 
comparison to be drawn across time to current day processes, while also accurately 
reflecting the system historically. This also allows for the resolution of the model to be 
consistent over time, which is important for metric comparison of systems in ecological 
network analysis. The structure and flow matrix is presented in A.2 Historical Structure 
and Flow Matrix Construction.
The flows for the historical analysis are represented in Table 1 below.

Table 1 - Historical Flow Values Used in Model
Flow From Flow To Value Units Historical 
Source
Washery Coal Coking Plant 1.4450 ton/ton-cs CISY 1989
Water Coking Plant 4.4834 ton/ton-cs **
Hot Rolled Sheet Cold Rolling Plant 0.0500 ton/ton-cs CISY 1989
Water Cold Rolling Plant 0.1494 ton/ton-cs **
Basic Oxygen Furnace 
Slag
Construction 
Material Plant 0.0085 ton/ton-cs Yin 2009
Water Entire 21.5000 ton/ton-cs CISY 1998
Flume Emissions Environment 1.2000 ton/ton-cs Price et al. 2001 
for year 1988
Dust Emissions Environment 0.0017 ton/ton-cs ***
SO2 Emissions Environment 0.0024 ton/ton-cs ***
NOx Emissions Environment 0.0033 ton/ton-cs ***
Effluent Environment 2.2081 ton/ton-cs CISY 1989
Con. Cast Slab Hot Rolling Plant 0.3464 ton/ton-cs CISY 1989
Water Hot Rolling Plant 4.8263 ton/ton-cs **
Lump Ore Iron Plant 1.7920 ton/ton-cs CISY 1989
Coal Iron Plant 0.5890 ton/ton-cs CISY 1989
Sinter Ore Iron Plant 1.6020 ton/ton-cs Sun et al 2013 for 
year 1990
Coke Iron Plant 0.6320 ton/ton-cs Sun et al 2013 for 
year 1990
Water Iron Plant 3.5076 ton/ton-cs **
Wide & Heavy Plate 
Products
Market 0.6927 ton/ton-cs CISY 1989
Cold Rolling Products Market 0.2131 ton/ton-cs CISY 1989
Hot Rolled Plate 
Products
Market 1.4762 ton/ton-cs CISY 1989
Cold Rolling 
Scrap/Scale
Scrap/Scale 0.0080 ton/ton-cs CISY 1988
Hot Rolling 
Scrap/Scale
Scrap/Scale 0.0556 ton/ton-cs CISY 1989
Wide & Heavy Plate 
Scrap/Scale
Scrap/Scale 0.0176 ton/ton-cs CISY 1989
Lime Plant Sinter Plant 0.0635 ton/ton-cs
Iron Ore Powder Sinter Plant 1.1538 ton/ton-cs
Lime (Raw Material 
Yard)
Sinter Plant 0.0346 ton/ton-cs
Coke Powder Sinter Plant 0.0680 ton/ton-cs CISY 1989
Water Sinter Plant 0.4835 ton/ton-cs **
Lime & Dolomite Steel Plant 0.0000 ton/ton-cs Rosst and Feng 
1990
Oxygen Steel Plant 0.0530 tce/ton-cs *Est based on US 
Prod
Hot Liquid Iron Steel Plant 1.0000 ton/ton-cs CISY 1989
Scrap/Scale Steel Plant 0.0950 ton/ton-cs CISY 1989
Water Steel Plant 0.5978 ton/ton-cs **
Crude Steel To Plate, HR, CR, 
and Construction 0.5589 ton/ton-cs Sun et al 2013 for 
year 1990
Effluent Water Treatment 
Plant 0.1250 ton/ton-cs -
Con. Cast Heavy Slab Wide & Heavy 
Plate Plant 0.1625 ton/ton-cs CISY 1989
Water Wide & Heavy 
Plate Plant 4.8263 ton/ton-cs **
*= Estimate
**Using Ratio's from Current Time and Assuming 210m^3/ton crude steel
*** Using 2x the current values as estimate

### Current Model Data Acquisition and Assumptions
The data for the simplified current day model structure and flow data was provided 
by industry partners within the CSI. The assumptions for the current model are as follows:
• The co-location of industries that could benefit from the products or waste streams 
of this historical plant are outside of the historical system boundaries
• Due to the steel manufacturing fuel use being represented largely by coal, a 
conversion of off-gasses into coal equivalent is assumed.
• Byproduct gasses irregularities in generation are negligible. Uncertainty factors 
such as equipment maintenance could affect the stable production of gasses.

### Current Model Structure and Flow Construction
The simplified current day structure of the steel manufacturing process is 
represented in Figure 8.

Figure 8 - Current Steel Manufacturing Process
As demonstrated in Figure 7, the major changes from our historical model are the additions 
of waste-gas energy recovery systems, increased intra-plant recycling, and the optimization 
of material flows. These structure and flow changes are represented in Table 2.

Table 2 – Present Day Values Used in Model
Flow From Flow To Value Units
Washery Coal Coking Plant 0.6173 ton/ton-cs
Water Coking Plant 0.8592 ton/ton-cs
Hot Rolled Sheet Cold Rolling Plant 0.2096 ton/ton-cs
Water Cold Rolling Plant 0.0286 ton/ton-cs
Water Entire 4.1200 ton/ton-cs
Flume Emissions Environment 0.0003 ton/ton-cs
Dust Emissions Environment 0.0009 ton/ton-cs
SO2 Emissions Environment 0.0012 ton/ton-cs
NOx Emissions Environment 0.0016 ton/ton-cs
Effluent Environment 0.1300 ton/ton-cs
Con. Cast Slab Hot Rolling Plant 0.7096 ton/ton-cs
Water Hot Rolling Plant 0.9249 ton/ton-cs
Pellett Iron Plant 0.3904 ton/ton-cs
Lump Ore Iron Plant 0.0981 ton/ton-cs
Coal Iron Plant 0.2019 ton/ton-cs
Sinter Ore Iron Plant 1.2365 ton/ton-cs
Coke Iron Plant 0.3173 ton/ton-cs
Oxygen Blast Iron Plant 0.0012 tce/ton-cs
Water Iron Plant 0.6722 ton/ton-cs
Lime & Dolomite Stone Lime Plant 0.2942 ton/ton-cs
BFG Lime Plant 0.0067 tce/ton-cs
COG Lime Plant 0.0076 tce/ton-cs
Wide & Heavy Plate Products Market 0.2692 ton/ton-cs
Cold Rolling Products Market 0.1923 ton/ton-cs
Hot Rolled Plate Products Market 0.4827 ton/ton-cs
COG Outside Park Power Plant 0.0036 tce/ton-cs
BFG Power Plant 0.0477 tce/ton-cs
BOFG Power Plant 0.0289 tce/ton-cs
COG Power Plant 0.0013 tce/ton-cs
Water Power Plant 0.2510 ton/ton-cs
Cold Rolling Scrap/Scale Scrap/Scale 0.0173 ton/ton-cs
Hot Rolling Scrap/Scale Scrap/Scale 0.0173 ton/ton-cs
Wide & Heavy Plate 
Scrap/Scale
Scrap/Scale 0.0212 ton/ton-cs
Lime Plant Sinter Plant 0.0635 ton/ton-cs
Iron Ore Powder Sinter Plant 1.1538 ton/ton-cs
Lime (Raw Material Yard) Sinter Plant 0.0346 ton/ton-cs
Anthracite Sinter Plant 0.0025 ton/ton-cs
Coke Powder Sinter Plant 0.0538 ton/ton-cs
Scrap/Scale Sinter Plant 0.0154 ton/ton-cs
Water Sinter Plant 0.0927 ton/ton-cs
Lime & Dolomite Steel Plant 0.0808 ton/ton-cs
Oxygen Steel Plant 0.0260 tce/ton-cs
Hot Liquid Iron Steel Plant 1.0096 ton/ton-cs
Scrap/Scale Steel Plant 0.0962 ton/ton-cs
Water Steel Plant 0.1146 ton/ton-cs
Crude Steel To Plate, HR, CR, and 
Construction
1.0000 ton/ton-cs
Effluent Water Treatment Plant 0.1250 ton/ton-cs
Con. Cast Heavy Slab Wide & Heavy Plate Plant 0.2904 ton/ton-cs
Water Wide & Heavy Plate Plant 0.9249 ton/ton-cs
*= Estimate
 
### Summary of Plant Scale Analysis
Two configurations were analysed and discussed in the plant scale analysis. A 
historical perspective and current day perspective were modelled in order to demonstrate 
the progress of steel manufacturing over time from an ecological perspective. Data was 
acquired from sources throughout literature and from industry partners, and assumptions 
for each of the model configurations were presented. The ecological results demonstrate 
an increase in efficiency over time.
