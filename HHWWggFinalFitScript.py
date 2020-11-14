###################################################################################################
# 3 September 2020                                                                                                 
# Abe Tishelman-Charny 
#
# The purpose of this module is to run fggfinalfit steps 
# pdfindex_HHWWggTag_0_2017_13TeV
#
# DNN 14 November 2020 
# 
# example directory strucure: /eos/user/a/atishelm/ntuples/HHWWgg_flashgg/TaggerOutput/HHWWgg-SL-SM-NLO-Run2/SM/SL
# Signal
# python HHWWggFinalFitScript.py --Step Signal --mode std --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec ForFggFinalfit --note SLSMNLODNN --DNN --outputDirec /eos/user/a/atishelm/www/HHWWgg/SM-NLO-DNN-Results/
# python HHWWggFinalFitScript.py --Step Signal --mode sigFitOnly --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec ForFggFinalfit --note SLSMNLODNN --DNN --outputDirec /eos/user/a/atishelm/www/HHWWgg/SM-NLO-DNN-Results/
# python HHWWggFinalFitScript.py --Step Signal --mode packageOnly --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec ForFggFinalfit --note SLSMNLODNN --DNN --outputDirec /eos/user/a/atishelm/www/HHWWgg/SM-NLO-DNN-Results/
# python HHWWggFinalFitScript.py --Step Signal --mode sigPlotsOnly --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec ForFggFinalfit --note SLSMNLODNN --DNN --outputDirec /eos/user/a/atishelm/www/HHWWgg/SM-NLO-DNN-Results/

# Background
# python HHWWggFinalFitScript.py --Step Background --mode fTestOnly --physics SM --finalStates SL --years 2016 --dirTypes Data --baseDirec ForFggFinalfit --note SLSMNLODNN --DNN --outputDirec /eos/user/a/atishelm/www/HHWWgg/SM-NLO-DNN-Results/


# Datacards and combine 
# python HHWWggFinalFitScript.py --Step Datacard --mode datacard --physics SM --finalStates SL --years 2017 --note SLSMNLODNN --DNN --dirTypes Datacard --baseDirec ForFggFinalfit
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates SL --years 2016 --note SLSMNLODNN --DNN --dirTypes Datacard --baseDirec ForFggFinalfit
# combine CMS-HGG_mva_13TeV_datacard_HHWWgg_SM-SL_2017_SLNLOstatOnly.txt -m 125 -M AsymptoticLimits --run=blind -t -1

# Combine 
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates SL --years 2017 --note SLSMNLODNN --dirTypes Combine --combineInd --DNN

