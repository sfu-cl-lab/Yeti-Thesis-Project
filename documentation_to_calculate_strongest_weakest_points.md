 + Create view `chao_draft.lmt_testYears_CSS_null_norm_prob_for_points` by adding numeric columns for position_L/R/D/C and country_USA/CAN/EURO.
 
 + Calculate attributes strength against average with equation **∑wi(xi- ẍ)** for each player in two cohorts(players drafted in 2001/2 ; players drafted in 2007/8). Code can be found here:
https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/Decision_Trees/LMT/calculate_points_strength_against_avg.py
 
 + Save the results in table `chao_draft.lmt_testYears_CSS_null_norm_prob_for_points`. And the strongest point and weakest point is summarized as following:


2001 & 2002 | Strongest Points(Weakest Players)<br>**[id, Name, value]** | Weakest Points(Strongest Players)<br>**[id, Name, value]** |
----------- |-----------------------------------------------------| ----------------------------------------------------|
LeafNode 1 | [59121, Peter Reynolds, 1.43699254055]<br>[27, Yared Hagos, 1.48708662639]<br>[58597, Igor Valeyev, 1.75168074781] | [13243, Jake Riddle, -2.58681834167]<br>[39663, Chris Petrow, -1.87908802555]<br>[15831, Tomas Linhart, -1.56171146015] |
LeafNode 2 | [17972, Ryan Bowness, 1.41460609338]<br>[27586, Marian Havel, 1.90158029189]<br>[18670, Pierre-Luc Emond, 2.45731999708] | [882, Simon Skoog, -2.40004324638]<br>[14513, Adrian Foster, -1.73434795491]<br>[547, Marcus Paulsson, -1.41170493637] |
LeafNode 3 | [8469667, Tony Martensson, 2.92737363303]<br>[13396, Vince Bellissimo, 3.04458672859]<br>[8469469, R.J. Umberger, 3.11652862375] | [8469508, Jay McClement, -2.18420320554]<br>[8469483, David Steckel, -2.18322570608]<br>[12235, Mikhail Tyulyapkin, -1.96791790014] |
LeafNode 4 | [9569, Andrei Taratukhin, 2.09992055229]<br>[28602, Martin Cizek, 2.15409441209]<br>[9563, Yuri Trubachyov, 2.62492018686] | [12233, Dmitri Kazionov, -2.38239233531]<br>[8470055, Petr Kanko, -2.06495548012]<br>[26581, Jean-Francois Soucy, -2.02927466217] |
LeafNode 5 | [3217, Jarkko Immonen, 1.31608294935]<br>[52122, Michal Blazek, 1.63999789359]<br>[7523, Viktor Ujcik, 1.78920151806] | [3195, Joonas Vihko, -2.34878916407]<br>[19350, Scott Dobben, -1.69144530233]<br>[8030, Carter Trevisani, -1.63408127869] |



2007 & 2008 | Strongest Points(Weakest Players [id, Name, value]) | Weakest Points(Strongest Players [id, Name, value]) |
----------- |-----------------------------------------------------| ----------------------------------------------------|
LeafNode 1 | [8474600, Roman Josi, 1.99987178996]<br>[8474141, Patrick Kane, 2.24496739982]<br>[8474563, Drew Doughty, 2.34215133661] | [8474569, Colin Wilson, -1.59960831342]<br>[8474168, Joakim Andersson, -1.58554383165]<br>[8474576, Zach Boychuk, -1.53096398201] |
LeafNode 2 | [8474048, Keith Aulie, 0.897759775364]<br>[8474000, Steven Kampfer, 1.50975012221]<br>[8474597, Cody Goloubef, 2.24758191393] | [12535, Travis Erstad, -1.72712719356]<br>[19232, Jeff Foss, -1.49236975153]<br>[8474162, Jake Muzzin, -1.28910957526] |
LeafNode 3 | [12536, Justin Mccrae, 1.62124834254]<br>[14431, Nathan Moon, 1.64334375002]<br>[8474657, Jamie Arniel, 2.45381818102] | [8474098, Colton Sceviour, -1.64236648773]<br>[19224, Kory Nagy, -1.23328568346]<br>[12120, Chris Doyle, -0.988503951702] |
LeafNode 4 | [8474192, Matt Frattin, 1.8569825254]<br>[8474739, Tommy Wingels, 2.3015009083]<br>[8474024, Jim O'Brien, 2.42440049563] | [8474727, Ben Smith, -3.02158559559]<br>[8474673, TJ Brodie, -2.29503202907]<br>[18746, Matt Marshall, -2.15415816858] |
LeafNode 5 | [8474616, Patrice Cormier, 2.43133112938]<br>[8474642, Lance Bouma, 2.48420235448]<br>[8474584, Michael Del Zotto, 2.8310216081] | [11465, Vinny Saponari, -1.93872865148]<br>[8474629, Shawn Lalonde, -1.84800868063]<br>[8474691, Philippe Cornet, -1.84467472577] |
LeafNode 6 | [9347, Justin Azevedo, -0.183531860288] | [8474146, Spencer Machacek, -2.10624733328] |



+ *Some strong players in strong clusters ranked by our model didn’t play or only played few games in NHL.* Because they never sign a contract with NHL but play in other competitive leagues like AHL, KHL. These players are summarized as following.


Name | NHL_GP_greater_than_0 | Career League | (cohort, leafNode) |
---- |---------------------- | ------------- | ------------------ |
Joonas Vihko | no | SM-liiga | (1, 5) |
Dmitri Kazionov | no | KHL | (1, 4) |
Tomas Linhart | no | Czech Extraliga | (1, 1) |
Adrian Foster | no | AHL | (1, 2) |
Marcus Paulsson | no | SHL | (1, 2) |
Mikhail Tyulyapkin | no | KHL(injury) | (1, 3) |
Jean-Francois Soucy | no | ECHL | (1, 4) |
Carter Trevisani | no | Serie A(ice hockey) | (1, 5) |
Kory Nagy | no | AHL | (2, 3) |






















            
