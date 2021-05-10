#!/usr/bin/env python3

import ROOT
import numpy as np
import pandas as pd

fileOfFiles = 'data/dataFileList.dat'

with open(fileOfFiles) as f:
	files = f.readlines()
# Remove whitespace characters like `\n` at the end of each line
files = [x.strip() for x in files]

## Assumed here that muminus_0 is mum and muminus is mup. Otherwise the order is kept, so it makes sense.
## For the moment I have ignored PIDsubs. Lambda0 seems to be replaced by KS0->pim pip?
wantedBranches_OriginalNames = [
	'Lb_ENDVERTEX_X',
	'Lb_ENDVERTEX_Y',
	'Lb_ENDVERTEX_Z',
	'L_ENDVERTEX_X',
	'L_ENDVERTEX_Y',
	'L_ENDVERTEX_Z',
	'Jpsi_ENDVERTEX_X',
	'Jpsi_ENDVERTEX_Y',
	'Jpsi_ENDVERTEX_Z',
	'L_PX',
	'L_PY',
	'L_PZ',
	'Lb_PX',
	'Lb_PY',
	'Lb_PZ',
	'Jpsi_PX',
	'Jpsi_PY',
	'Jpsi_PZ',
	'p_PX',
	'p_PY',
	'p_PZ',
	'pim_PX',
	'pim_PY',
	'pim_PZ',
	'mum_PX',
	'mum_PY',
	'mum_PZ',
	'mup_PX',
	'mup_PY',
	'mup_PZ',
	'L_M',
	'L_MM',
	'Lb_M',
	'Lb_MM',
	'Jpsi_M',
	'Jpsi_MM',
	'Lb_BPVDIRA',
	'Lb_BPVIPCHI2',
	'Lb_BPVVDCHI2',
	'Lb_VFASPF_CHI2_VDOF',
	'L_BPVDIRA',
	'L_BPVIPCHI2',
	'L_BPVVDCHI2',
	'L_VFASPF_CHI2_VDOF',
	'Lb_OWNPV_X',
	'Lb_OWNPV_Y',
	'Lb_OWNPV_Z',
	'Lb_OWNPV_CHI2',
	'Lb_OWNPV_NDOF',
	'Lb_DTF_FixJPsi_status',
	'Lb_DTF_FixJPsi_M',
	'Lb_DTF_FixJPsi_P',
	'Lb_DTF_FixJPsi_chi2',
	'Lb_DTF_FixJPsi_nDOF',
	'Lb_DTF_FixJPsi_PV_key',
	'Lb_DTF_FixJPsi_PV_X',
	'Lb_DTF_FixJPsi_PV_Y',
	'Lb_DTF_FixJPsi_PV_Z',
	'Lb_DTF_FixJPsi_Lambda0_M',
	'Lb_DTF_FixJPsi_Lambda0_P',
	'Lb_DTF_FixJPsi_Lambda0_decayLength',
	'Lb_DTF_FixJPsi_Lambda0_piplus_PX',
	'Lb_DTF_FixJPsi_Lambda0_piplus_PY',
	'Lb_DTF_FixJPsi_Lambda0_piplus_PZ',
	'Lb_DTF_FixJPsi_Lambda0_pplus_PX',
	'Lb_DTF_FixJPsi_Lambda0_pplus_PY',
	'Lb_DTF_FixJPsi_Lambda0_pplus_PZ',
	'Lb_DTF_FixJPsi_J_psi_1S_muminus_0_PX',
	'Lb_DTF_FixJPsi_J_psi_1S_muminus_0_PY',
	'Lb_DTF_FixJPsi_J_psi_1S_muminus_0_PZ',
	'Lb_DTF_FixJPsi_J_psi_1S_muminus_PX',
	'Lb_DTF_FixJPsi_J_psi_1S_muminus_PY',
	'Lb_DTF_FixJPsi_J_psi_1S_muminus_PZ',
	'Lb_DTF_FixJPsiLambda_status',
	'Lb_DTF_FixJPsiLambda_M',
	'Lb_DTF_FixJPsiLambda_P',
	'Lb_DTF_FixJPsiLambda_chi2',
	'Lb_DTF_FixJPsiLambda_nDOF',
	'Lb_DTF_FixJPsiLambda_PV_key',
	'Lb_DTF_FixJPsiLambda_PV_X',
	'Lb_DTF_FixJPsiLambda_PV_Y',
	'Lb_DTF_FixJPsiLambda_PV_Z',
	'Lb_DTF_FixJPsiLambda_Lambda0_M',
	'Lb_DTF_FixJPsiLambda_Lambda0_P',
	'Lb_DTF_FixJPsiLambda_Lambda0_decayLength',
	'Lb_DTF_FixJPsiLambda_Lambda0_piplus_PX',
	'Lb_DTF_FixJPsiLambda_Lambda0_piplus_PY',
	'Lb_DTF_FixJPsiLambda_Lambda0_piplus_PZ',
	'Lb_DTF_FixJPsiLambda_Lambda0_pplus_PX',
	'Lb_DTF_FixJPsiLambda_Lambda0_pplus_PY',
	'Lb_DTF_FixJPsiLambda_Lambda0_pplus_PZ',
	'Lb_DTF_FixJPsiLambda_J_psi_1S_muminus_0_PX',
	'Lb_DTF_FixJPsiLambda_J_psi_1S_muminus_0_PY',
	'Lb_DTF_FixJPsiLambda_J_psi_1S_muminus_0_PZ',
	'Lb_DTF_FixJPsiLambda_J_psi_1S_muminus_PX',
	'Lb_DTF_FixJPsiLambda_J_psi_1S_muminus_PY',
	'Lb_DTF_FixJPsiLambda_J_psi_1S_muminus_PZ',
	'Lb_DTF_FixJPsi_PIDSubs_status',
	'Lb_DTF_FixJPsi_PIDSubs_M',
	'Lb_DTF_FixJPsi_PIDSubs_P',
	'Lb_DTF_FixJPsi_PIDSubs_chi2',
	'Lb_DTF_FixJPsi_PIDSubs_nDOF',
	'Lb_DTF_FixJPsi_PIDSubs_PV_key',
	'Lb_DTF_FixJPsi_PIDSubs_PV_X',
	'Lb_DTF_FixJPsi_PIDSubs_PV_Y',
	'Lb_DTF_FixJPsi_PIDSubs_PV_Z',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_M',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_P',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_decayLength',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_piplus_PX',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_piplus_PY',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_piplus_PZ',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_pplus_PX',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_pplus_PY',
#    'Lb_DTF_FixJPsi_PIDSubs_Lambda0_pplus_PZ',
	'Lb_DTF_FixJPsi_PIDSubs_J_psi_1S_muminus_0_PX',
	'Lb_DTF_FixJPsi_PIDSubs_J_psi_1S_muminus_0_PY',
	'Lb_DTF_FixJPsi_PIDSubs_J_psi_1S_muminus_0_PZ',
	'Lb_DTF_FixJPsi_PIDSubs_J_psi_1S_muminus_PX',
	'Lb_DTF_FixJPsi_PIDSubs_J_psi_1S_muminus_PY',
	'Lb_DTF_FixJPsi_PIDSubs_J_psi_1S_muminus_PZ',
	'Lb_DTF_FixJPsiLambda_PIDSubs_status',
	'Lb_DTF_FixJPsiLambda_PIDSubs_M',
	'Lb_DTF_FixJPsiLambda_PIDSubs_P',
	'Lb_DTF_FixJPsiLambda_PIDSubs_chi2',
	'Lb_DTF_FixJPsiLambda_PIDSubs_nDOF',
	'Lb_DTF_FixJPsiLambda_PIDSubs_PV_key',
	'Lb_DTF_FixJPsiLambda_PIDSubs_PV_X',
	'Lb_DTF_FixJPsiLambda_PIDSubs_PV_Y',
	'Lb_DTF_FixJPsiLambda_PIDSubs_PV_Z',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_M',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_P',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_decayLength',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_piplus_PX',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_piplus_PY',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_piplus_PZ',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_pplus_PX',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_pplus_PY',
#    'Lb_DTF_FixJPsiLambda_PIDSubs_Lambda0_pplus_PZ',
	'Lb_DTF_FixJPsiLambda_PIDSubs_J_psi_1S_muminus_0_PX',
	'Lb_DTF_FixJPsiLambda_PIDSubs_J_psi_1S_muminus_0_PY',
	'Lb_DTF_FixJPsiLambda_PIDSubs_J_psi_1S_muminus_0_PZ',
	'Lb_DTF_FixJPsiLambda_PIDSubs_J_psi_1S_muminus_PX',
	'Lb_DTF_FixJPsiLambda_PIDSubs_J_psi_1S_muminus_PY',
	'Lb_DTF_FixJPsiLambda_PIDSubs_J_psi_1S_muminus_PZ',
#    'TrackType'
]

