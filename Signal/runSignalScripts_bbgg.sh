mode="fTest"
#mode="signalFit"

YEAR="2016"
#YEAR="2017"
#YEAR="2018"

##python RunSignalScripts.py --inputConfig configs/config_test_${YEAR}.py --mode ${mode} --printOnly
##python RunSignalScripts.py --inputConfig configs/config_HHbbggSignal_${YEAR}.py --mode ${mode} --printOnly
python RunSignalScripts.py --inputConfig configs/config_HHbbggSignal_${YEAR}.py --mode ${mode} --modeOpts "--doPlots"