# python /eos/user/a/atishelm/www/HHWWgg/SM-NLO-Results//SM/SL/2016/python HHWWggFinalFitScript.py --Step Signal --mode sigFitOnly --physics SM --finalStates SL --years 2016 --dirTypes Signal --baseDirec HHWWgg-SL-SM-NLO-Run2 --note SLNLOstatOnly
# ForFggFinalfit
# python HHWWggFinalFitScript.py --Step Signal --mode std --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec HHWWgg-SL-SM-NLO-Run2 --note SLNLOstatOnly
# python HHWWggFinalFitScript.py --Step Signal --mode sigFitOnly --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec HHWWgg-SL-SM-NLO-Run2 --note SLNLOstatOnly
# python HHWWggFinalFitScript.py --Step Signal --mode packageOnly --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec HHWWgg-SL-SM-NLO-Run2 --note SLNLOstatOnly
# python HHWWggFinalFitScript.py --Step Signal --mode sigPlotsOnly --physics SM --finalStates SL --years 2018 --dirTypes Signal --baseDirec HHWWgg-SL-SM-NLO-Run2 --note SLNLOstatOnly
#
# python HHWWggFinalFitScript.py --Step Background --mode fTestOnly --physics SM --finalStates SL --years 2016 --dirTypes Data --baseDirec HHWWgg-SL-SM-NLO-Run2 --note SLNLOstatOnly
# python HHWWggFinalFitScript.py --Step Background --mode bkgPlotsOnly --physics SM --finalStates SL --years 2016 --dirTypes Data --baseDirec HHWWgg-SL-SM-NLO-Run2 --note SLNLOstatOnly
#
# python HHWWggFinalFitScript.py --Step Datacard --mode datacard --physics SM --finalStates SL --years 2017 --note SLNLOstatOnly --dirTypes Datacard --baseDirec HHWWgg-SL-SM-NLO-Run2
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates SL --years 2017 --note SLNLOstatOnly --dirTypes Combine --combineInd
# 
#
# Example Usage:
# 
# Signal: (run twice)
# python HHWWggFinalFitScript.py --Step Signal --mode std --physics SM --finalStates SL --years 2016 --dirTypes Signal --note AllCats
# python HHWWggFinalFitScript.py --Step Signal --mode std --physics SM --finalStates SL --years 2016 --dirTypes Signal --note AllCats
# 
# Background:
# python HHWWggFinalFitScript.py --Step Background --mode fTestOnly --physics SM --finalStates SL --years 2016 --dirTypes Data --note AllCats 
# python HHWWggFinalFitScript.py --Step Background --mode bkgPlotsOnly --physics SM --finalStates SL --years 2016 --dirTypes Data --note AllCats
#
# Datacard:
# python HHWWggFinalFitScript.py --Step Datacard --mode datacard --physics SM --finalStates SL,FH,FL --years 2016,2017,2018 --note AllCats --dirTypes Datacard
# 
# Combine:
# ##--individuals
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates SL,FL,FH --years 2016,2017,2018 --note AllCats --dirTypes Combine --combineInd
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates FH,SL --years 2018 --note AllCats --dirTypes Combine --combineInd
#
# ##-- Run 2 
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates SL,FL,FH --years 2016,2017,2018 --note AllCats --dirTypes Combine --Run2
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates FH,SL --years 2016,2017,2018 --note AllCats --dirTypes Combine --Run2
# 
##-- Everything
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates SL,FL,FH --years 2016,2017,2018 --note AllCats --dirTypes Combine --combineAll
#
# Plot:
# python HHWWggFinalFitScript.py --Step Plot --physicsCases SM --finalStates SL --years all --note Plot --HH_limit
# python HHWWggFinalFitScript.py --Step Plot --mode Plot --physicsCases Plot --finalStates Plot --years Plot --note Plot
#
# 
# ##-- DNN 
# python HHWWggFinalFitScript.py --Step Signal --mode std --physics SM --finalStates SL --years 2017 --dirTypes Signal --note DNNaddWJets
# python HHWWggFinalFitScript.py --Step Signal --mode sigFitOnly --physics SM --finalStates SL --years 2017 --dirTypes Signal --note DNNaddWJets
# python HHWWggFinalFitScript.py --Step Signal --mode packageOnly --physics SM --finalStates SL --years 2017 --dirTypes Signal --note DNNaddWJets
# python HHWWggFinalFitScript.py --Step Signal --mode sigPlotsOnly --physics SM --finalStates SL --years 2017 --dirTypes Signal --note DNNaddWJets
#
# python HHWWggFinalFitScript.py --Step Background --mode fTestOnly --physics SM --finalStates SL --years 2017 --dirTypes Data --note DNNaddWJets 
# python HHWWggFinalFitScript.py --Step Background --mode bkgPlotsOnly --physics SM --finalStates SL --years 2017 --dirTypes Data --note DNNaddWJets 
# 
# python HHWWggFinalFitScript.py --Step Datacard --mode datacard --physics SM --finalStates SL --years 2017 --note DNNaddWJets --dirTypes Datacard
# python HHWWggFinalFitScript.py --Step Combine --mode combine --physics SM --finalStates SL --years 2017 --note DNNaddWJets --dirTypes Combine --combineInd
###################################################################################################

import os 
import argparse 
import subprocess
# import CMS_lumi, tdrstyle

from HHWWggFinalFitScript_Tools import * 

parser = argparse.ArgumentParser()