wantedBranches = [
	'Lb_ENDVERTEX_X',
	'Lb_ENDVERTEX_Y',
	'Lb_ENDVERTEX_Z',
	'L_ENDVERTEX_X',
	'L_ENDVERTEX_Y',
	'L_ENDVERTEX_Z',
	'Jpsi_ENDVERTEX_X',
	'Jpsi_ENDVERTEX_Y',
	'Jpsi_ENDVERTEX_Z',
	'L_PX',
	'L_PY',
	'L_PZ',
	'Lb_PX',
	'Lb_PY',
	'Lb_PZ',
	'Jpsi_PX',
	'Jpsi_PY',
	'Jpsi_PZ',
	'p_PX',
	'p_PY',
	'p_PZ',
	'pim_PX',
	'pim_PY',
	'pim_PZ',
	'mum_PX',
	'mum_PY',
	'mum_PZ',
	'mup_PX',
	'mup_PY',
	'mup_PZ',
	'L_M',
	'L_MM',
	'Lb_M',
	'Lb_MM',
	'Jpsi_M',
	'Jpsi_MM',
	'Lb_BPVDIRA',
	'Lb_BPVIPCHI2',
	'Lb_BPVVDCHI2',
	'Lb_VFASPF_CHI2_VDOF',
	'L_BPVDIRA',
	'L_BPVIPCHI2',
	'L_BPVVDCHI2',
	'L_VFASPF_CHI2_VDOF',
	'Lb_OWNPV_X',
	'Lb_OWNPV_Y',
	'Lb_OWNPV_Z',
	'Lb_OWNPV_CHI2',
	'Lb_OWNPV_NDOF',
	'DTF_FixJPsi_status',
	'DTF_FixJPsi_Lb_M',
	'DTF_FixJPsi_Lb_P',
	'DTF_FixJPsi_chi2',
	'DTF_FixJPsi_nDOF',
	'DTF_FixJPsi_PV_key',
	'DTF_FixJPsi_PV_X',
	'DTF_FixJPsi_PV_Y',
	'DTF_FixJPsi_PV_Z',
	'DTF_FixJPsi_L_M',
	'DTF_FixJPsi_L_P',
	'DTF_FixJPsi_L_decayLength',
	'DTF_FixJPsi_pim_PX',
	'DTF_FixJPsi_pim_PY',
	'DTF_FixJPsi_pim_PZ',
	'DTF_FixJPsi_p_PX',
	'DTF_FixJPsi_p_PY',
	'DTF_FixJPsi_p_PZ',
	'DTF_FixJPsi_mum_PX',
	'DTF_FixJPsi_mum_PY',
	'DTF_FixJPsi_mum_PZ',
	'DTF_FixJPsi_mup_PX',
	'DTF_FixJPsi_mup_PY',
	'DTF_FixJPsi_mup_PZ',
	'DTF_FixJPsiLambda_status',
	'DTF_FixJPsiLambda_Lb_M',
	'DTF_FixJPsiLambda_Lb_P',
	'DTF_FixJPsiLambda_chi2',
	'DTF_FixJPsiLambda_nDOF',
	'DTF_FixJPsiLambda_PV_key',
	'DTF_FixJPsiLambda_PV_X',
	'DTF_FixJPsiLambda_PV_Y',
	'DTF_FixJPsiLambda_PV_Z',
	'DTF_FixJPsiLambda_L_M',
	'DTF_FixJPsiLambda_L_P',
	'DTF_FixJPsiLambda_L_decayLength',
	'DTF_FixJPsiLambda_pim_PX',
	'DTF_FixJPsiLambda_pim_PY',
	'DTF_FixJPsiLambda_pim_PZ',
	'DTF_FixJPsiLambda_p_PX',
	'DTF_FixJPsiLambda_p_PY',
	'DTF_FixJPsiLambda_p_PZ',
	'DTF_FixJPsiLambda_mum_PX',
	'DTF_FixJPsiLambda_mum_PY',
	'DTF_FixJPsiLambda_mum_PZ',
	'DTF_FixJPsiLambda_mup_PX',
	'DTF_FixJPsiLambda_mup_PY',
	'DTF_FixJPsiLambda_mup_PZ',
	'DTF_FixJPsi_PIDSubs_status',
	'DTF_FixJPsi_PIDSubs_Lb_M',
	'DTF_FixJPsi_PIDSubs_Lb_P',
	'DTF_FixJPsi_PIDSubs_chi2',
	'DTF_FixJPsi_PIDSubs_nDOF',
	'DTF_FixJPsi_PIDSubs_PV_key',
	'DTF_FixJPsi_PIDSubs_PV_X',
	'DTF_FixJPsi_PIDSubs_PV_Y',
	'DTF_FixJPsi_PIDSubs_PV_Z',
#    'DTF_FixJPsi_PIDSubs_L_M',
#    'DTF_FixJPsi_PIDSubs_L_P',
#    'DTF_FixJPsi_PIDSubs_L_decayLength',
#    'DTF_FixJPsi_PIDSubs_pim_PX',
#    'DTF_FixJPsi_PIDSubs_pim_PY',
#    'DTF_FixJPsi_PIDSubs_pim_PZ',
#    'DTF_FixJPsi_PIDSubs_p_PX',
#    'DTF_FixJPsi_PIDSubs_p_PY',
#    'DTF_FixJPsi_PIDSubs_p_PZ',
	'DTF_FixJPsi_PIDSubs_mum_PX',
	'DTF_FixJPsi_PIDSubs_mum_PY',
	'DTF_FixJPsi_PIDSubs_mum_PZ',
	'DTF_FixJPsi_PIDSubs_mup_PX',
	'DTF_FixJPsi_PIDSubs_mup_PY',
	'DTF_FixJPsi_PIDSubs_mup_PZ',
	'DTF_FixJPsiLambda_PIDSubs_status',
	'DTF_FixJPsiLambda_PIDSubs_Lb_M',
	'DTF_FixJPsiLambda_PIDSubs_Lb_P',
	'DTF_FixJPsiLambda_PIDSubs_chi2',
	'DTF_FixJPsiLambda_PIDSubs_nDOF',
	'DTF_FixJPsiLambda_PIDSubs_PV_key',
	'DTF_FixJPsiLambda_PIDSubs_PV_X',
	'DTF_FixJPsiLambda_PIDSubs_PV_Y',
	'DTF_FixJPsiLambda_PIDSubs_PV_Z',
#    'DTF_FixJPsiLambda_PIDSubs_L_M',
#    'DTF_FixJPsiLambda_PIDSubs_L_P',
#    'DTF_FixJPsiLambda_PIDSubs_L_decayLength',
#    'DTF_FixJPsiLambda_PIDSubs_pim_PX',
#    'DTF_FixJPsiLambda_PIDSubs_pim_PY',
#    'DTF_FixJPsiLambda_PIDSubs_pim_PZ',
#    'DTF_FixJPsiLambda_PIDSubs_p_PX',
#    'DTF_FixJPsiLambda_PIDSubs_p_PY',
#    'DTF_FixJPsiLambda_PIDSubs_p_PZ',
	'DTF_FixJPsiLambda_PIDSubs_mum_PX',
	'DTF_FixJPsiLambda_PIDSubs_mum_PY',
	'DTF_FixJPsiLambda_PIDSubs_mum_PZ',
	'DTF_FixJPsiLambda_PIDSubs_mup_PX',
	'DTF_FixJPsiLambda_PIDSubs_mup_PY',
	'DTF_FixJPsiLambda_PIDSubs_mup_PZ'
#    'TrackType'
]

