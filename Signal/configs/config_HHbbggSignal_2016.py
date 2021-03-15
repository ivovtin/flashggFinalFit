# Config file: options for signal fitting

_year = '2016'

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/afs/cern.ch/work/i/ivovtin/public/HHbbgg_ntuples/18_02_2020',
  #'procs':'auto', # if auto: inferred automatically from filenames
  'procs':'hh_node_SM_%s'%_year, # if auto: inferred automatically from filenames
  'cats':'auto', # if auto: inferred automatically from (0) workspace
  'ext':'hhbbgg_%s'%_year,
  'analysis':'', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  ##'analysis':'example', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  ##'analysis':'STXS', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  #'massPoints':'120,125,130',
  'massPoints':'125',

  #Photon shape systematics  
  'scales':'HighR9EB,HighR9EE,LowR9EB,LowR9EE,Gain1EB,Gain6EB', # separate nuisance per year
  'scalesCorr':'MaterialCentralBarrel,MaterialOuterBarrel,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB', # correlated across years
  'scalesGlobal':'NonLinearity,Geant4', # affect all processes equally, correlated across years
  'smears':'HighR9EBPhi,HighR9EBRho,HighR9EEPhi,HighR9EERho,LowR9EBPhi,LowR9EBRho,LowR9EEPhi,LowR9EERho', # separate nuisance per year

  # Job submission options
  #'batch':'IC', # ['condor','SGE','IC','local']
  #'queue':'hep.q'
  'batch':'local', # ['condor','SGE','IC','local']
  #'batch':'condor', # ['condor','SGE','IC','local']
  'queue':'espresso',

}
