# Evolutionary History of Felidae

## Introduction
Felidae is a taxonomic family of cats. Members of Felidae range from the domestic cat to extant big cats, such as lions and tigers, but also extinct members such as the saber-toothed tiger. This project aims to analyze the diversity of Felidae through time. The data utilized in this project is found on the PaleoBiology Database online at paleodb.org. Occurrence data of fossils is downloadable as a CSV file with species name, and an estimate for the age of each fossil in the collection. In order to find species diversity through time, the files are cleaned up with UNIX, then run through python functions to get the data into a plottable format, and finally visualized using R. R is used to plot species diversity through time. Since the fossil ages are estimates, we can use PyRate to statistically analyze more accurate estimates for speciation and extinction. Throughout the history of Felidae, some interesting events include the introduction of melanism, present in many species of cats; the Late Miocene Radiation, which is responsible for the great species diversity we see today; and divergenece between modern cats and now extinct saber-toothed cats, such as the smilodon. Diversity graphs will illustrate these events. In addition to occurrence data, the paleobiology database also houses collection data with information on the locations of the fossils as well as their ages. This information can be used to plot the fossil through time, showing the geographic distribution of Felidae through history.

## References
Christiansen, Per. "Evolution of Skull and Mandible Shape in Cats (Carnivora: Felidae)." PLOS (2008): n. pag. PLOS. Web. <http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0002807&type=printable>. 

Johnson, Warren E., William J. Murphy, Agostinho Antunes, Emma Teeling, Stephen J. O’Brien, Jill Pecon-Slattery, and Eduardo Eizirik. "The Late Miocene Radiat Ion of Modern Felidae : A Genetic Assessment." Science (2006): n. pag. Web. <http://www.imaginiquebengals.com/johnsonsuppl2006.pdf>. 

Eizirik, Eduardo, Eduardo Eizirik, 1,2, * Naoya Yuhki, Warren E. Johnson, Marilyn Menotti-Raymond, Steven S. Hannah, and Stephen J. O’Brien. "Molecular Genetics and Evolution of Melanism in the Cat Family." Current Biology (2003): n. pag. Cell. Web. <http://www.cell.com/current-biology/pdf/S0960-9822(03)00128-3.pdf>.

**See .ipynb files for outlines**
**See .Rmd files for R code used to produce graphs**
**See PyRate folder for script to run PyRate and PyRate output graphs**
**See output_png folder for .png of graphs produced with R**
**See output_pdf fodler for .pdf of graphs produced with R**