parser.add_argument("--Step",type=str, default="", help="Fggfinalfit step to run", required=False)
parser.add_argument("--mode",type=str, default="", help="Fggfinalfit mode to run", required=False)
parser.add_argument("--systematics", action="store_true", default=False, help="Include systematics", required=False)
parser.add_argument("--physicsCases",type=str, default="", help="Comma separated list of physics cases to run. Ex: SM", required=False)
parser.add_argument("--finalStates",type=str, default="", help="Comma separated list of physics cases to run. Ex: SL,FH,FL", required=False)
parser.add_argument("--years",type=str, default="", help="Comma separated list of years to run. Ex: 2016,2017,2018", required=False)
parser.add_argument("--dirTypes",type=str, default="", help="Comma separated list of dirTypes to run. Ex: Signal,Data", required=False)
parser.add_argument("--baseDirec",type=str, default="", help="Location of ntuples with proper subdirectoy structure.", required=False)
parser.add_argument("--note",type=str, default="HHWWggAnalysis", help="Note for ext variable", required=False)
parser.add_argument("--HH_limit", action="store_true", default=False, help="Plot HH limits", required=False)
parser.add_argument("--Run2", action="store_true", default=False, help="Compute combined Run 2 limits ", required=False)
parser.add_argument("--combineAll", action="store_true", default=False, help="Compute limits from all inputs combined", required=False)
parser.add_argument("--combineInd", action="store_true", default=False, help="Compute limits for individual cases", required=False)
parser.add_argument("--DNN", action="store_true", default=False, help="Use DNN cats", required=False)
parser.add_argument("--outputDirec",type=str,default="/eos/user/a/atishelm/www/HHWWgg/fggfinalfit/",help="output location for plots",required=False)

args = parser.parse_args()

# ntupleDirec = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/TaggerOutput/" # HHWWgg-SL-SM-NLO-Run2/"
ntupleDirec = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/WeightsExp/" 
# baseDirec = "HHWWgg_Combination"
# baseDirec = "HHWWgg_DNNResult"
# baseDirec = "HHWWgg_DNNResultAddWJets"
baseDirec = args.baseDirec
# outputDirec = "/eos/user/a/atishelm/www/HHWWgg/DNN_Results"
# outputDirec = "/eos/user/a/atishelm/www/HHWWgg/DNN_Result_AddWJets"
# outputDirec = "/eos/user/a/atishelm/www/HHWWgg/DNN_Result_AddWJets"
# outputDirec = "/afs/cern.ch/work/a/atishelm/private/HHWWgg-AN-WorkingDirectory/AN-20-165/Images/"
outputDirec = args.outputDirec
# outputDirec = "/eos/user/a/atishelm/www/HHWWgg/SM-NLO-Results/"

# outputDirec2 = "/afs/cern.ch/work/a/atishelm/private/HHWWgg-AN-WorkingDirectory/AN-20-165/Images/"

note = args.note 
mode = args.mode 
systematics = int(args.systematics)

##-- Get Loop params 
loopParams = ["physicsCases","finalStates","years","dirTypes"]
for loopParam in loopParams:
  exec("%s = args.%s.split(',')"%(loopParam,loopParam))
  exec("print'%s:',%s"%(loopParam,loopParam))

##-- Setup For Combine Step
if(args.Step=="Combine"): 
  # For each case X finalState X year, setup datacard, signal and background model locations
  os.system('mkdir -p Combine2/%s'%(args.note))
  os.system('mkdir -p Combine2/%s/Models'%(args.note))

