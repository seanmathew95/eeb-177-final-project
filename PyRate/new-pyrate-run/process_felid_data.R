source("~/PyRate/pyrate_utilities.r")

# we need to give the utilities a list of extant species
# looked at ouput graph of occurrences to see which species in the dataset are considered extant
extant_cats = c("Panthera tigris", "Panthera pardus", "Panthera onca",'Panthera leo','Lynx rufus','Felis silvestris','Felis serval','Felis rufus','Felis libyca','Felis concolor','Felis caracal','Acinonyx jubatus')

# use the extract.ages.pbdb() function in pyrate_utilities to reformat our dataset...

extract.ages.pbdb(file= "felidae_occ.csv", extant_species=extant_cats)


extract.ages.pbdb()
