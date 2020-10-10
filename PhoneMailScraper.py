#! /usr/bin/env python 3

import re, pyperclip
text = '''
EXAMPLE PHONE AND EMAIL
DIRECTORY
This example PDF was created to practice writing programs that could automatically get phone numbers and email addresses from PDFs.
You can learn to program with the free resources at https://inventwithpython.com
PUBLIC DOMAIN IMAGE OF THE SEAL OF APPROVAL
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
 
       Jessie Mckay
Tom Jordan Clayton Cross Rayford Sutton Jerome Gentry Weldon Camacho Quinton Franks Adam Hubbard Jarred Fox
Arnoldo Parker
Sid Mcdaniel Raymon Combs Ervin Francis Gilberto Austin Lino Barlow
Stacey Shepherd Roscoe Terry
Eddie Meadows Carlos Simpson Jerome Manning Hong Erickson
Burt Graham Mario Sloan
Jeffry Mcintosh Owen Malone Jamar Gilbert Guadalupe Ramsey Chet Ramsey Lester Finch Mason Marquez
Olen Boyer
Sherman Gamble
Gerry Mccarthy
Jon Jefferson
Cristopher Maddox
Abel Talley
Jerrod Hurst
Ezra Pickett
Delbert Mcintyre
Tom Wilkins
Deandre Schneider
Louie Gross
Cary Mathews
jmckay67@aol.com tjordan@msn.com ccross20@gmail.com rayfords66@hotmail.com jgentry@me.com wcamacho57@icloud.com qfranks@comcast.net cygzfjd61@outlook.com jfox39@live.com aparker39@sbcglobal.net mcdanie3354@att.net uqcwsntti71@att.net efrancis@optonline.net austi363@optonline.net lbarlow22@me.com sshepherd61@sbcglobal.net rterry64@outlook.com eddiem89@yahoo.com csimpson8@verizon.net jmanning54@optonline.net herickson3@me.com bgraham70@sbcglobal.net msloan55@verizon.net jmcintosh@icloud.com owenm64@yahoo.com uzkp@yahoo.com gramsey51@optonline.net cramsey91@outlook.com lfinch@gmail.com masonm44@att.net oboyer8@icloud.com tnjdmbnizb@comcast.net gmccarthy4@msn.com tzb23@yahoo.com cmaddox@yahoo.com talle6@att.net jhurst88@outlook.com epickett85@msn.com dmcintyre@optonline.net twilkins7@icloud.com deandres56@outlook.com lgross@me.com cmathews23@verizon.net
479-205-4874
678-560-3485
724-900-2986
242-391-3183
604-720-6426
651-807-8065
209-754-9111
641-433-6698
701-528-9851
304-491-9583
863-583-8107
507-948-3980
546-367-3454
321-854-5616
904-896-2920
309-387-1990
605-373-2329
573-454-1209
252-822-2439
586-481-1805
615-716-5379
903-995-3368
205-868-3935
881-376-2173
936-631-8841
307-368-4710
631-957-9402
336-402-2815
511-768-9073
862-579-2515
678-439-5117
949-328-4768
764-582-6489
662-882-4349
323-686-4356
321-641-1192
980-511-2211
931-381-2749
557-314-1719
641-845-9700
571-248-3160
611-848-3013
724-392-9051
                                                                                                                                                                            
       Clinton Hernandez Sylvester Goodman
Efren Daniels Myles Knapp
Trey Hendrix Gerardo Gonzales Collin Wilkinson Hubert Moore Rudolph Joyce Raymundo Griffin Stanton Burris Newton Huff Lonnie Gibson Newton Mendez Dominic Kane
Rey Alvarado Maxwell Pittman Freddy Nolan Quentin Kane Marcelo Owens Saul Warner Giuseppe Edwards Glen Duffy Johnson Bird
Lon Mays
Orval Jones
Stefan Wiley Dewayne Vincent Elmo Morton
Trenton Randolph
Alonzo Noble
Stephan Callahan
Merrill Morin
Antonia Vasquez Jerrod Horne Sammie Blanchard Renaldo Nielsen Rick Logan
Xavier Sexton Delmer Chambers Melvin Dixon Randell Wright
chernandez16@yahoo.com
sylvesterg@comcast.net edaniels@comcast.net mknapp26@outlook.com thendrix@me.com ggonzales@hotmail.com cwilkinson7@comcast.net hmoore12@yahoo.com joyc5185@sbcglobal.net rgriffin45@optonline.net sburris@comcast.net nhuff@att.net lgibson51@comcast.net nmendez@mac.com dkane93@msn.com alvarad24@live.com mpittman9@gmail.com fnolan38@verizon.net qkane60@me.com mowens88@aol.com swarner@mac.com gedwards@aol.com gduffy35@optonline.net cwnzm@hotmail.com lmays@gmail.com xugizlf81@live.com swiley19@sbcglobal.net dvincent@verizon.net emorton5@hotmail.com trentonr64@comcast.net alonzon17@aol.com scallahan89@optonline.net mmorin73@mac.com vasque3298@comcast.net jerrodh62@comcast.net sblanchard44@att.net renaldon@comcast.net rlogan97@optonline.net ysbmcsipr3@comcast.net dchambers18@sbcglobal.net mdixon95@me.com rwright@att.net
303-606-9242
419-691-5429
740-228-1291
479-529-9642
308-702-9334
704-481-3176
270-245-5606
559-639-2831
506-203-1818
716-387-4756
501-919-6026
351-796-1964
809-948-1893
984-578-4176
765-298-6852
309-531-8927
561-405-2390
423-694-1512
561-365-7342
717-616-6054
517-593-3243
971-374-3441
313-758-7914
713-418-9707
811-557-8092
601-247-7920
405-866-8158
940-998-9912
904-383-5407
772-773-7846
312-773-6768
814-960-3437
703-767-4323
403-212-2346 805-997-2016 415-595-9796 252-739-5595 473-406-4822 778-569-3862 410-418-7216 816-614-7357 307-476-5699
                                                                                                                              
       Kasey Mcbride Long Cohen Hunter Walton Jacques Dean Nicky Cleveland Heath Reeves Dannie Castro Malcolm Pickett Emil Bryant Lonny Trevino Lamont Booker Norberto Ramsey Donny Mcintosh Antwan Harmon Cristopher Blanchard
Zane Glover
Ralph Booth
Curtis Maddox Deon David Salvador Short Curtis Rios
Ashley William Nicholas Blanchard Jermaine Stephenson Aubrey Knapp Abel Shields Micheal Whitfield Royal Williams Hayden Barber Cruz Gregory
Stacy Wyatt Adrian Mason Faustino Sosa Toney Mccarty Bill Gentry Wallace Bullock Damon Blake Waldo Castaneda Wilford Yates Chas Hicks
Miles Combs
mcbrid17@gmail.com cohe1696@yahoo.com hwalton3@hotmail.com jacquesd@att.net ncleveland88@mac.com hreeves56@mac.com dcastro91@mac.com picket8286@gmail.com ebryant28@hotmail.com ltrevino@live.com lbooker16@me.com ramse3653@verizon.net donnym24@live.com aharmon99@sbcglobal.net
cblanchard@msn.com zglover61@yahoo.com rbooth23@mac.com curtism@verizon.net ddavid37@sbcglobal.net qxu@msn.com crios28@yahoo.com awilliam86@sbcglobal.net blanchar7913@icloud.com
jstephenson53@live.com aubreyk90@msn.com abels@verizon.net pmorp6@msn.com royalw65@verizon.net hbarber66@sbcglobal.net cgregory@mac.com wyat97@gmail.com maso5913@gmail.com fsosa33@sbcglobal.net mccart6795@me.com gentr9578@verizon.net wbullock50@hotmail.com dblake74@sbcglobal.net wcastaneda@sbcglobal.net wyates@att.net hexxuxu97@icloud.com mcombs2@icloud.com
939-537-1879
905-523-5311
975-675-8521
515-420-4722
573-286-5790
646-934-6224
473-909-5259
425-691-6076
740-912-1584
361-423-3274
939-725-1384
484-326-9103
207-389-7224
947-684-9146
877-503-6944
601-896-4565
254-945-4889
417-576-2133
627-632-6773
812-983-9748
303-568-6327
402-497-9729
441-769-3433
641-409-6385
514-637-7967
813-213-1319
704-231-9162
229-718-3131 518-483-3634 231-296-9140 706-899-3971 464-525-8598 464-999-6721 760-690-7194 424-442-9011 211-937-9457 234-238-8851 904-838-7421 320-944-8986 881-674-8231 847-833-3195
                                                                                                                           
       Greg Goodwin Howard Palmer Teddy Underwood Lanny Anthony Modesto Haley Dirk Watkins Fausto Quinn Pablo Nguyen Wayne Scott Christoper Guerrero
Joe Clay
Riley Berry
Casey Rosa
Cleo Carver
Eli Avery
Percy Mathis Dante Briggs Robbie Spears Galen Solis
Vince Mcdonald Alberto Hamilton Dana Garner Martin Blackburn Rolland Graves Jack Fulton Glenn Logan Chung Hanson Korey Petersen Daniel Buckner
Eli Nicholson
Timothy Alvarez
Rich Scott
Long Morrison
Ernesto Deleon King Mcgowan Tyron White Oscar Cash Darin Kelly Harry Bird Clyde Gillespie Reynaldo Small Damien Hatfield
goodwi99@sbcglobal.net palme7345@live.com teddyu49@live.com dxa18@optonline.net mhaley24@sbcglobal.net dwatkins@msn.com fquinn63@icloud.com pablon88@aol.com wscott@yahoo.com
guerrer5579@comcast.net dhuy50@mac.com rberry36@outlook.com ros81@msn.com ccarver63@yahoo.com eavery@msn.com percym86@yahoo.com dbriggs68@att.net uyqcq84@msn.com gsolis80@gmail.com vmcdonald22@aol.com ahamilton74@yahoo.com dgarner@gmail.com mblackburn48@me.com rgraves8@optonline.net jfulton61@live.com loga4146@verizon.net cpnxn91@att.net kpetersen80@gmail.com dbuckner@outlook.com elin47@msn.com xzwkvrg72@mac.com lflmzbbzh@optonline.net lmorrison36@yahoo.com edeleon77@comcast.net kmcgowan@comcast.net twhite89@gmail.com oscarc94@hotmail.com dkelly@outlook.com bir8097@me.com clydeg32@optonline.net rsmall61@gmail.com dhatfield30@icloud.com
504-925-2032
984-739-5933
832-295-6774
405-807-2836
559-710-6677
903-628-5508
339-741-4816
509-213-3802
608-743-7298
843-618-3895
307-922-7850
703-663-5402
513-264-5926
239-856-1769
718-379-7684
224-699-9948
727-437-8571
240-841-7589
913-851-9474
270-796-8192
418-393-3324
815-834-1689
218-986-7343
585-227-9385
806-463-3328
700-911-8905
308-973-7318
859-328-2032
859-301-4839
216-207-9704
631-926-6045
867-402-4652
239-805-3865
402-619-6555 877-623-7118 351-562-7333 361-447-2150 860-946-8955 218-585-4289 352-464-2633 270-618-4131 845-511-8104
                                                                                                                              
       Cyril Wynn
Sidney Lara Pasquale Larson Olen Fuentes Floyd Bray
Dennis Fowler Hoyt Nielsen Humberto Leonard Sylvester Maldonado Landon Goff
Ian Hebert
Levi Oconnor
Theo Lloyd
Britt Baird
Luciano Donaldson Larry Cummings Colin Bender
Jae Davis
Clark Alvarez German Parsons Lupe Conrad Brendan Conley Cletus Bauer Hilario Trevino Frances Clark Young Hernandez Trenton Robinson Monroe Winters Rick Trevino
Erwin Downs
Margarito West
Emmitt Quinn
Vern Rodriguez
Ross Gutierrez Junior Fields Roman Baldwin Seymour Morton Franklin Lamb Bill Mccray Micah Murray Angelo Mckenzie Son Atkinson
cwynn63@outlook.com sidneyl@hotmail.com larso56@msn.com ofuentes67@verizon.net tins28@gmail.com dfowler@me.com hnielsen88@yahoo.com leonar8259@live.com
smaldonado58@att.net lgoff67@comcast.net heber22@hotmail.com loconnor93@att.net tlloyd@hotmail.com bbaird@gmail.com omykcnmh8@verizon.net larryc97@optonline.net cbender89@verizon.net jdavis49@msn.com yaehophxlt43@aol.com parson87@me.com lconrad54@live.com fcocztufbo79@comcast.net cbauer35@verizon.net htrevino47@sbcglobal.net fclark82@att.net hernande713@verizon.net zlcqlnt21@comcast.net mwinters94@me.com rtrevino26@optonline.net edowns@hotmail.com wes6448@live.com emmittq21@aol.com vrodriguez@aol.com rgutierrez37@msn.com jfields98@icloud.com rbaldwin28@msn.com smorton58@verizon.net flamb51@live.com bmccray14@yahoo.com murra7344@comcast.net amckenzie@optonline.net satkinson56@mac.com
405-918-3937
464-390-2264
242-726-1488
662-743-9060
209-732-1588
239-519-8768
847-950-8510
412-975-6397
239-551-4133
900-442-1979
386-249-3186
880-553-1551
767-978-1382
336-660-3178
313-778-4612
618-745-4805
264-514-9602
913-873-4406
580-711-6719
307-897-7205
778-511-8803
737-888-4741
709-765-4993
540-930-7062
916-842-3938
402-505-7515
917-530-7084
516-501-5869
601-538-7861
660-268-3286
260-599-6493
541-359-8699
316-362-3876
484-238-6979 464-562-2555 939-673-2435 612-241-8285 246-914-9884 561-545-9594 902-346-5892 517-879-4678 833-227-6959
                                                                                                                              
       Justin Perry
Ron Mccoy Wallace Robertson Bertram Vega Roscoe Hines Ismael Lewis
Kurt Dunlap Jimmy Valenzuela Willian Downs Grady Shaw Scottie Atkinson Berry Phillips
Ian Graham
Allen Clemons Kirby Gilliam
Evan Terry Franklin Solomon Leonardo Barber Connie Vincent Evan Richmond Myles Woodard Adan Armstrong Samual Dorsey Jules Merritt
Shad Meyers Hosea Howell Ward Clarke Bennett Mckenzie Herschel Irwin Max Howe
Carol Boyle
Marc Daniels
Lester Mcfarland
Boris Bowers
Lou Joyce
Jermaine Love
Antone Parsons
Xavier Everett
Francis Sheppard
Vicente Waller
Jerrell Sweet
Bo Ware
Ike Walsh
gahu14@live.com rmccoy55@outlook.com wallacer81@yahoo.com bvega39@yahoo.com kyxdmsnoh81@verizon.net ilewis38@aol.com kurtd@mac.com
970-964-7403
509-871-3552
626-611-3619
971-972-1597
719-841-7163
619-346-4110
508-602-5051
                           jvalenzuela12@optonline.net   727-615-7434
    wdowns@att.net gshaw98@yahoo.com satkinson47@att.net bphillips57@outlook.com igraham47@verizon.net qbmgk@live.com kgilliam@sbcglobal.net eterry67@yahoo.com fsolomon81@outlook.com barbe138@yahoo.com cvincent38@hotmail.com erichmond@live.com mwoodard34@icloud.com aarmstrong39@att.net dorse4380@optonline.net julesm60@verizon.net smeyers78@sbcglobal.net hhowell6@outlook.com wclarke49@me.com bmckenzie49@aol.com herscheli@live.com mhowe28@msn.com cboyle11@hotmail.com mdaniels@yahoo.com lmcfarland7@hotmail.com bbowers53@mac.com louj89@msn.com jlove99@gmail.com tdymy79@live.com xeverett92@verizon.net fsheppard@live.com vwaller57@live.com jsweet91@me.com bware30@gmail.com iwalsh76@verizon.net
828-375-9162
385-795-4623
822-584-4566
877-241-8837
718-474-8986
758-521-6779
231-830-4298
752-276-6713
937-522-5976
564-854-2757
980-613-5291
765-235-1022
562-742-4234
872-336-6099
281-237-5202
334-551-4961
806-574-2800
848-750-3377
600-394-1825
878-259-8254
740-662-9378
904-372-9568
518-502-8801
646-279-2565
718-639-4360
810-209-6214
516-268-8591
414-460-6215
511-359-9922
313-337-4929
808-252-4393
985-747-2466
557-385-4600
561-887-6946
251-908-7682
                                                                                                                                            
       Thomas Ford Spencer Mccarty Anton Zimmerman Jeffry Jacobson Joaquin Merrill Waylon Holder Federico Pickett Milo Harper
Andy Owen Kendall Mcmillan Cortez Underwood Robin Michael Orville Wade
Pete Becker
Edwin Wilkerson Fabian Fisher Refugio Roth Millard Stewart Odell Bailey
Gayle Curry
Hilario Barr
Burt Finley
Teddy Randolph Clarence Calhoun Waldo Rasmussen Theo Kirk
Hunter Cochran Herbert Meyer Aubrey Hudson Cory Ramos
Merlin Hunter
Santiago Fuentes
Donny Mcintyre
Armando Keith
Cody Spears
Genaro Valdez
Anibal Charles
Aurelio Coffey
Faustino Bishop
Jerrell Morales
Jonas Chang
Darrin Peters
Kim Hooper
kppilspnbx1@live.com smccarty19@outlook.com antonz@icloud.com jjacobson@sbcglobal.net jmerrill@aol.com wholder34@me.com yiafpwdr98@aol.com mharper@aol.com owe3619@comcast.net kmcmillan11@gmail.com cunderwood10@att.net rmichael63@live.com rfdct61@msn.com pbecker9@verizon.net ewilkerson41@icloud.com ffisher98@gmail.com ozcir22@mac.com mstewart95@outlook.com baile513@msn.com aigkbtdmnq@att.net hbarr28@gmail.com burtf31@yahoo.com teddyr78@att.net ccalhoun@live.com wrasmussen@mac.com kir6754@verizon.net hcochran@outlook.com hmeyer29@me.com aubreyh@live.com cramos56@sbcglobal.net mhunter@aol.com sfuentes@outlook.com donnym84@me.com keit55@mac.com cspears@live.com gvaldez52@verizon.net acharles53@live.com coffe5429@hotmail.com fbishop@gmail.com jmorales87@mac.com jonasc32@me.com peter4280@icloud.com hoope8340@icloud.com
805-324-5310
509-735-5037
479-370-6824
517-610-2685
601-571-9567
811-230-2024
800-514-7080
615-208-3677
957-802-8298
649-808-2639
641-800-1884
284-474-5209
336-422-7446
211-825-1882
857-975-5724
802-417-3513
315-699-1661
802-231-2555
516-566-2494
811-752-7869
512-355-5025
710-478-3968
473-379-1236
911-939-5787
619-864-2272
702-520-2633
972-237-5021
435-270-1776
957-844-5572
345-325-5854
857-799-1123
423-972-1868
732-512-2111
303-324-8947
337-289-6754
201-549-6070
811-663-1391
231-306-7737
877-683-2440
317-977-9813
321-942-6841
590-892-9217
805-838-5008
                                                                                                                                                                            
       Shirley Carrillo Anderson Gibson Millard Foster Stephen Workman Rex Gonzalez
Loyd Morris Alonzo Mckee Aron Wise Shelby Pope Robby Riggs Tyron Cooper Domingo Carpenter Walker Castro Elliot Goodwin Elliott Garcia Cedrick May Zack Golden Dannie Young Ned Hansen Bennett Andrews Jacques Golden Larry Hickman Jayson Aguirre Hugo Haney Isidro Slater
Chas Wolfe Coleman Duncan Augustine Burton Terrence Wooten
Odis George
Cory Bruce
Willard Koch
Winford Norton
Rubin Alston Dino Skinner Grady Clarke Trevor Murray Chase Macias Shad Ayers Domenic Wise Cory Combs Brooks Lang
shirleyc43@gmail.com agibson78@gmail.com millardf16@gmail.com sworkman10@mac.com rgonzalez19@yahoo.com lmorris@icloud.com amckee52@hotmail.com awise70@outlook.com spope39@hotmail.com tqqfpjflk38@comcast.net lsdjhcpu86@hotmail.com
dcarpenter50@sbcglobal.net wcastro99@hotmail.com egoodwin13@verizon.net egarcia36@outlook.com cmay@icloud.com zackg45@icloud.com dyoung42@me.com nhansen69@live.com bandrews32@msn.com jgolden18@yahoo.com lhickman@verizon.net jaguirre9@outlook.com hhaney26@live.com mudcejrd85@verizon.net chasw@gmail.com cduncan85@hotmail.com aburton57@optonline.net jusdkxph@gmail.com dbbzbwb91@optonline.net cbruce4@live.com vgblyq10@optonline.net wnorton23@hotmail.com rubina87@hotmail.com dskinner51@live.com gclarke91@outlook.com tmurray74@me.com cmacias98@sbcglobal.net ayer7122@icloud.com dwise43@msn.com ccombs32@outlook.com blang@gmail.com
862-903-5577
971-459-6814
832-973-8787
724-235-8718
401-388-1482
620-456-6406
604-970-5352
205-650-8301
503-692-6921
832-401-6373
627-940-2958
412-988-2153
702-441-4902
660-228-3120
970-346-7317
900-515-8022
412-274-5147
811-671-7274
844-981-7131
928-363-1271
928-648-5234
607-685-6515
845-732-8332
671-685-2562
517-354-9683
585-457-1628
415-651-9418
910-892-9556
678-559-8557
716-725-1472
306-223-8164
268-361-9914
975-333-6787
928-890-6926 626-879-6822 207-211-9430 843-386-9067 260-456-3631 216-779-2942 360-527-4014 207-490-9134 754-826-3039
                                                                                                                              
       Jeffry Bush
Josh Benjamin Mohamed Peck Keneth Rios
Jeff Owen
Lewis Curtis Waldo Christian Rhett Compton Chas Frank Gabriel Briggs Chang Kemp Joel Tillman Thanh Pratt Jerrod Blackwell Brant Kidd Antonio Moody Elmer Mathis Efren Adkins Jon Gibson Ivory Mercer Moises Mooney Stuart Barnes Herb Baxter Xavier Hatfield Odell Cantu Basil Craig Raphael Mckay Edmundo Diaz Charles Abbott Garret Mosley
Cyrus Maynard
Armand Newman
Julius Cantu
Lacy Hancock
Darnell Pate
Wm Kemp
Rod French
Denis Mcintyre
Lawrence Alexander
Gil Hamilton Norbert Randolph Milton Nash
jeffryb92@optonline.net jbenjamin65@gmail.com mpeck88@hotmail.com rio8048@live.com jarhuhq77@aol.com lcurtis51@live.com waldoc76@me.com rcompton27@yahoo.com cfrank48@gmail.com gbriggs94@att.net ckemp@outlook.com jtillman@hotmail.com thanhp86@comcast.net jerrodb66@hotmail.com bkidd3@mac.com amoody@att.net emathis75@hotmail.com eadkins81@live.com jgibson42@hotmail.com imercer@outlook.com mmooney77@icloud.com sbarnes99@verizon.net xhkas57@icloud.com xhatfield64@yahoo.com cant705@me.com bcraig@outlook.com rmckay20@hotmail.com edmundod56@msn.com cabbott31@optonline.net njulvhcn93@att.net cmaynard16@gmail.com anewman77@verizon.net jcantu@outlook.com lacyh31@sbcglobal.net dpate81@optonline.net wkemp90@msn.com zrspofejaq8@me.com mcintyr4071@aol.com
maljsrrm@me.com ghamilton@hotmail.com nrandolph86@aol.com mnash4@gmail.com
949-397-1831
609-482-9780
480-944-6768
803-578-4079
740-757-4030
866-589-2878
276-754-5930
813-698-9067
419-776-9055
914-618-8277
484-757-3289
833-559-8496
334-637-9844
703-991-2866
213-314-5841
440-223-7802
954-793-2175
561-397-1896
959-251-2438
717-802-4300
717-785-7593
832-216-4922
303-973-9806
614-606-2670
268-276-2651
700-574-4217
409-477-5735
760-508-9852
278-426-9095
787-476-3853
787-691-9912
351-885-2122
862-718-4191
510-576-2942
856-249-2703
283-747-8595
580-653-8630
570-718-5678
260-546-5128
500-453-3492
254-824-5463
660-468-5254
                                                                                                                                                                      
   Damon Potts
   dpotts97@optonline.net
  320-495-8716
   Mitch Wilkinson
   mwilkinson@aol.com
  520-913-4849
   Reynaldo Pickett
   rpickett25@att.net
  615-931-7580
   Alphonse Wolfe
   awolfe@comcast.net
  214-884-3779
   Faustino Crane
   fcrane93@live.com
  507-334-3277
   Hayden Carlson
   hcarlson78@hotmail.com
  870-657-6522
   Ethan Torres
   etorres40@hotmail.com
  478-216-1711
   Chester Sandoval
   sandova9646@live.com
  514-896-7404
   Sam Langley
   slangley@gmail.com
  500-500-3314
   Rafael Harrell
   vrwj74@icloud.com
  763-924-7904
   Ezequiel Hampton
    ehampton58@optonline.net
    970-588-7047
   Lewis Williamson
 imaucos@live.com
 661-232-5367
   Denis Valdez
   dvaldez60@me.com
  562-518-8825
   Lucien Glenn
   glen9@msn.com
  628-344-5680
   Morgan Lloyd
   mlloyd10@hotmail.com
  969-653-3615
   Courtney Reilly
   creilly61@sbcglobal.net
  734-327-6388
   Arturo Hobbs
   arturoh31@gmail.com
  385-299-9749
   Alberto Hoffman
   ahoffman@aol.com
  712-661-3487
   Arlie Hill
   hil3545@gmail.com
  360-263-4384
  Pete Ayala
   ayal9762@me.com
   302-778-8742
  Solomon Salazar
     284-338-3975
      aateg@aol.com
   Clyde Evans
  540-681-8060
 cevans13@live.com
  Burton Ware
     219-692-2356
   bware52@msn.com
  Jermaine Chang
      754-751-6646
      jchang98@gmail.com
   Carson Bryant
  646-974-9671
 carsonb3@verizon.net
  Garland Meadows
     511-708-3208
   gmeadows25@optonline.net
  Robert Craig
     360-959-6205
   rcraig20@me.com
  Pete Bowen
      517-382-3381
      pbowen17@icloud.com
   Cleo Roman
  248-625-9398
 croman18@optonline.net
  Chet Gould
     702-555-3916
   oqjccy36@outlook.com
  Pat Keller
      316-324-9162
      patk15@mac.com
   Abdul Mcmahon
  201-949-5545
 amcmahon4@gmail.com
  Brock Alston
     712-527-1022
   alsto3815@live.com
  Ron Nguyen
     416-878-7482
   gazvrfrtk@mac.com
  Antone Byers
     787-868-6561
   byer3769@outlook.com
  Tad Rhodes
      312-873-6991
      trhodes86@hotmail.com
   Pedro Christensen
  706-427-9083
 pchristensen42@icloud.com
  Reginald Mitchell
      877-666-4112
      rmitchell60@comcast.net
   Lon Sanchez
  250-861-4906
 lsanchez46@me.com
  Quinn Stafford
     586-397-4519
   qstafford@yahoo.com
  Armand Lancaster
      620-579-2169
      alancaster40@me.com
  
      Oscar Morrison Chad Hewitt
Lou Espinoza German Juarez Chase Bullock Margarito Farley Ramiro Wright
Eddy Sherman Clinton Doyle Monroe Stevens Clay Tyler
Ruben Graves
Lane Kirk
Shayne Collier
Otha Brock
Robby Jordan
Bret Garcia Marcellus Velasquez Darell Kane
Herb Joseph Sergio Watts Jarrett Colon Graig Lester Tyler Alvarado Harris Duran Nestor Page Perry Ellison Earl Cantrell Modesto Strong Galen Kidd
Abe Melton Salvatore Peterson Josh Franks
Del Howe
Vicente Wolf Jordan Bass Santos Sanders Jarred Farmer Ezekiel Allison
Eloy Love
Kevin Delaney Chase Valenzuela
508-405-5015 607-718-7246 882-284-1717 276-391-3652 920-671-2378 975-201-8332 822-403-4750 231-595-3324 631-975-3387 305-907-3140 412-638-7724 724-723-3759 881-337-7390 757-809-2413 407-774-5107 915-287-5137 910-869-3090 606-276-4621 882-280-7095 509-429-1943 541-475-7662 309-508-1355 740-267-4233 501-409-1473 801-504-1087 559-670-5302 201-665-2121 352-331-5192 802-352-7505 704-324-8184 737-660-1617 747-812-2712 908-744-2720 330-492-1841 940-822-6951 818-252-2721 913-432-1517 662-620-8019 904-409-8657 956-460-2704 412-984-5650 405-295-7426
morriso963@live.com hewit4282@att.net lespinoza86@me.com juare3314@hotmail.com cbullock@icloud.com mfarley26@sbcglobal.net wrigh2662@aol.com esherman@hotmail.com cdoyle@me.com mstevens60@hotmail.com ctyler25@me.com wthg6@gmail.com lkirk72@optonline.net scollier53@comcast.net othab30@comcast.net rjordan@verizon.net bgarcia71@aol.com slzcwg65@gmail.com dkane58@yahoo.com herbj15@gmail.com swatts20@yahoo.com jcolon51@live.com glester8@att.net talvarado94@msn.com dura5281@aol.com npage@aol.com pellison64@msn.com ecantrell11@msn.com mstrong36@icloud.com gkidd39@optonline.net abem94@mac.com lbzj22@live.com jfranks@hotmail.com dhowe@mac.com vwolf38@live.com jordanb7@aol.com zcochs@yahoo.com jarredf49@me.com ezekiela44@gmail.com elove16@att.net zjyjmxqmra62@outlook.com cvalenzuela48@att.net
                                                                                                                                                                                                                          
      Ken Schroeder Dillon Thornton Kristopher House Lucio Douglas Alfonso Butler Dwain Murphy Chung Simon Nathanael Randolph Russ Padilla
Charles Williams Evan Watkins Travis Munoz Kasey Mendez Abdul Owen Laurence Levine Mauro Blackburn Waldo Faulkner Lewis Pruitt
Kent Carson
Earle Rogers
Lacy Cortez
Moshe Eaton
Gale Hodge Columbus Ellison Buddy Davenport Jonah Winters Reuben Estes Alexander Mcintosh Hilton Mann Chester Valenzuela Rory Frazier
Sid Campos Ken Dawson Roland Buck Jeffery Bray Alfred Britt Mike Howell Cedric Harrell Antione Baker Graig Morrison Alex Cantu Cristobal Green
662-232-8483 911-729-7310 704-597-7710 646-401-4421 947-418-2138 512-617-6333 617-608-5697 918-836-5453 660-723-4047 340-243-5059 567-645-6231 312-321-3459 664-390-4772 704-806-7715 811-529-6184 440-883-4270 704-851-1305 306-308-5554 669-287-1101 606-301-9233 603-619-3984 369-388-5135 211-804-9027 609-603-5875 807-633-8743 574-288-7526 442-493-2585 867-973-4264 614-534-6204 705-967-9230 229-749-9282 850-461-5256 868-388-6332 809-571-4553 704-894-9878 714-915-5120 671-514-2487 848-959-8580 712-778-8373 800-419-7915 767-760-9879 920-514-8429
ukxetboxf@outlook.com dthornton13@live.com hous49@mac.com ldouglas76@outlook.com abutler32@live.com dmurphy62@sbcglobal.net csimon@att.net kwtvektf11@gmail.com russp63@gmail.com cwilliams97@verizon.net ewatkins92@aol.com iemcbryipl69@sbcglobal.net kmendez27@comcast.net aowen44@sbcglobal.net llevine9@mac.com mblackburn7@hotmail.com uxuhoxw88@hotmail.com lpruitt@gmail.com ixzpuyo66@hotmail.com erogers2@comcast.net lcortez@gmail.com meaton70@mac.com ghodge@sbcglobal.net columbuse82@outlook.com bdavenport@mac.com winter5659@att.net restes3@verizon.net alexanderm24@msn.com hmann59@yahoo.com cvalenzuela67@me.com rfrazier61@optonline.net scampos93@yahoo.com gefcnxvuo28@gmail.com rbuck46@verizon.net jbray68@optonline.net abritt10@msn.com mhowell@sbcglobal.net charrell@gmail.com abaker@icloud.com graigm83@aol.com acantu31@verizon.net cgreen81@icloud.com
                                                                                                                                                                                                                          
      Toby Pearson
Kirk Cote
Albert Chaney Lino Harper Gerald Jacobs Lindsay Malone Joseph Goff
Glen Head
Tyree Vazquez Teddy Golden Vern Mason Miguel Leach Lauren Mason Tommie Vinson Allen Hopkins Warner Mcgowan Kip Floyd
Kirk Slater
Tracey Moon Ronald Knowles Elton Chapman Jasper Saunders Craig Cabrera Roger Ruiz
Sid George Deangelo Vaughan Sidney Reeves Porfirio Moon Jonah Serrano Alvaro Fuentes Darwin Walters Riley Gallagher Josh Coleman Jarvis Skinner Elroy Carroll
Robt Randolph Rocco Rodriguez Avery Morales Travis Avila
Rico Byrd
Alfonso Rogers Zackary Mueller
979-615-8194 407-368-1707 517-934-5775 484-864-4308 882-932-5737 216-535-7866 586-712-7233 678-692-2952 605-987-7999 714-572-3513 650-877-3804 341-579-1479 210-760-8311 204-838-7059 424-452-8638 731-702-4288 706-840-4421 239-202-9045 456-417-9695 331-901-2186 832-700-5909 615-855-2852 518-958-2402 262-997-7396 564-927-4219 511-532-2766 913-302-1126 623-819-8400 312-974-7442 830-703-5401 767-708-9905 416-760-6930 740-835-9107 919-309-9882 806-955-2940 517-690-7444 754-521-8827 757-950-9394 801-582-1623 602-334-2268 720-231-4309 413-219-2761
pearso1658@gmail.com zgnpqlhltg94@icloud.com achaney35@me.com lharper37@aol.com jacob3024@icloud.com lmalone15@icloud.com jgoff10@icloud.com hea9668@msn.com tvazquez69@att.net tgolden74@comcast.net vmason@sbcglobal.net leac289@yahoo.com laurenm75@aol.com jgwjfme29@yahoo.com ahopkins61@att.net warnerm72@hotmail.com kfloyd76@hotmail.com slate638@gmail.com tmoon80@outlook.com rknowles64@verizon.net echapman@sbcglobal.net jsaunders@icloud.com cabrer5597@sbcglobal.net rruiz80@msn.com sidg22@me.com deangelov98@msn.com sreeves53@live.com pmoon84@att.net jserrano@comcast.net alvarof71@att.net walter6016@me.com rgallagher46@live.com jcoleman@yahoo.com jarviss1@hotmail.com zvslhawecs@live.com rrandolph68@gmail.com rrodriguez17@optonline.net amorales91@outlook.com tavila@att.net pjro@gmail.com arogers@me.com zmueller88@optonline.net
                                                                                                                                                                                                                          
      Randall Davis Pasquale Chen Hai Contreras Dewey Donovan Wendell Bowman Miles Carpenter Marlin Thornton Peter Love
Evan Pittman Carroll Bullock Rosendo Kirby Jarrod Wilson Tyler Richard Sammie Pace Marcellus Acevedo Mario Atkins Donnie Finch Lucius Mcdaniel Alvin Hutchinson Benny Ward
Paul Wallace Courtney Beck Junior Maddox
Rey Acosta
Carlo Cruz Chadwick Juarez Dean Hooper Ramon Lara
Jewell Petty
Max Warren
Elvis Miranda Jewell Clarke George Christensen Gavin Poole
Seth Paul Sammie Ellison Barton Nichols Brett Patterson Isidro Nieves Kent Faulkner Charles Bolton Josiah Knight
832-308-7198 763-392-6690 208-717-9659 410-794-4397 900-510-8520 811-923-5052 604-456-6749 708-959-5284 717-451-2756 337-672-7915 859-834-4141 310-296-4069 409-712-6453 501-840-6906 754-653-6084 264-590-6665 564-637-2215 713-290-9465 900-446-5048 719-895-9108 682-385-9427 420-722-2968 660-344-4688 208-419-8576 810-517-6381 464-625-4489 775-410-7394 327-640-3130 710-817-5065 802-677-2487 464-590-4144 317-204-9567 752-688-3779 360-506-5027 414-485-6912 737-369-5205 224-932-7915 660-317-1885 304-331-3182 661-892-8158 709-560-6738 623-754-9047
rdavis3@gmail.com pchen@outlook.com haic98@verizon.net ddonovan50@att.net wendellb26@icloud.com mcarpenter51@msn.com mthornton27@yahoo.com ahanaqwcvp28@yahoo.com isd@aol.com cbullock49@me.com rosendok42@yahoo.com jwilson@hotmail.com trichard@me.com space@sbcglobal.net macevedo10@gmail.com marioa41@hotmail.com dfinch84@sbcglobal.net lmcdaniel33@hotmail.com aleh24@yahoo.com bward25@att.net pwallace@optonline.net cbeck64@att.net jmaddox85@sbcglobal.net racosta@live.com ccruz33@optonline.net chadwickj@aol.com hoope23@me.com lar52@comcast.net jpetty@me.com mwarren@outlook.com elvism@comcast.net nuu61@icloud.com christense3094@icloud.com gpoole13@att.net spaul62@optonline.net sellison37@comcast.net nichol6482@sbcglobal.net bpatterson6@yahoo.com inieves71@comcast.net kfaulkner7@mac.com cbolton@live.com iyccvuo93@aol.com
                                                                                                                                                                                                                          
  Lupe Benjamin
     613-644-1136
      benjami8413@optonline.net
   Elliot Gonzalez
  206-501-5134
 elliotg37@me.com
  Bobby Dean
     641-659-3811
   bdean72@aol.com
  Amos Price
     717-690-6787
   aprice95@hotmail.com
  Kerry Schroeder
     260-446-7362
   kschroeder@comcast.net
  Wes Pate
      417-354-6961
      wpate99@verizon.net
   Cleveland Mann
  415-375-3287
 cmann79@live.com
  Norbert Vinson
     385-868-1852
   nvinson8@hotmail.com
  Milton Wade
     931-883-8104
   mwade90@gmail.com
  Lauren Barnett
     573-991-4106
   lbarnett80@sbcglobal.net
  Cary Kirby
      859-271-7097
      ckirby9@msn.com
  Biostatistician Officer Assistant Intelligence Counting Representative Sales
C-Level
Well Manager Receptionist Sales Business Director Metal
VP Administrator Media Technology Chief Improvement Social Engineer Operations Brand Producer Orderly
(CIO)
Chief
Sales Authorizer
Clark Salinas Hugo Cross Domenic Molina Calvin Ayers Thomas Sawyer Danny William Samuel Solomon Sydney Sutton Stewart Harrell Ken Gardner Eddie Emerson Roosevelt Welch Ernie Russell Josef Holder Fletcher Johns Bryce Ortega Sheldon Lester Lenard Berry Merrill Chan
Chi Cameron Young Joyce Quincy Schroeder Refugio Lopez Nelson Fox Chang Glass Arnoldo Maynard Donnell Dudley Britt Stout Gilbert Dillon Rodrick Rojas Dewitt Vega
845-641-5553 500-760-4858 256-975-9610 337-838-9148 352-421-3126 600-925-9300 505-206-9958 835-752-9580 701-478-9209 248-330-7997 308-996-8347 700-827-1719 620-789-4914 767-759-3917 664-249-7260 734-953-8555 670-461-8880 661-543-3087 719-476-8186 336-785-6554 270-966-2464 609-767-9156 671-478-1186 636-205-1065 708-519-6690 567-993-7583 323-311-8849 954-290-5167 737-908-8008 724-458-5072 281-349-5499
csalinas16@mac.com hcross@optonline.net dmolina@me.com calvina46@optonline.net tsawyer14@live.com dwilliam23@comcast.net ssolomon59@icloud.com ssutton97@outlook.com harrel9997@icloud.com kgardner63@msn.com eemerson@att.net rwelch10@verizon.net erussell@sbcglobal.net jholder76@comcast.net fletcherj30@icloud.com bortega64@aol.com leste5473@sbcglobal.net lberry46@sbcglobal.net mchan@yahoo.com ccameron69@att.net hmpvqjoa46@outlook.com schroede2388@sbcglobal.net rlopez58@gmail.com nfox93@gmail.com cglass17@verizon.net maynar1865@hotmail.com dmfovekv30@me.com stou1718@gmail.com gdillon46@live.com rrojas79@sbcglobal.net dvega19@att.net

Painter
Sales
Media
Engineer Payable/Receivable Entry
Geological Officer Coordinator Representative of
Entry
Biological Public Medical Officer Cloud Graphic Officer Computer Benefits Office Loan Laboratory Customer Associate
Associate Outside Pipefitter Assistant Manager
Sales
C-Level Representative Pharmacist Engineer Account Technician Supervisors Supervisor (CIO)
Analyst
Greg Bradford Ismael Hood Javier Robinson Zack Marquez Brice Compton Damien Weaver Scott Gibbs Benjamin Ferrell Delbert Morrison Isaiah Freeman Hector Hess Dana Massey Kristopher Petersen
Boris Rivers Jorge Harrison Maurice Casey Enrique Sawyer Jewell Downs Ellis Weber
Lee Best
Alden Whitney Andre Pickett Alonso Woodard Stan Cleveland Vance Prince Kirby Hensley Rolando Chapman
Eric Ball
Hilton Matthews Daryl Duke
Logan Jacobson Jeremiah Rivas Eliseo Bauer Hugo Justice Wilfred Lloyd Homer Pierce Lawerence Sweet Bobby Grimes Shon Pittman Lloyd Holloway Edwin Pratt Lionel Bush
262-820-4152 606-234-6374 709-585-7066 450-634-7241 580-596-6155 464-308-4946 918-309-9419 213-748-2704 563-448-3826 331-792-6315 732-387-3313 246-581-8092
562-851-4009 240-895-6681 858-334-8209 334-830-4816 234-996-5407 415-598-3660 835-677-9574 276-748-3451 330-499-3030 585-858-1317 551-513-1029 937-818-1903 618-678-4534 612-533-9615
803-434-1882 406-895-8654 516-281-3409 830-449-7659 339-410-7481 234-821-7223 954-550-9499 253-542-2779 764-390-6339 985-687-2410 800-590-9014 682-780-2792 600-756-2467 401-866-3137 307-263-3138 937-900-4399
gbradford77@verizon.net ihood41@comcast.net javierr@msn.com zmarquez48@live.com bcompton58@mac.com dweaver90@aol.com sgibbs76@mac.com ziaqn32@live.com dmorrison48@verizon.net ifreeman@outlook.com hhess38@aol.com dmassey@verizon.net
qdkmws84@mac.com brivers@yahoo.com jharrison90@comcast.net mcasey42@outlook.com esawyer71@mac.com jdowns47@me.com eweber36@me.com leeb42@msn.com whitne8050@att.net picket3817@live.com awoodard86@mac.com scleveland23@aol.com vprince47@outlook.com khensley@comcast.net
rchapman23@comcast.net ericb55@gmail.com hmatthews@outlook.com pzqzby10@sbcglobal.net ljacobson@comcast.net vvqvizja8@me.com tdjk78@msn.com justic7939@optonline.net wlloyd@aol.com pierc3069@icloud.com lawerences@live.com bgrimes@att.net pittma7860@icloud.com lholloway71@verizon.net epratt@aol.com lbush@msn.com

Developer Ethical Coordinator Cleaner Engineer Researcher
Williams Sawyer Abram Haney Barney Sanchez Robert Jefferson Rosario Moses Jesse Guthrie
864-281-9229 671-786-3117 516-809-9156 502-231-2744 352-944-3271 877-969-3462
sawye65@yahoo.com cbtuky10@aol.com bsanchez28@outlook.com rjefferson68@optonline.net rmoses@me.com jguthrie76@outlook.com
Consultant, Franklin Mitchell, 402-787-1071, franklinm19@msn.com Financial, Odell Blackburn, 809-961-6647, blackbur9571@gmail.com Taper, Chad Cervantes, 415-950-8689, ccervantes77@msn.com Care, Chet Durham, 224-525-5964, cdurham50@msn.com Relations, Leslie Lester, 901-981-1453, toixcrjopk79@hotmail.com Manager, Conrad Acosta, 309-738-4792, svrxmkxp@comcast.net CIO—Chief, Pat Dickson, 868-453-1548, pdickson14@msn.com Administrator, Tony Alford, 425-667-1206, talford73@live.com Computer, Maximo Molina, 847-242-1903, maximom58@me.com Motion, Dale Silva, 360-923-6219, silv58@outlook.com
Associate, Tim Ferrell, 236-831-4749, tferrell82@verizon.net
Digital, Lavern Briggs, 646-573-7286, lbriggs59@hotmail.com
Brand, Clyde Sellers, 880-758-9012, rcn14@optonline.net
Resources, Rolland Miranda, 814-825-6659, rmiranda90@verizon.net Manager, Ned Davenport, 868-537-8850, ndavenport8@gmail.com Medical, Alden Kirby, 574-528-9602, akirby82@comcast.net Computer, Antione Harvey, 732-995-8604, aharvey7@aol.com Operating, Bret Bruce, 513-704-8737, bbruce99@me.com
Lead, Nathanael Marsh, 202-689-6810, nmarsh@aol.com Artificial, Odis Nunez, 201-626-6879, onunez@sbcglobal.net Film, Manual Brennan, 510-505-3719, mbrennan@live.com

Solar, Bart Donovan, 717-297-6940, bdonovan41@outlook.com Electrical, Delbert Burt, 405-437-7498, dburt20@optonline.net or, Rocco Stone, 860-529-5931, rstone1@att.net
Assistant, Rico Blackwell, 445-306-1341, rblackwell@mac.com SQL, Seymour Gordon, 236-269-1791, sgordon2@aol.com Payroll, Gail Lang, 828-668-6177, glang5@live.com
Robot, Noe Myers, 289-953-2219, aupqzrku84@outlook.com Novelist/Writer, Ryan Estrada, 767-781-1015, llsfmma@icloud.com Solar, Cristobal Wiggins, 905-210-9724, cwiggins60@optonline.net Production, Solomon Bolton, 218-846-8390, bolto28@mac.com Product, Darius Riley, 918-517-2683, pleduuntz68@icloud.com Retail, Parker Cameron, 865-218-2016, pcameron64@mac.com Officer, Gus Pollard, 283-951-6724, gpollard8@hotmail.com Hacking, Deshawn Reyes, 737-733-5204, dreyes50@icloud.com Personal, Jude Gallegos, 240-679-3122, judeg74@optonline.net Product, Emmett English, 509-813-6551, eenglish29@mac.com Impressions, Fred Mcintyre, 916-367-3767, fmcintyre8@mac.com Drafter, Rex Tillman, 920-535-4810, rtillman@icloud.com Manager, Milton Joyner, 602-767-1562, mjoyner73@mac.com

'''

#Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(( (\d\d\d) | (\(\d\d\d\)) )?    #area code (optionnal)
(-|\s)?                         #first separator(optionnal)
(\d{3})                         #first 3 digits
-                               #second separator
(\d{4})                         #last 4 digits
(\s(ext(\.)?\s|x)               #extension (optionnal)
(\d{2,5}))?)                     #number extension (optionnal)

''', re.VERBOSE)


#Create a regex for emails
mailRegex = re.compile(r'''
#some._+(\d){0,10}thing@mail.thing

[a-zA-Z._+0-9]+            #name part
@                         #@ part
[a-zA-Z._+0-9]+            #domain part

''', re.VERBOSE)


#Get the text off the clipboard
listMails = mailRegex.findall(text)
listPhones = phoneRegex.findall(text)

allPhoneNumbers = []
for phone in listPhones :
    allPhoneNumbers.append(phone[0])
    

# TODO : Extract the email/phone numbers from this text
result = '\n'.join(listMails) + '\n' + '\n'.join(allPhoneNumbers)
pyperclip.copy(result)
