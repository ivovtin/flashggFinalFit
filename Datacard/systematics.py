# Python file to store systematics:

# Comment out all nuisances that you do not want to include

# THEORY SYSTEMATICS:

# For type:constant
#  1) specify same value for all processes
#  2) define process map json in ./theory_uncertainties

# For type:factory
# Tier system: adds different uncertainties to dataframe
#   1) shape: absolute yield of process kept constant, shape effects i.e. calc migrations across cats
#   2) ishape: as (1) but absolute yield for proc x cat is allowed to vary
#   3) norm: absolute yield of production mode (s0) kept constant but migrations across sub-processes e.g. STXS bins.Same value in each category.
#   4) inorm: as (3) but absolute yield of production mode (s0) can vary
#   5) inc: variations in production mode (s0), same value for each subprocess in each category
# Relations: shape = ishape/inorm
#            norm  = inorm/inc
# Specify as list in dict: e.g. 'tiers'=['inc','inorm','norm','ishape','shape']

theory_systematics = [
                # Normalisation uncertainties: enter interpretations
                {'name':'BR_hgg','title':'BR_hgg','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"0.98/1.021"},
                # If using STXS splitting: replace QCDScale with dedicated STXS uncertainties
                {'name':'QCDscale_ggH','title':'QCDscale_ggH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggh.json'},
                {'name':'QCDscale_qqH','title':'QCDscale_qqH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_qqh.json'},
                {'name':'QCDscale_VH','title':'QCDscale_VH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_vh.json'}, # Note: VH had components accounted for in THU_qqH_*, set to 1 in json
                {'name':'QCDscale_ggZH','title':'QCDscale_ggZH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggzh.json'},
                {'name':'QCDscale_ttH','title':'QCDscale_ttH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_tth.json'},
                {'name':'QCDscale_tHq','title':'QCDscale_tHq','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thq.json'},
                {'name':'QCDscale_tHW','title':'QCDscale_tHW','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thw.json'},
                {'name':'QCDscale_bbH','title':'QCDscale_bbH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_bbh.json'},
                # Pdf uncertainties
                {'name':'pdf_Higgs_ggH','title':'pdf_Higgs_ggH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggh.json'},
                {'name':'pdf_Higgs_qqH','title':'pdf_Higgs_qqH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_qqh.json'},
                {'name':'pdf_Higgs_VH','title':'pdf_Higgs_VH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_vh.json'},
                {'name':'pdf_Higgs_ggZH','title':'pdf_Higgs_ggZH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggzh.json'},
                {'name':'pdf_Higgs_ttH','title':'pdf_Higgs_ttH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_tth.json'},
                {'name':'pdf_Higgs_tHq','title':'pdf_Higgs_tHq','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thq.json'},
                {'name':'pdf_Higgs_tHW','title':'pdf_Higgs_tHW','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thw.json'},
                # alpha S uncertainties
                {'name':'alphaS_ggH','title':'alphaS_ggH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggh.json'},
                {'name':'alphaS_qqH','title':'alphaS_qqH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_qqh.json'},
                {'name':'alphaS_VH','title':'alphaS_VH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_vh.json'},
                {'name':'alphaS_ggZH','title':'alphaS_ggZH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_ggzh.json'},
                {'name':'alphaS_ttH','title':'alphaS_ttH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_tth.json'},
                {'name':'alphaS_tHq','title':'alphaS_tHq','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thq.json'},
                {'name':'alphaS_tHW','title':'alphaS_tHW','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'theory_uncertainties/thu_thw.json'},

                # Shape uncertainties: calculated from weights in the input workspace
                # Scale weights are grouped: [1,2], [3,6], [4,8]
                #{'name':'scaleWeight_0','title':'CMS_hgg_scaleWeight_0','type':'factory','prior':'lnN','correlateAcrossYears':1}, # nominal weight
                {'name':'scaleWeight_1','title':'CMS_hgg_scaleWeight_1','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape','mnorm']},
                {'name':'scaleWeight_2','title':'CMS_hgg_scaleWeight_2','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape','mnorm']},
                {'name':'scaleWeight_3','title':'CMS_hgg_scaleWeight_3','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape','mnorm']},
                {'name':'scaleWeight_4','title':'CMS_hgg_scaleWeight_4','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape','mnorm']},
                #{'name':'scaleWeight_5','title':'CMS_hgg_scaleWeight_5','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['norm','shape']}, #Unphysical
                {'name':'scaleWeight_6','title':'CMS_hgg_scaleWeight_6','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape','mnorm']},
                #{'name':'scaleWeight_7','title':'CMS_hgg_scaleWeight_7','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['norm','shape']}, #Unphysical
                {'name':'scaleWeight_8','title':'CMS_hgg_scaleWeight_8','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape','mnorm']},
                {'name':'alphaSWeight_0','title':'CMS_hgg_alphaSWeight_0','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
                {'name':'alphaSWeight_1','title':'CMS_hgg_alphaSWeight_1','type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']},
              ]
for i in range(1,60): theory_systematics.append( {'name':'pdfWeight_%g'%i, 'title':'CMS_hgg_pdfWeight_%g'%i, 'type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']} )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# EXPERIMENTAL SYSTEMATICS
# correlateAcrossYears = 0 : no correlation
# correlateAcrossYears = 1 : fully correlated
# correlateAcrossYears = -1 : partially correlated