##-- Run steps for each case 
if(args.Step!="Plot"):
  for physicsCase in physicsCases:
    for finalState in finalStates:
      for year in years:
        direc = "%s/%s/%s/%s"%(baseDirec,physicsCase,finalState,year)
        for dirType in dirTypes: 
          FitDir = GetFitDirec(dirType)
          if(args.Step=="Datacard"): 
            fullDirec = "%s_Signal"%(direc)
            inputWSDir = "%s/%s_Signal"%(ntupleDirec,direc)
          else: 
            fullDirec = "%s_%s"%(direc,dirType)
            inputWSDir = "%s/%s_%s"%(ntupleDirec,direc,dirType)

          if(args.Step=="Combine"): 
            # print"physics Case: ",physicsCase
            # print"finalState: ",finalState
            # print"year: ",year 
            # print"note: ",note 
            # For each case X finalState X year, setup datacard, signal and background model locations
            ext = "HHWWgg_%s-%s_%s_%s"%(physicsCase,finalState,year,note)
            FinalStateParticles = GetFinalStateParticles(finalState)
            # print"FinalStateParticles:",FinalStateParticles
            # os.chdir('Combine')
            os.chdir('Combine2')

            ##-- Copy models from this fggfinalfit repo 
            os.system('mkdir -p Models/%s'%(ext))
            os.system('cp ../Signal/outdir_%s_nodeSM_HHWWgg_%s/CMS-HGG_mva_13TeV_sigfit.root ./Models/%s/CMS-HGG_mva_13TeV_sigfit.root'%(ext,FinalStateParticles,ext))
            os.system('cp ../Background/CMS-HGG_multipdf_%s.root ./Models/%s/CMS-HGG_mva_13TeV_multipdf.root'%(ext,ext))
            os.system('cp ../Datacard/%s_%s_datacards/Datacard_13TeV_%s_nodeSM_HHWWgg_%s_cleaned.txt CMS-HGG_mva_13TeV_datacard_%s.txt'%(ext,args.note,ext,FinalStateParticles,ext))
            
            ##-- Add branching ratios to data card in form of rateParam
            SL_BR = GetBR("SL")
            FH_BR = GetBR("FH")
            FL_BR = GetBR("FL")

            datacardName = "CMS-HGG_mva_13TeV_datacard_%s.txt"%(ext)
            print "Creating datacard: ",datacardName
            datacard = open(datacardName,'a')
            datacard.write('\n')
            if(finalState == "SL"):       
              datacard.write("br_WW_qqlnu rateParam HHWWggTag_0_%s GluGluToHHTo %s\n"%(year,SL_BR))
              datacard.write("br_WW_qqlnu rateParam HHWWggTag_1_%s GluGluToHHTo %s\n"%(year,SL_BR))
              datacard.write("xs_HH rateParam HHWWggTag_0_%s GluGluToHHTo 31.049\n"%(year))
              datacard.write("xs_HH rateParam HHWWggTag_1_%s GluGluToHHTo 31.049\n"%(year))
              datacard.write("br_HH_WWgg rateParam HHWWggTag_0_%s GluGluToHHTo 0.000970198\n"%(year))
              datacard.write("br_HH_WWgg rateParam HHWWggTag_1_%s GluGluToHHTo 0.000970198\n"%(year))
               
              if(args.DNN):
                datacard.write("br_WW_qqlnu rateParam HHWWggTag_2_%s GluGluToHHTo %s\n"%(year,SL_BR))
                datacard.write("br_WW_qqlnu rateParam HHWWggTag_3_%s GluGluToHHTo %s\n"%(year,SL_BR))
                datacard.write("xs_HH rateParam HHWWggTag_2_%s GluGluToHHTo 31.049\n"%(year))
                datacard.write("xs_HH rateParam HHWWggTag_3_%s GluGluToHHTo 31.049\n"%(year))    
                datacard.write("br_HH_WWgg rateParam HHWWggTag_2_%s GluGluToHHTo 0.000970198\n"%(year))
                datacard.write("br_HH_WWgg rateParam HHWWggTag_3_%s GluGluToHHTo 0.000970198\n"%(year))                            

              # datacard.write("br_WW_qqlnu rateParam HHWWggTag_2_%s GluGluToHHTo %s\n"%(year,SL_BR)) # DNN only..3 cats (not always...)
              datacard.write("nuisance edit freeze br_WW_qqlnu\n")
              datacard.write("nuisance edit freeze xs_HH\n")
              datacard.write("nuisance edit freeze br_HH_WWgg\n")
            elif(finalState == "FL"):
              datacard.write("br_WW_lnulnu rateParam HHWWggTag_3_%s GluGluToHHTo %s\n"%(year,FL_BR))
              datacard.write("nuisance edit freeze br_WW_lnulnu\n")            
            elif(finalState == "FH"):
              datacard.write("br_WW_qqqq rateParam HHWWggTag_2_%s GluGluToHHTo %s\n"%(year,FH_BR))
              datacard.write("nuisance edit freeze br_WW_qqqq\n")                  
            else: 
              print "Final state is not SL FL or FH. It's: %s"%(finalState)
              os.chdir('..')
              exit(1)
            
            os.chdir('..')

          else: 
            script = open('%s_Config_TEMPLATE.txt'%(FitDir)).read()
            cats = FinalStateCats(finalState,args.DNN)
            ext = "HHWWgg_%s-%s_%s_%s"%(physicsCase,finalState,year,note)
            configParams = GetConfigParams(dirType)
            FinalStateParticles = GetFinalStateParticles(finalState)

            if(dirType=="Signal" or dirType=="Datacard"):
              analysis_type = GetAnalysisType(physicsCase) ##-- get analysis type from physics case 
              usrprocs = GetUsrProcs(physicsCase)

            for param in configParams:
              systematics = str(systematics)
              if(param=='systematics'): exec("script = script.replace('{systematics}',systematics)")
              exec("script = script.replace('{%s}',%s)"%(param,param))
              
            scriptName = "%s_Config.py"%(ext)

            with open(scriptName, "w") as outScript:
              outScript.write(script)
            
            if(args.Step=="Datacard"):
              os.system('mv %s Configs'%(scriptName))
              os.system('python RunCombineScripts.py --inputConfig Configs/%s'%(scriptName))
            else: 
              os.system('mv %s %s/Configs'%(scriptName,FitDir))
              os.chdir('%s'%(FitDir))          
              os.system('python Run%sScripts.py --inputConfig Configs/%s'%(FitDir,scriptName))

            if(args.Step != "Datacard"):
              # outDirec = '%s/%s/%s'%(outputDirec,ext,mode)
              # outDirec = '%s/AnalyticFitting/%s/%s/%s/'%(outputDirec,physicsCase,finalState,year)
              outDirec = '%s/%s/%s/%s/'%(outputDirec,physicsCase,finalState,year)
              print "Outputting plots to: %s"%(outDirec)
              os.system('mkdir -p %s'%(outDirec))
              os.system('cp %s/index.php %s/%s'%(outputDirec,outputDirec,physicsCase))
              os.system('cp %s/index.php %s/%s/%s'%(outputDirec,outputDirec,physicsCase,finalState))
              os.system('cp %s/index.php %s/%s/%s/%s'%(outputDirec,outputDirec,physicsCase,finalState,year))
              # os.system('cp %s/index.php %s/%s '%(outputDirec,outputDirec,ext))
              # os.system('cp %s/index.php %s'%(outputDirec,outDirec))          
              plotDirs = GetPlotDir(mode)
              for plotDir in plotDirs: 
                if(dirType=="Signal"):
                  os.system('cp outdir_%s_nodeSM_HHWWgg_%s/%s/*.png %s'%(ext,FinalStateParticles,plotDir,outDirec))
                  os.system('cp outdir_%s_nodeSM_HHWWgg_%s/%s/*.pdf %s'%(ext,FinalStateParticles,plotDir,outDirec))
                else: 
                  os.system('cp outdir_%s/%s/*.png %s'%(ext,plotDir,outDirec))
                  os.system('cp outdir_%s/%s/*.pdf %s'%(ext,plotDir,outDirec))  
              if(dirType=="Signal"):
                sigExt = "%s_nodeSM_HHWWgg_%s"%(ext,FinalStateParticles)
                for cat in cats.split(','):
                # copy outfiles so they can be picked up by background plots 
                  sigExtwTag = "%s_%s"%(sigExt,cat)
                  os.system('cp outdir_%s/CMS-HGG_sigfit_%s.root outdir_%s/CMS-HGG_sigfit_%s.root'%(sigExt,sigExt,sigExt,sigExtwTag))
              if(FitDir!="Combine"): os.chdir('..')

