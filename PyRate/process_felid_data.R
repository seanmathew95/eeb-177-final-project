source("~/PyRate/pyrate_utilities.r")

# we need to give the utilities a list of extant species
# looked at ouput graph of occurrences to see which species in the dataset are considered extant
extant_cats = c("Panthera tigris","Panthera leo","Panthera onca","Panthera pardus","Panthera uncia","Neofelis nebulosa","Neofelis diardi","Pardofelis marmorata","Catopuma badia","Catopuma temminckii","Caracal caracal","Caracal aurata","Caracal serval","Leopardus braccatus","Leopardus colocolo","Leopardus geoffroyi","Leopardus guigna","Leopardus guttulus","Leopardus jacobitus","Leopardus pajeros","Leopardus pardalis","Leopardus tigrinus","Leopardus wiedii","Lynx canadensis","Lynx lynx","Lynx pardinus","Lynx rufus","Puma concolor","Puma yagouaroundi","Acinonyx jubatus","Prionailurus bengalensis","Prionailurus bengalensis iriomotensis","Prionailurus planiceps","Prionailurus rubiginosus","Prionailurus viverrinus","Otocolobus manul","Felis catus","Felis chaus","Felis margarita","Felis nigripes","Felis silvestris", "Felis silvestris bieti")


# use the extract.ages.pbdb() function in pyrate_utilities to reformat our dataset...
extract.ages.pbdb(file= "felidae_occ.csv", extant_species=extant_cats)


extract.ages.pbdb()