totalNumberOfEntries = 0
entriesCap = 3e5 # How many entries do we want (roughly)?
currentFileIndex = 0
#completeDF = pd.DataFrame(columns=wantedBranches)

## Let's try a faster way
dictionaryList = []

## Build the data frame
while totalNumberOfEntries < entriesCap:
	print("Processing file", currentFileIndex, "...")
	inputData = ROOT.TFile.Open(files[currentFileIndex], "READ")
	## Get the n-tuples
	dataTree = inputData.Get("Lb_T/DecayTree")
    
	## Cycle through all events
	for entryNumber in range(0,dataTree.GetEntries()):       
		## Timid progress check
		if totalNumberOfEntries % 1000 == 0:
			print("Processing entry", totalNumberOfEntries, "...")
        
		## For each entry, store wanted branches
		dataTree.GetEntry(entryNumber)
		dictionaryOfBranchValues = {}
		for branchIndex in range(len(wantedBranches_OriginalNames)):
			wantedBranch = wantedBranches[branchIndex]
			wantedBranch_Original = wantedBranches_OriginalNames[branchIndex]
			currentValue = getattr(dataTree, wantedBranch_Original)
            
			## Pick first value if there's more than one
			## There has to be a better way to do this check, but this works
			if str(type(currentValue)) == "<class 'cppyy.LowLevelView'>":
				if len(currentValue) == 0:
					dictionaryOfBranchValues[wantedBranch] = np.nan
				else:
					dictionaryOfBranchValues[wantedBranch] = currentValue[0]
			else:
				dictionaryOfBranchValues[wantedBranch] = currentValue

		## Fill the DF row by row
		#completeDF.loc[totalNumberOfEntries] = dictionaryOfBranchValues
		dictionaryList.append(dictionaryOfBranchValues)
		totalNumberOfEntries += 1
    
	currentFileIndex += 1

completeDF = pd.DataFrame.from_dict(dictionaryList)
h5File = "data/Cusom_LHCbData_2016_MagUpDown_Dimuon_Ttracks.h5";
completeDF.to_hdf(h5File, "LHCbData");