experimental_systematics = [
                {'name':'lumi_13TeV_Uncorrelated','title':'lumi_13TeV_Uncorrelated','type':'constant','prior':'lnN','correlateAcrossYears':0,'value':{'2016':'1.022','2017':'1.020','2018':'1.015'}},
                {'name':'lumi_13TeV_X_Y_Factorization','title':'lumi_13TeV_X_Y_Factorization','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.009','2017':'1.008','2018':'1.020'}},
                {'name':'lumi_13TeV_Length_Scale','title':'lumi_13TeV_Length_Scale','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'-','2017':'1.003','2018':'1.002'}},
                {'name':'lumi_13TeV_Beam_Beam_Deflection','title':'lumi_13TeV_Beam_Beam_Deflection','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.004','2017':'1.004','2018':'-'}},
                {'name':'lumi_13TeV_Dynamic_Beta','title':'lumi_13TeV_Dynamic_Beta','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.005','2017':'1.005','2018':'-'}},
                {'name':'lumi_13TeV_Beam_Current_Calibration','title':'lumi_13TeV_Beam_Current_Calibration','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'-','2017':'1.003','2018':'1.002'}},
                {'name':'lumi_13TeV_Ghosts_And_Satellites','title':'lumi_13TeV_Ghosts_And_Satellites','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016':'1.004','2017':'1.001','2018':'-'}},
                {'name':'LooseMvaSF','title':'CMS_hgg_LooseMvaSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'PreselSF','title':'CMS_hgg_PreselSF','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'electronVetoSF','title':'CMS_hgg_electronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'TriggerWeight','title':'CMS_hgg_TriggerWeight','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'MuonIDWeight','title':'CMS_hgg_MuonID','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'MuonIsoWeight','title':'CMS_hgg_MuonIso','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'ElectronIDWeight','title':'CMS_hgg_ElectronID','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'ElectronRecoWeight','title':'CMS_hgg_ElectronReco','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JetBTagCutWeight','title':'CMS_hgg_BTagCut','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JetBTagReshapeWeight','title':'CMS_hgg_BTagReshape','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'prefireWeight','title':'CMS_hgg_prefire','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'SigmaEOverEShift','title':'CMS_hgg_SigmaEOverEShift','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'MvaShift','title':'CMS_hgg_phoIdMva','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'PUJIDShift','title':'CMS_hgg_PUJIDShift','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JECAbsolute','title':'CMS_scale_j_Absolute','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'JECFlavorQCD','title':'CMS_scale_j_FlavorQCD','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'JECBBEC1','title':'CMS_scale_j_BBEC1','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'JECHF','title':'CMS_scale_j_HF','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'JECEC2','title':'CMS_scale_j_EC2','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'JECRelativeBal','title':'CMS_scale_j_RelativeBal','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'JECAbsoluteYEAR','title':'CMS_scale_j_Absolute_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JECBBEC1YEAR','title':'CMS_scale_j_BBEC1_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JECHFYEAR','title':'CMS_scale_j_HF_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JECEC2YEAR','title':'CMS_scale_j_EC2_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JECRelativeSampleYEAR','title':'CMS_scale_j_RelativeSample_y','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JEC','title':'CMS_scale_j','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JER','title':'CMS_res_j','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'metJecUncertainty','title':'CMS_hgg_MET_scale_j','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'metJerUncertainty','title':'CMS_hgg_MET_res_j','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'metPhoUncertainty','title':'CMS_hgg_MET_PhotonScale','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'metUncUncertainty','title':'CMS_hgg_MET_Unclustered','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'JetHEM','title':'CMS_hgg_JetHEM','type':'factory','prior':'lnN','correlateAcrossYears':0}
              ]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Shape nuisances: effect encoded in signal model
signal_shape_systematics = [
                {'name':'CMS_hgg_nuisance_deltafracright','title':'CMS_hgg_nuisance_deltafracright','type':'signal_shape','mean':'0.0','sigma':'0.02'},
                {'name':'CMS_hgg_nuisance_NonLinearity_13TeVscale','title':'CMS_hgg_nuisance_NonLinearity_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'0.002'},
                {'name':'CMS_hgg_nuisance_Geant4_13TeVscale','title':'CMS_hgg_nuisance_Geant4_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'0.0005'},
                {'name':'CMS_hgg_nuisance_HighR9EB_13TeVscale','title':'CMS_hgg_nuisance_HighR9EB_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_HighR9EE_13TeVscale','title':'CMS_hgg_nuisance_HighR9EE_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_LowR9EB_13TeVscale','title':'CMS_hgg_nuisance_LowR9EB_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_LowR9EE_13TeVscale','title':'CMS_hgg_nuisance_LowR9EE_13TeVscale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_ShowerShapeHighR9EB_scale','title':'CMS_hgg_nuisance_ShowerShapeHighR9EB_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_ShowerShapeHighR9EE_scale','title':'CMS_hgg_nuisance_ShowerShapeHighR9EE_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_ShowerShapeLowR9EB_scale','title':'CMS_hgg_nuisance_ShowerShapeLowR9EB_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_ShowerShapeLowR9EE_scale','title':'CMS_hgg_nuisance_ShowerShapeLowR9EE_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_MaterialCentralBarrel_scale','title':'CMS_hgg_nuisance_MaterialCentralBarrel_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_MaterialOuterBarrel_scale','title':'CMS_hgg_nuisance_MaterialOuterBarrel_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_MaterialForward_scale','title':'CMS_hgg_nuisance_MaterialForward_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_FNUFEE_scale','title':'CMS_hgg_nuisance_FNUFEE_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_FNUFEB_scale','title':'CMS_hgg_nuisance_FNUFEB_scale','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EBPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_HighR9EBRho_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EBRho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_HighR9EERho_13TeVsmear','title':'CMS_hgg_nuisance_HighR9EERho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_LowR9EBRho_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EBRho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'},
                {'name':'CMS_hgg_nuisance_LowR9EERho_13TeVsmear','title':'CMS_hgg_nuisance_LowR9EERho_13TeVsmear','type':'signal_shape','mean':'0.0','sigma':'1.0'}
              ]