if(args.Step=="Combine"): 
  # run all possible combine combinations 
  # Columns: year --> Run 2 
  # Rows: SL, FH, FL --> Combine 
  # os.chdir('Combine')
  os.chdir('Combine2')
  command = "combineCards.py "
  datacards = []
  
  ##-- Individual limits 
  if(args.combineInd):
    for physicsCase in physicsCases:
      for ifs,finalState in enumerate(finalStates):
        for iy,year in enumerate(years):
          if(iy==len(years)-1 and ifs == len(finalStates)-1): 
            print "Skipping:"
            print year 
            print finalState
            continue 
          # print"combine final state:",finalState
          # print"combine year:",year
          ext = "HHWWgg_%s-%s_%s_%s"%(physicsCase,finalState,year,note)
          dCardName = "CMS-HGG_mva_13TeV_datacard_%s"%(ext)
          dCardtxt = "%s.txt"%(dCardName)
          dCardWorkspace = "%s.root"%(dCardName)
          datacards.append(dCardtxt)
          print "Computing limits for %s ..."%(ext)

          ##-- With datacard.txt 
          # combineCommand = 'combine %s -m 125 -M AsymptoticLimits --run=blind'%(dCardtxt)
          # os.system(combineCommand)
          # os.system('mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/%s_limits.root'%(ext))

          ##-- With text2workspace

          # print "Using datacard: %s"%(dCardWorkspace)
          os.system('text2workspace.py %s'%(dCardtxt))
          os.system('combine -M AsymptoticLimits -m 125 --freezeParameters allConstrainedNuisances --expectSignal 1 --cminDefaultMinimizerStrategy 0 -d %s --run blind -t -1'%(dCardWorkspace))
          os.system('mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/%s_limits.root'%(ext))
          # os.system('combine %s -m 125 -M AsymptoticLimits --run=blind'%(dCardWorkspace))


          # combineCommands.append(combineCommand)
          # print "combine Command: ",combineCommand


          # os.system('rm higgsCombineTest.AsymptoticLimits.mH125.root')
          # subprocess.call(combineCommand, shell=True)


  # for com in combineCommands:
    # os.chdir('..')
    # os.chdir('Combine')
    # os.system(com)

  if(args.Run2):
    ##-- Run 2 Limits 
    for physicsCase in physicsCases:
      for ifs,finalState in enumerate(finalStates):
        run2_datacards = []

        for year in years:
          # run2_datacards = []
          ext = "HHWWgg_%s-%s_%s_%s"%(physicsCase,finalState,year,note)
          dCardName = "CMS-HGG_mva_13TeV_datacard_%s"%(ext)
          # dCard = "CMS-HGG_mva_13TeV_datacard_%s.txt"%(ext)
          dCardtxt = "%s.txt"%(dCardName)
          dCardWorkspace = "%s.root"%(dCardName)
          run2_datacards.append(dCardtxt)

        if(ifs==len(finalStates)-1): 
          print "Skipping"
          print finalState
          continue 
        print "Computing Full Run 2 limits for final state: %s"%(finalState)

        run2_ext = "HHWWgg_%s-%s_%s_%s"%(physicsCase,finalState,"Run2",note)
        run2_command = "combineCards.py "
        for run2_datacard in run2_datacards: run2_command += ' %s '%(run2_datacard)
        run2_datacardName_txt = "run2_datacard_%s.txt"%(finalState)
        run2_datacardName_root = "run2_datacard_%s.root"%(finalState)
        run2_command += " >> %s "%(run2_datacardName_txt)
        print"run2 combine command: ",run2_command
        os.system('rm %s'%(run2_datacardName_txt))
        os.system('rm %s'%(run2_datacardName_root))
        os.system(run2_command)
        os.system('text2workspace.py %s'%(run2_datacardName_txt))
        
        ##-- With text2workspace 
        # need to use freezeparameters method to BR's can't change
        os.system('combine -M AsymptoticLimits -m 125 --freezeParameters allConstrainedNuisances --expectSignal 1 --cminDefaultMinimizerStrategy 0 -d %s --run blind -t -1'%(run2_datacardName_root))
        os.system('mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/%s_limits.root'%(run2_ext))
        
        ##-- not sure - previous strategy:
        # os.system('combine %s -m 125 -M AsymptoticLimits --run=blind'%(run2_datacardName_root))
        # os.system('mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/%s_limits.root'%(run2_ext))

          # print "Computing limits for %s ..."%(ext)
          # os.system('text2workspace.py %s'%(dCardtxt))
          # os.system('combine -M AsymptoticLimits -m 125 --freezeParameters allConstrainedNuisances --expectSignal 1 --cminDefaultMinimizerStrategy 0 -d %s --run blind -t -1'%(dCardWorkspace))
          # os.system('combine %s -m 125 -M AsymptoticLimits --run=blind'%(dCard))
          # os.system('mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/%s_limits.root'%(ext))

  # ##-- Channel Combined Limits 
  # for physicsCase in physicsCases:
  #   for finalState in finalStates:
  #     for year in years:
  #       ext = "HHWWgg_%s-%s_%s_%s"%(physicsCase,finalState,year,note)
  #       dCardName = "CMS-HGG_mva_13TeV_datacard_%s"%(ext)
  #       # dCard = "CMS-HGG_mva_13TeV_datacard_%s.txt"%(ext)
  #       dCardtxt = "%s.txt"%(dCardName)
  #       dCardWorkspace = "%s.root"%(dCardName)
  #       print "Computing limits for %s ..."%(ext)
  #       os.system('text2workspace.py %s'%(dCardtxt))
  #       os.system('combine -M AsymptoticLimits -m 125 --freezeParameters allConstrainedNuisances --expectSignal 1 --cminDefaultMinimizerStrategy 0 -d %s --run blind -t -1'%(dCardWorkspace))
  #       # os.system('combine %s -m 125 -M AsymptoticLimits --run=blind'%(dCard))
  #       os.system('mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/%s_limits.root'%(ext))

  if(args.combineAll):
    datacards = [] 
    for finalState in finalStates:
      for year in years:   
        ext = "HHWWgg_%s-%s_%s_%s"%(physicsCase,finalState,year,note)
        dCardName = "CMS-HGG_mva_13TeV_datacard_%s"%(ext)
        dCardtxt = "%s.txt"%(dCardName)        
        datacards.append(dCardtxt)
    for datacard in datacards: command += " %s "%(datacard)
    command += " >> Datacard_Combined.txt "

    print "For full combination, run these commands:"
    print "1) cd Combine"
    print "2)",command 
    print "3) text2workspace.py Datacard_Combined.txt"
    # print "4) combine Datacard_Combined.txt -m 125 -M AsymptoticLimits --run=blind"
    print "4) combine -M AsymptoticLimits -m 125 --freezeParameters allConstrainedNuisances --expectSignal 1 --cminDefaultMinimizerStrategy 0 -d Datacard_Combined.root --run blind -t -1"
    print "5) mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/HHWWgg_SM-All_Run2_AllCats_limits.root"
    # print "Command: ",command
    # print "Computing combined limit..."
    # print "Command: ",command
    # # os.chdir('Combine')

    # os.system('rm Datacard_Combined.txt')
    # os.system('rm higgsCombineTest.AsymptoticLimits.mH125.root')

    # os.system(command)
    # os.system('text2workspace.py Datacard_Combined.txt')
    # os.system('combine -M AsymptoticLimits -m 125 --freezeParameters allConstrainedNuisances --expectSignal 1 --cminDefaultMinimizerStrategy 0 -d Datacard_Combined.root --run blind -t -1')
    # os.system('combine Datacard_Combined.txt -m 125 -M AsymptoticLimits --run=blind')
    
  # https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit/issues/543  ##-- Object is duplicated info -- should be ok 

    # os.system('combine Datacard_Combined.txt -m 125 -M AsymptoticLimits --run=blind')
    # # os.system('combine DataCard_Combined.txt -m 125 -M AsymptoticLimits --run=blind')
    # os.system('combine -M AsymptoticLimits -m 125 --freezeParameters allConstrainedNuisances --expectSignal 1 --cminDefaultMinimizerStrategy 0 -d DataCard_Combined.txt --run blind -t -1')
    # # os.system('mv higgsCombineTest.AsymptoticLimits.mH125.root Limits/limits.root')

  # os.chdir('..')

if(args.Step=="Plot"): 
  # os.chdir('Combine')
  os.chdir('Combine2')
  print "Creating limit table ..."
  CreateLimitTable(args.HH_limit)
  PlotLimitBands(0)
  PlotLimitBands(1)
  os.chdir('..')