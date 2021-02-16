# m8070PresetDecoder
This python file was compiled under python3.8 using imported lxml 4.62
It is used to decode the xml file of the Instrument settings (InstrumentState.xml) and show them in human readable format. From there you can copy and paste into excel and convert text to table  or do what you like.
It also shows what modules were present when the preset was created.

product is m8070b search for this at keysight.com
m8070b is a BERT for high speed digital testing.

I have also precompiled a windows runnable version using cx_freeze  so if you would like to just run it, grab the zip file and unzip the whole ting to a directory and run the exe from there. Was tested under Windoiws 10.
Microsoft Windows 10 Enterprise
Version	10.0.18363 Build 18363


-Tim Fairfield Feb 10, 2021 Keysight Applications Engineer Toronto canada.


the usages is now using command line arguments
like this:
D:\inout\m8070instrumentsettingsv1.2>instrumentsettingsmain.exe -h
usage: instrumentsettingsmain.exe [-h] [-mn] [-mo] location

 

Decode Keysight M8070 Setup files. This utility parses the xml setup into comma separated data. use --help for help

 

positional arguments:
  location              paste path to M8070 InstrumentState.xml file (for example C:\Users\fairfiel.KEYSIGHT\Documents
                        \Keysight\M8070B\Workspaces\Default\User\Settings\sw_fw_mfiles\pcie1_rx

 

optional arguments:
  -h, --help            show this help message and exit
  -mn, --moduleinfonone
                        do not show module information
  -mo, --moduleinfoonly
                        show only module information, no register

example: just the module info and I am looking at the instrument state in the CurrentSetting folder, you will be looking at another one most likely.

D:\inout\m8070instrumentsettingsv1.2>instrumentsettingsmain.exe C:\Users\fairfiel.KEYSIGHT\Documents\Keysight\M8070B\Workspaces\Default\User\Settings\CurrentSetting -mo
file=  C:\Users\fairfiel.KEYSIGHT\Documents\Keysight\M8070B\Workspaces\Default\User\Settings\CurrentSetting\InstrumentState.xml
M1
M8045A
M8045A 64GBd Generator-Clock
Keysight.SeriesM80XX.Mal.M8045
Keysight.SeriesM80XX.Mal, Version=7.2.40.2, Culture=neutral, PublicKeyToken=ced78d295d1e0f2b
M2
M8046A
M8046A 64GBd Error Analyzer
Keysight.SeriesM80XX.Mal.M8046
Keysight.SeriesM80XX.Mal, Version=7.2.40.2, Culture=neutral, PublicKeyToken=ced78d295d1e0f2b             


here is the normal output of the present state:
D:\inout\m8070instrumentsettingsv1.2>
D:\inout\m8070instrumentsettingsv1.2>instrumentsettingsmain.exe C:\Users\fairfiel.KEYSIGHT\Documents\Keysight\M8070B\Workspaces\Default\User\Settings\CurrentSetting
file=  C:\Users\fairfiel.KEYSIGHT\Documents\Keysight\M8070B\Workspaces\Default\User\Settings\CurrentSetting\InstrumentState.xml
M1
M8045A
M8045A 64GBd Generator-Clock
Keysight.SeriesM80XX.Mal.M8045
Keysight.SeriesM80XX.Mal, Version=7.2.40.2, Culture=neutral, PublicKeyToken=ced78d295d1e0f2b
M2
M8046A
M8046A 64GBd Error Analyzer
Keysight.SeriesM80XX.Mal.M8046
Keysight.SeriesM80XX.Mal, Version=7.2.40.2, Culture=neutral, PublicKeyToken=ced78d295d1e0f2b
M1 ,M1.DataOut1 ,HF Jitter ,External_Jitter_State ,False
M1 ,M1.SysInB ,Comparator ,TermVoltage ,0
M1 ,M1.SysInB ,Comparator ,Threshold ,0.25
M1 ,M1.DataOut2 ,HF Jitter ,External_Jitter_State ,False
M1 ,M1.DataOut1 ,HF Jitter ,HF_Jitter_PhaseModulationMode ,LimitedByUnitInterval
M1 ,M1.RefClkOut ,Output Timing ,RefClkOutFrequency ,RefOut10MHz
M1 ,M1.RefClkOut ,Output Timing ,Frequency ,10000000
M1 ,M1.DataOut2 ,HF Jitter ,HF_Jitter_PhaseModulationMode ,LimitedByUnitInterval
M1 ,M1 ,HF Jitter ,HF_RJ_LowPassFilter ,FILTER100
M1 ,M1 ,HF Jitter ,HF_RJ_HighPassFilter ,FILTER10
M1 ,M1.TrigOut ,HH ,ModulationDelayLine ,MediumDelayLine
M1 ,M1.DataOut1 ,Error Insertion ,ErrorInsertionState ,False
M1 ,M1.DataOut1 ,Error Insertion ,InsertSingleBitError ,None
M1 ,M1.DataOut1 ,Error Insertion ,InsertDisparityError ,None
M1 ,M1.DataOut1 ,Error Insertion ,ErrorInsertionMode ,ErrorInsertionRatioWithRandomSpacing
M1 ,M1.DataOut1 ,Error Insertion ,ErrorInsertionRateSelector ,ErrorRate10eMinus6
M1 ,M1.DataOut1 ,Embedding ,State ,False
M1 ,M1.DataOut1 ,Embedding ,ProfileFileName ,Factory/N4910_61601_measured.s2p
M1 ,M1.DataOut1 ,Embedding ,ProfileWorkspacePath ,|spprofile:Factory/N4910_61601_measured.s2p
M1 ,M1.DataOut1 ,HH ,ModulationDelayLine ,MediumDelayLine
M1 ,M1.TrigOut ,Configuration ,TrigOutOperatingMode ,SubrateClock
M1 ,M1.TrigOut ,Configuration ,SubrateFrequency ,625000000
M1 ,M1.TrigOut ,Configuration ,TrigOutSubrateDivider ,8
M1 ,M1.TrigOut ,Sequencing ,SequenceChannelRestart ,None
M1 ,M1.TrigOut ,Sequencing ,SequenceChannelDownload ,None
M1 ,M1.TrigOut ,Sequencing ,SequenceKind ,Bert
M1 ,M1.TrigOut ,Sequencing ,SequenceGranularityMultiplier ,1
M1 ,M1.TrigOut ,Sequencing ,SequenceJumpTarget ,1
M1 ,M1.DataOut2 ,HH ,ModulationDelayLine ,MediumDelayLine
M1 ,M1.CtrlOutA ,Amplifier ,Amplitude ,0.5
M1 ,M1.CtrlOutA ,Amplifier ,Offset ,0
M1 ,M1.CtrlOutA ,Amplifier ,High ,0.25
M1 ,M1.CtrlOutA ,Amplifier ,Low ,-0.25
M1 ,M1.CtrlOutA ,Amplifier ,State ,False
M1 ,M1.CtrlOutA ,Amplifier ,Polarity ,Normal
M1 ,M1.DataOut1 ,Pattern Memory ,HwState ,None
M1 ,M1.ClkGen ,SSC ,SSC_State ,False
M1 ,M1.ClkGen ,SSC ,SSC_HwState ,False
M1 ,M1.ClkGen ,SSC ,SSC_Deviation ,0.5
M1 ,M1.ClkGen ,SSC ,SSC_DeviationUp ,0
M1 ,M1.ClkGen ,SSC ,SSC_DeviationDown ,-0.5
M1 ,M1.ClkGen ,SSC ,SSC_Frequency ,33000
M1 ,M1.ClkGen ,SSC ,SSC_Type ,DownSpread
M1 ,M1.ClkGen ,SSC ,SSC_Profile ,Triangular
M1 ,M1.ClkGen ,SSC ,SSC_ProfileDownloadTrigger ,False
M1 ,M1.ClkGen ,SSC ,SSC_Shape ,Factory/Triangular.txt
M1 ,M1.ClkGen ,SSC ,SSC_Shape_WorkspacePath ,|sscprofile:Factory/Triangular.txt
M1 ,M1.ClkOut ,Amplifier ,State ,False
M1 ,M1.ClkOut ,Amplifier ,ObeyGlobalOutputState ,True
M1 ,M1.ClkOut ,Amplifier ,TermConfig ,Balanced
M1 ,M1.ClkOut ,Amplifier ,TermVoltage ,0
M1 ,M1.ClkOut ,Amplifier ,Polarity ,Normal
M1 ,M1.ClkOut ,Amplifier ,Amplitude ,0.10000000000000001
M1 ,M1.ClkOut ,Amplifier ,Offset ,0
M1 ,M1.ClkOut ,Amplifier ,High ,0.050000000000000003
M1 ,M1.ClkOut ,Amplifier ,Low ,-0.050000000000000003
M1 ,M1.DataOut2 ,Error Insertion ,ErrorInsertionState ,False
M1 ,M1.DataOut2 ,Error Insertion ,InsertSingleBitError ,None
M1 ,M1.DataOut2 ,Error Insertion ,InsertDisparityError ,None
M1 ,M1.DataOut2 ,Error Insertion ,ErrorInsertionMode ,ErrorInsertionRatioWithRandomSpacing
M1 ,M1.DataOut2 ,Error Insertion ,ErrorInsertionRateSelector ,ErrorRate10eMinus6
M1 ,M1.DataOut2 ,Embedding ,State ,False
M1 ,M1.DataOut2 ,Embedding ,ProfileFileName ,Factory/N4910_61601_measured.s2p
M1 ,M1.DataOut2 ,Embedding ,ProfileWorkspacePath ,|spprofile:Factory/N4910_61601_measured.s2p
M1 ,M1.DataOut2 ,Pattern Memory ,HwState ,None
M1 ,M1.DataOut1 ,Amplifier ,State ,False
M1 ,M1.DataOut1 ,Amplifier ,StateAsEnum ,Disabled
M1 ,M1.DataOut1 ,Amplifier ,Coupling ,Dc
M1 ,M1.DataOut1 ,Amplifier ,TermConfig ,Unbalanced
M1 ,M1.DataOut1 ,Amplifier ,TermVoltage ,0
M1 ,M1.DataOut1 ,Amplifier ,Polarity ,Normal
M1 ,M1.DataOut1 ,Amplifier ,AmplitudeRangeInternal ,2
M1 ,M1.DataOut1 ,Amplifier ,Amplitude ,0.29999999999999999
M1 ,M1.DataOut1 ,Amplifier ,PodRevision ,0
M1 ,M1.DataOut1 ,Amplifier ,Offset ,0.14999999999999999
M1 ,M1.DataOut1 ,Amplifier ,High ,0.29999999999999999
M1 ,M1.DataOut1 ,Amplifier ,Low ,0
M1 ,M1.DataOut1 ,Amplifier ,JitterState ,False
M1 ,M1.DataOut1 ,Amplifier ,Jitter ,0
M1 ,M1.SysOutA ,Amplifier ,Amplitude ,0.5
M1 ,M1.SysOutA ,Amplifier ,Offset ,0
M1 ,M1.SysOutA ,Amplifier ,High ,0.25
M1 ,M1.SysOutA ,Amplifier ,Low ,-0.25
M1 ,M1.SysOutA ,Amplifier ,State ,False
M1 ,M1.SysOutA ,Amplifier ,Polarity ,Normal
M1 ,M1.DataOut1 ,De-Embedding ,State ,False
M1 ,M1.DataOut1 ,De-Embedding ,ProfileFileName ,Factory/N4910_61601_measured.s2p
M1 ,M1.DataOut1 ,De-Embedding ,ProfileWorkspacePath ,|spprofile:Factory/N4910_61601_measured.s2p
M1 ,M1.CtrlOutB ,Amplifier ,Amplitude ,0.5
M1 ,M1.CtrlOutB ,Amplifier ,Offset ,0
M1 ,M1.CtrlOutB ,Amplifier ,High ,0.25
M1 ,M1.CtrlOutB ,Amplifier ,Low ,-0.25
M1 ,M1.CtrlOutB ,Amplifier ,State ,False
M1 ,M1.CtrlOutB ,Amplifier ,Polarity ,Normal
M1 ,M1.ClkOut ,Output Timing ,Divider ,Div1
M1 ,M1.ClkOut ,Output Timing ,DividerHw ,Div4
M1 ,M1.ClkOut ,Output Timing ,JitterDelay ,0
M1 ,M1.ClkOut ,Output Timing ,Frequency ,5000000000
M1 ,M1.ClkOut ,Output Timing ,ChannelDataRate ,5000000000
M1 ,M1.ClkOut ,Output Timing ,ChannelDataRateMultiplier ,1
M1 ,M1.ClkOut ,Output Timing ,ChannelSubRate ,HalfRate
M1 ,M1.DataOut1 ,Output Timing ,FrequencyMultiplier ,ExpPlus0
M1 ,M1.DataOut1 ,Output Timing ,Delay ,0
M1 ,M1.DataOut1 ,Output Timing ,DelayOffset ,0
M1 ,M1.DataOut1 ,Output Timing ,JitterDelay ,0
M1 ,M1.DataOut1 ,Output Timing ,CableDeskew ,0
M1 ,M1.DataOut1 ,Output Timing ,SymbolRate ,5000000000
M1 ,M1.DataOut1 ,Output Timing ,SymbolDuration ,2.0000000000000001E-10
M1 ,M1.DataOut1 ,Output Timing ,ChannelDataRate ,5000000000
M1 ,M1.DataOut1 ,Output Timing ,ChannelDataRateMultiplier ,1
M1 ,M1.DataOut1 ,Output Timing ,ChannelSubRate ,HalfRate
M1 ,M1.DataOut2 ,De-Embedding ,State ,False
M1 ,M1.DataOut2 ,De-Embedding ,ProfileFileName ,Factory/N4910_61601_measured.s2p
M1 ,M1.DataOut2 ,De-Embedding ,ProfileWorkspacePath ,|spprofile:Factory/N4910_61601_measured.s2p
M1 ,M1.CtrlInA ,Comparator ,TermVoltage ,0
M1 ,M1.CtrlInA ,Comparator ,Threshold ,0.25
M1 ,M1.ClkOut1 ,Amplifier ,State ,False
M1 ,M1.ClkOut1 ,Configuration ,SourceSelect ,DataClock
M1 ,M1.ClkOut1 ,Output Timing ,Divider ,Div2
M1 ,M1.ClkOut1 ,Output Timing ,Frequency ,2500000000
M1 ,M1.SysOutB ,Amplifier ,Amplitude ,0.5
M1 ,M1.SysOutB ,Amplifier ,Offset ,0
M1 ,M1.SysOutB ,Amplifier ,High ,0.25
M1 ,M1.SysOutB ,Amplifier ,Low ,-0.25
M1 ,M1.SysOutB ,Amplifier ,State ,False
M1 ,M1.SysOutB ,Amplifier ,Polarity ,Normal
M1 ,M1.CtrlInB ,Comparator ,TermVoltage ,0
M1 ,M1.CtrlInB ,Comparator ,Threshold ,0.25
M1 ,M1.DataOut2 ,Amplifier ,State ,False
M1 ,M1.DataOut2 ,Amplifier ,StateAsEnum ,Disabled
M1 ,M1.DataOut2 ,Amplifier ,Coupling ,Dc
M1 ,M1.DataOut2 ,Amplifier ,TermConfig ,Unbalanced
M1 ,M1.DataOut2 ,Amplifier ,TermVoltage ,0
M1 ,M1.DataOut2 ,Amplifier ,Polarity ,Normal
M1 ,M1.DataOut2 ,Amplifier ,AmplitudeRangeInternal ,2
M1 ,M1.DataOut2 ,Amplifier ,Amplitude ,0.29999999999999999
M1 ,M1.DataOut2 ,Amplifier ,PodRevision ,0
M1 ,M1.DataOut2 ,Amplifier ,Offset ,0.14999999999999999
M1 ,M1.DataOut2 ,Amplifier ,High ,0.29999999999999999
M1 ,M1.DataOut2 ,Amplifier ,Low ,0
M1 ,M1.DataOut2 ,Amplifier ,JitterState ,False
M1 ,M1.DataOut2 ,Amplifier ,Jitter ,0
M1 ,M1.System ,Configuration ,GlobalJitterState ,True
M1 ,M1.System ,Configuration ,GlobalOutputStates ,False
M1 ,M1.System ,Configuration ,GlobalSscState ,True
M1 ,M1.System ,Configuration ,GlobalSscStateRecallIndicator ,True
M1 ,M1.DataOut2 ,Output Timing ,FrequencyMultiplier ,ExpPlus0
M1 ,M1.DataOut2 ,Output Timing ,Delay ,0
M1 ,M1.DataOut2 ,Output Timing ,DelayOffset ,0
M1 ,M1.DataOut2 ,Output Timing ,JitterDelay ,0
M1 ,M1.DataOut2 ,Output Timing ,CableDeskew ,0
M1 ,M1.DataOut2 ,Output Timing ,SymbolRate ,5000000000
M1 ,M1.DataOut2 ,Output Timing ,SymbolDuration ,2.0000000000000001E-10
M1 ,M1.DataOut2 ,Output Timing ,ChannelDataRate ,5000000000
M1 ,M1.DataOut2 ,Output Timing ,ChannelDataRateMultiplier ,1
M1 ,M1.DataOut2 ,Output Timing ,ChannelSubRate ,HalfRate
M1 ,M1.ClkOut2 ,Amplifier ,State ,False
M1 ,M1.ClkOut2 ,Configuration ,SourceSelect ,DataClock
M1 ,M1.ClkOut2 ,Output Timing ,Divider ,Div2
M1 ,M1.ClkOut2 ,Output Timing ,Frequency ,2500000000
M1 ,M1.DataOut1 ,Deemphasis ,OscilloscopeChannelSelection ,None
M1 ,M1.DataOut1 ,Deemphasis ,OscilloscopeChannelLocation ,None
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisMode ,Interactive
M1 ,M1.DataOut1 ,Deemphasis ,MainCursorAutoMagnitude ,True
M1 ,M1.DataOut1 ,Deemphasis ,MainCursorSuffix ,2
M1 ,M1.DataOut1 ,Deemphasis ,NumberOfCursors ,5
M1 ,M1.DataOut1 ,Deemphasis ,NumberOfPreCursorTaps ,2
M1 ,M1.DataOut1 ,Deemphasis ,Cursor0 ,0
M1 ,M1.DataOut1 ,Deemphasis ,Cursor1 ,0
M1 ,M1.DataOut1 ,Deemphasis ,Cursor2 ,1
M1 ,M1.DataOut1 ,Deemphasis ,Cursor3 ,0
M1 ,M1.DataOut1 ,Deemphasis ,Cursor4 ,0
M1 ,M1.DataOut1 ,Deemphasis ,AmplitudeScale ,100
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisSelectPresetRegister ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisUnit ,Deempahsis_db
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPresetRegister ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_pre_03 ,NaN
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_pre_03 ,NaN
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_00 ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_00 ,100
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_01 ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_01 ,100
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_02 ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_02 ,100
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_03 ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_03 ,100
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_04 ,NaN
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_04 ,NaN
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_05 ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_05 ,100
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_DB_06 ,0
M1 ,M1.DataOut1 ,Deemphasis ,DeemphasisPreset_00_PCT_06 ,100
M1 ,M1.DataOut1 ,Deemphasis ,PCIeLtssmPresetsFileName ,Factory/FullSwing-63.xml
M1 ,M1.DataOut1 ,Deemphasis ,PCIeLtssmPresetsWorkspacePath ,|pcie-deemphasis:Factory/FullSwing-63.xml
M1 ,M1.DataOut1 ,Deemphasis ,PCIeLtssmFullSwing ,63
M1 ,M1.DataOut1 ,Deemphasis ,PCIeLtssmRequestedPreCursor ,0
M1 ,M1.DataOut1 ,Deemphasis ,PCIeLtssmRequestedPostCursor ,0
M1 ,M1.SysInA ,Comparator ,TermVoltage ,0
M1 ,M1.SysInA ,Comparator ,Threshold ,0.25
M1 ,M1.DataOut1 ,FEC Error Insertion ,FEC_ErrorInsertionState ,False
M1 ,M1.DataOut1 ,FEC Error Insertion ,FEC_ErrorInsertionMode ,PostFecNSymbolErrorsPerFrame
M1 ,M1.DataOut1 ,FEC Error Insertion ,FEC_ErrorPerFrame ,5
M1 ,M1.DataOut1 ,FEC Error Insertion ,FEC_ErrorRatio ,0.00091911764705882352
M1 ,M1.DataOut1 ,FEC Error Insertion ,InsertSingleBIPError ,None
M1 ,M1.DataOut2 ,FEC Error Insertion ,FEC_ErrorInsertionState ,False
M1 ,M1.DataOut2 ,FEC Error Insertion ,FEC_ErrorInsertionMode ,PostFecNSymbolErrorsPerFrame
M1 ,M1.DataOut2 ,FEC Error Insertion ,FEC_ErrorPerFrame ,5
M1 ,M1.DataOut2 ,FEC Error Insertion ,FEC_ErrorRatio ,0.00091911764705882352
M1 ,M1.DataOut2 ,FEC Error Insertion ,InsertSingleBIPError ,None
M1 ,M1.TrigOut ,Amplifier ,Amplitude ,0.10000000000000001
M1 ,M1.TrigOut ,Amplifier ,Offset ,0
M1 ,M1.TrigOut ,Amplifier ,High ,0.050000000000000003
M1 ,M1.TrigOut ,Amplifier ,Low ,-0.050000000000000003
M1 ,M1.TrigOut ,Amplifier ,TermVoltage ,0
M1 ,M1.TrigOut ,Amplifier ,State ,False
M1 ,M1.TrigOut ,Amplifier ,Polarity ,Normal
M1 ,M1.TrigOut ,Amplifier ,TermConfig ,Balanced
M1 ,M1.ClkOut ,LF Jitter ,LF_Jitter_State ,True
M1 ,M1.ClkOut ,LF Jitter ,JitterUnit ,Jitter_UI
M1 ,M1.ClkOut ,LF Jitter ,LF_Jitter_Delay ,2.0000000000000001E-09
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_State ,False
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Amplitude ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Amplitude_UI ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Amplitude_sec ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Frequency ,1000
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Waveform ,Sinusoid
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_State2 ,False
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Amplitude2 ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Amplitude2_UI ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Amplitude2_sec ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_PJ_Frequency2 ,1000
M1 ,M1.ClkOut ,LF Jitter ,LF_RSSC_State ,False
M1 ,M1.ClkOut ,LF Jitter ,LF_RSSC_Amplitude ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_RSSC_Amplitude_UI ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_RSSC_Amplitude_sec ,0
M1 ,M1.ClkOut ,LF Jitter ,LF_RSSC_Frequency ,33000
M1 ,M1.DataOut1 ,Line Coding ,Coding ,NRZ
M1 ,M1.DataOut1 ,Line Coding ,BitsPerSymbol ,1
M1 ,M1.DataOut1 ,Line Coding ,PAM4_SymbolMapping ,Gray
M1 ,M1.DataOut1 ,Line Coding ,PAM4_CustomSymbolMapping ,00,01,11,10
M1 ,M1.DataOut1 ,Line Coding ,PAM4_PreCoder ,False
M1 ,M1.DataOut1 ,Line Coding ,PAM4_Level_3 ,100
M1 ,M1.DataOut1 ,Line Coding ,PAM4_Level_2 ,66
M1 ,M1.DataOut1 ,Line Coding ,PAM4_Level_1 ,33
M1 ,M1.DataOut1 ,Line Coding ,PAM4_Level_0 ,0
M1 ,M1.DataOut1 ,Line Coding ,PAM3_PreCoder ,False
M1 ,M1.DataOut1 ,Line Coding ,PAM3_Level_2 ,100
M1 ,M1.DataOut1 ,Line Coding ,PAM3_Level_1 ,50
M1 ,M1.DataOut1 ,Line Coding ,PAM3_Level_0 ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_Jitter_State ,True
M1 ,M1.ClkOut ,HF Jitter ,JitterUnit ,Jitter_UI
M1 ,M1.ClkOut ,HF Jitter ,HF_Jitter_Delay ,2.0000000000000001E-09
M1 ,M1.ClkOut ,HF Jitter ,HF_Jitter_PhaseModulationMode ,LimitedByUnitInterval
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_State1 ,False
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Frequency1 ,10000000
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Amplitude1 ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Amplitude1_UI ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Amplitude1_sec ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_State2 ,False
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Frequency2 ,10000000
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Amplitude2 ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Amplitude2_UI ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_PJ_Amplitude2_sec ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_BUJ_State ,False
M1 ,M1.ClkOut ,HF Jitter ,HF_BUJ_Amplitude ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_BUJ_Amplitude_UI ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_BUJ_Amplitude_sec ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_BUJ_Polynom ,PRBS7
M1 ,M1.ClkOut ,HF Jitter ,HF_BUJ_Polynom_DataRate ,RATE625
M1 ,M1.ClkOut ,HF Jitter ,HF_BUJ_Filter ,FILTER200
M1 ,M1.ClkOut ,HF Jitter ,HF_RJ_State ,False
M1 ,M1.ClkOut ,HF Jitter ,HF_RJ_Amplitude ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_RJ_Amplitude_UI ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_RJ_Amplitude_sec ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_RJ_LowPassFilter ,FILTER100
M1 ,M1.ClkOut ,HF Jitter ,HF_RJ_HighPassFilter ,FILTERDISABLE
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_State ,False
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_Amplitude1 ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_Amplitude1_UI ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_Amplitude1_sec ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_Amplitude2 ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_Amplitude2_UI ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_Amplitude2_sec ,0
M1 ,M1.ClkOut ,HF Jitter ,HF_sRJ_LowPassFilter ,True
M1 ,M1.ClkOut ,HF Jitter ,External_Jitter_State ,False
M1 ,M1.DataOut1 ,Waveform Encoder ,Mode ,LevelLookup
M1 ,M1.DataOut2 ,Waveform Encoder ,Mode ,LevelLookup
M1 ,M1.System ,Sequencing ,SequencesChangeRequests ,DeleteAll:::::::::@null@:::Create:::Generator::::::@null@:::Bind:::Generator::::::M1.DataOut1,M1.DataOut2:::Value:::Generator:::<?xml version="1.0" encoding="utf-16"?><sequenceDefinition xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.keysight.com/schemas/M8000/DataSequence"><version>1.0.0</version><description /><phyProtocol name="None" /><sequence><loop><block length="128"><prbs polynomial="2^15-1" /></block></loop></sequence></sequenceDefinition>:::@null@:::Create:::Analyzer::::::@null@:::Bind:::Analyzer::::::M2.DataIn:::Value:::Analyzer:::<?xml version="1.0" encoding="utf-16"?><sequenceDefinition xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.keysight.com/schemas/M8000/DataSequence"><version>1.0.0</version><description /><phyProtocol name="None" /><sequence><syncAndLoopBlock length="128"><prbs polynomial="2^15-1" /></syncAndLoopBlock></sequence></sequenceDefinition>:::@null@
M1 ,M1.System ,Sequencing ,SequencesCheck ,None
M1 ,M1.System ,Sequencing ,SequencesBreak ,None
M1 ,M1.System ,Sequencing ,LinkTrainingClearLog ,None
M1 ,M1.DataOut2 ,LF Jitter ,LF_Jitter_State ,True
M1 ,M1.DataOut2 ,LF Jitter ,JitterUnit ,Jitter_UI
M1 ,M1.DataOut2 ,LF Jitter ,LF_Jitter_Delay ,2.0000000000000001E-09
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_State ,False
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Amplitude ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Amplitude_UI ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Amplitude_sec ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Frequency ,1000
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Waveform ,Sinusoid
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_State2 ,False
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Amplitude2 ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Amplitude2_UI ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Amplitude2_sec ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_PJ_Frequency2 ,1000
M1 ,M1.DataOut2 ,LF Jitter ,LF_RSSC_State ,False
M1 ,M1.DataOut2 ,LF Jitter ,LF_RSSC_Amplitude ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_RSSC_Amplitude_UI ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_RSSC_Amplitude_sec ,0
M1 ,M1.DataOut2 ,LF Jitter ,LF_RSSC_Frequency ,33000
M1 ,M1.TrigOut ,Output Timing ,Delay ,0
M1 ,M1.TrigOut ,Output Timing ,CableDeskew ,0
M1 ,M1.TrigOut ,Output Timing ,SymbolRate ,5000000000
M1 ,M1.TrigOut ,Output Timing ,SymbolDuration ,2.0000000000000001E-10
M1 ,M1.TrigOut ,Output Timing ,ChannelDataRate ,5000000000
M1 ,M1.TrigOut ,Output Timing ,ChannelDataRateMultiplier ,1
M1 ,M1.TrigOut ,Output Timing ,ChannelSubRate ,HalfRate
M1 ,M1.TrigOut ,Output Timing ,Frequency ,1000000000
M1 ,M1.DataOut2 ,Line Coding ,Coding ,NRZ
M1 ,M1.DataOut2 ,Line Coding ,BitsPerSymbol ,1
M1 ,M1.DataOut2 ,Line Coding ,PAM4_SymbolMapping ,Gray
M1 ,M1.DataOut2 ,Line Coding ,PAM4_CustomSymbolMapping ,00,01,11,10
M1 ,M1.DataOut2 ,Line Coding ,PAM4_PreCoder ,False
M1 ,M1.DataOut2 ,Line Coding ,PAM4_Level_3 ,100
M1 ,M1.DataOut2 ,Line Coding ,PAM4_Level_2 ,66
M1 ,M1.DataOut2 ,Line Coding ,PAM4_Level_1 ,33
M1 ,M1.DataOut2 ,Line Coding ,PAM4_Level_0 ,0
M1 ,M1.DataOut2 ,Line Coding ,PAM3_PreCoder ,False
M1 ,M1.DataOut2 ,Line Coding ,PAM3_Level_2 ,100
M1 ,M1.DataOut2 ,Line Coding ,PAM3_Level_1 ,50
M1 ,M1.DataOut2 ,Line Coding ,PAM3_Level_0 ,0
M1 ,M1.DataOut2 ,Deemphasis ,OscilloscopeChannelSelection ,None
M1 ,M1.DataOut2 ,Deemphasis ,OscilloscopeChannelLocation ,None
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisMode ,Interactive
M1 ,M1.DataOut2 ,Deemphasis ,MainCursorAutoMagnitude ,True
M1 ,M1.DataOut2 ,Deemphasis ,MainCursorSuffix ,2
M1 ,M1.DataOut2 ,Deemphasis ,NumberOfCursors ,5
M1 ,M1.DataOut2 ,Deemphasis ,NumberOfPreCursorTaps ,2
M1 ,M1.DataOut2 ,Deemphasis ,Cursor0 ,0
M1 ,M1.DataOut2 ,Deemphasis ,Cursor1 ,0
M1 ,M1.DataOut2 ,Deemphasis ,Cursor2 ,1
M1 ,M1.DataOut2 ,Deemphasis ,Cursor3 ,0
M1 ,M1.DataOut2 ,Deemphasis ,Cursor4 ,0
M1 ,M1.DataOut2 ,Deemphasis ,AmplitudeScale ,100
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisSelectPresetRegister ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisUnit ,Deempahsis_db
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPresetRegister ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_pre_03 ,NaN
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_pre_03 ,NaN
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_00 ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_00 ,100
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_01 ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_01 ,100
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_02 ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_02 ,100
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_03 ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_03 ,100
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_04 ,NaN
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_04 ,NaN
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_05 ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_05 ,100
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_DB_06 ,0
M1 ,M1.DataOut2 ,Deemphasis ,DeemphasisPreset_00_PCT_06 ,100
M1 ,M1.DataOut2 ,Deemphasis ,PCIeLtssmPresetsFileName ,Factory/FullSwing-63.xml
M1 ,M1.DataOut2 ,Deemphasis ,PCIeLtssmPresetsWorkspacePath ,|pcie-deemphasis:Factory/FullSwing-63.xml
M1 ,M1.DataOut2 ,Deemphasis ,PCIeLtssmFullSwing ,63
M1 ,M1.DataOut2 ,Deemphasis ,PCIeLtssmRequestedPreCursor ,0
M1 ,M1.DataOut2 ,Deemphasis ,PCIeLtssmRequestedPostCursor ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_Jitter_State ,True
M1 ,M1.DataOut1 ,LF Jitter ,JitterUnit ,Jitter_UI
M1 ,M1.DataOut1 ,LF Jitter ,LF_Jitter_Delay ,2.0000000000000001E-09
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_State ,False
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Amplitude ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Amplitude_UI ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Amplitude_sec ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Frequency ,1000
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Waveform ,Sinusoid
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_State2 ,False
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Amplitude2 ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Amplitude2_UI ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Amplitude2_sec ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_PJ_Frequency2 ,1000
M1 ,M1.DataOut1 ,LF Jitter ,LF_RSSC_State ,False
M1 ,M1.DataOut1 ,LF Jitter ,LF_RSSC_Amplitude ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_RSSC_Amplitude_UI ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_RSSC_Amplitude_sec ,0
M1 ,M1.DataOut1 ,LF Jitter ,LF_RSSC_Frequency ,33000
M1 ,M1.System ,Local Bus ,JitterSourceHfSyncFlag ,False
M1 ,M1.System ,Local Bus ,JitterSourceLfPJSyncFlag ,False
M1 ,M1.System ,Local Bus ,JitterSourceLfPJLoadFlag ,False
M1 ,M1.System ,Local Bus ,JitterSourceLfSscSyncFlag ,False
M1 ,M1.System ,Local Bus ,JitterSourceLfRSscSyncFlag ,False
M1 ,M1.System ,Local Bus ,JitterSweepSyncFlag ,False
M1 ,M1.DataOut1 ,Status ,JitterState ,False
M1 ,M1.DataOut1 ,Status ,SscState ,False
M1 ,M1.DataOut1 ,Sequencing ,SequenceChannelExists ,True
M1 ,M1.DataOut1 ,Sequencing ,SequenceKind ,Bert
M1 ,M1.DataOut1 ,Sequencing ,SequenceGranularityMultiplier ,8
M1 ,M1.DataOut1 ,Sequencing ,SequenceChannelRestart ,None
M1 ,M1.DataOut1 ,Sequencing ,SequenceJumpTarget ,1
M1 ,M1.DataOut1 ,Sequencing ,CoderEnabled ,False
M1 ,M1.DataOut1 ,Sequencing ,SequenceChannelDownload ,None
M1 ,M1.DataOut1 ,Sequencing ,PhyProtocol ,None
M1 ,M1.DataOut2 ,Status ,JitterState ,False
M1 ,M1.DataOut2 ,Status ,SscState ,False
M1 ,M1.DataOut1 ,SSC ,SSC_State ,False
M1 ,M1.DataOut1 ,SSC ,SSC_Deviation ,0.5
M1 ,M1.DataOut1 ,SSC ,SSC_Frequency ,33000
M1 ,M1.DataOut1 ,SSC ,SSC_Type ,DownSpread
M1 ,M1.DataOut1 ,SSC ,SSC_Profile ,Triangular
M1 ,M1.DataOut1 ,SSC ,SSC_ProfileDownloadTrigger ,False
M1 ,M1.DataOut2 ,SSC ,SSC_State ,False
M1 ,M1.DataOut2 ,SSC ,SSC_Deviation ,0.5
M1 ,M1.DataOut2 ,SSC ,SSC_Frequency ,33000
M1 ,M1.DataOut2 ,SSC ,SSC_Type ,DownSpread
M1 ,M1.DataOut2 ,SSC ,SSC_Profile ,Triangular
M1 ,M1.DataOut2 ,SSC ,SSC_ProfileDownloadTrigger ,False
M1 ,M1.DataOut2 ,Sequencing ,SequenceChannelExists ,True
M1 ,M1.DataOut2 ,Sequencing ,SequenceKind ,Bert
M1 ,M1.DataOut2 ,Sequencing ,SequenceGranularityMultiplier ,8
M1 ,M1.DataOut2 ,Sequencing ,SequenceChannelRestart ,None
M1 ,M1.DataOut2 ,Sequencing ,SequenceJumpTarget ,1
M1 ,M1.DataOut2 ,Sequencing ,CoderEnabled ,False
M1 ,M1.DataOut2 ,Sequencing ,SequenceChannelDownload ,None
M1 ,M1.DataOut2 ,Sequencing ,PhyProtocol ,None
M1 ,M1.DataOut1 ,Sequencing ,LinkTrainingState ,L0
M1 ,M1.ClkGen ,Synthesizer ,TriggerSource ,Reference
M1 ,M1.ClkGen ,Synthesizer ,TriggerInternalMode_Source ,Internal
M1 ,M1.ClkGen ,Synthesizer ,TriggerInternalMode_Frequency ,5000000000
M1 ,M1.ClkGen ,Synthesizer ,Frequency ,5000000000
M1 ,M1.ClkGen ,Synthesizer ,Period ,2.0000000000000003E-10
M1 ,M1.ClkGen ,Synthesizer ,TriggerReferenceMode_ReferenceFrequency ,Ref10
M1 ,M1.ClkGen ,Synthesizer ,TriggerReferenceMode_Frequency ,5000000000
M1 ,M1.ClkGen ,Synthesizer ,TriggerDirectMode_Frequency ,8200000000
M1 ,M1.ClkGen ,Synthesizer ,TriggerDirectMode_DetectedFrequency ,8200000000
M1 ,M1.ClkGen ,Synthesizer ,TriggerClockMultiplierMode_Frequency ,100000000
M1 ,M1.ClkGen ,Synthesizer ,TriggerClockMultiplierMode_Bandwidth ,Bw100
M1 ,M1.ClkGen ,Synthesizer ,TriggerClockMultiplierMode_Multiplier ,80
M1 ,M1.ClkGen ,Synthesizer ,TriggerClockMultiplierMode_Divider ,1
M1 ,M1.ClkGen ,Synthesizer ,TriggerClockMultiplierMode_DetectedFrequency ,100000000
M1 ,M1.ClkGen ,Synthesizer ,GClk1Frequency ,10000000000
M1 ,M1.ClkGen ,Synthesizer ,GClk1FrequencySscOffset ,0
M1 ,M1.ClkGen ,Synthesizer ,GClk1FrequencyMultiplier ,2
M1 ,M1.ClkGen ,Synthesizer ,GClk1HwState ,True
M1 ,M1.ClkGen ,Synthesizer ,GClk2Frequency ,10000000000
M1 ,M1.ClkGen ,Synthesizer ,GClk2HwState ,False
M1 ,M1.ClkGen ,Synthesizer ,RefClkInFrequency ,10000000
M1 ,M1.ClkGen ,Synthesizer ,RefClkInFrequencyMeas ,8000000000
M1 ,M1.ClkGen ,Synthesizer ,RefClkInHwState ,True
M1 ,M1.ClkGen ,Synthesizer ,RequestTemporaryStop ,None
M1 ,M1.ClkGen ,Synthesizer ,ActualRunModeGClk1 ,Running
M1 ,M1.ClkGen ,Synthesizer ,TargetRunModeGClk1 ,Running
M1 ,M1.ClkGen ,Synthesizer ,WordWidth ,WordWidth64Bits
M1 ,M1.ClkGen ,Synthesizer ,CoderMode ,Code132
M1 ,M1.ClkGen ,Synthesizer ,SyncOutState ,On
M1 ,M1.ClkGen ,Synthesizer ,SyncInState ,Off
M1 ,M1.DataOut2 ,Sequencing ,LinkTrainingState ,L0
M1 ,M1.DataOut1 ,HF Jitter ,HF_Jitter_State ,True
M1 ,M1.DataOut1 ,HF Jitter ,JitterUnit ,Jitter_UI
M1 ,M1.DataOut1 ,HF Jitter ,HF_Jitter_Delay ,2.0000000000000001E-09
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_State1 ,False
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Frequency1 ,10000000
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Amplitude1 ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Amplitude1_UI ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Amplitude1_sec ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_State2 ,False
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Frequency2 ,10000000
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Amplitude2 ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Amplitude2_UI ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_PJ_Amplitude2_sec ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_BUJ_State ,False
M1 ,M1.DataOut1 ,HF Jitter ,HF_BUJ_Amplitude ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_BUJ_Amplitude_UI ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_BUJ_Amplitude_sec ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_BUJ_Polynom ,PRBS7
M1 ,M1.DataOut1 ,HF Jitter ,HF_BUJ_Polynom_DataRate ,RATE625
M1 ,M1.DataOut1 ,HF Jitter ,HF_BUJ_Filter ,FILTER200
M1 ,M1.DataOut1 ,HF Jitter ,HF_RJ_State ,False
M1 ,M1.DataOut1 ,HF Jitter ,HF_RJ_Amplitude ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_RJ_Amplitude_UI ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_RJ_Amplitude_sec ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_RJ_LowPassFilter ,FILTER100
M1 ,M1.DataOut1 ,HF Jitter ,HF_RJ_HighPassFilter ,FILTERDISABLE
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_State ,False
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Amplitude1 ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Amplitude1_UI ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Amplitude1_sec ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Amplitude2 ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Amplitude2_UI ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Amplitude2_sec ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Total ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Total_UI ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_Total_sec ,0
M1 ,M1.DataOut1 ,HF Jitter ,HF_sRJ_LowPassFilter ,True
M1 ,M1.DataOut2 ,HF Jitter ,HF_Jitter_State ,True
M1 ,M1.DataOut2 ,HF Jitter ,JitterUnit ,Jitter_UI
M1 ,M1.DataOut2 ,HF Jitter ,HF_Jitter_Delay ,2.0000000000000001E-09
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_State1 ,False
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Frequency1 ,10000000
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Amplitude1 ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Amplitude1_UI ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Amplitude1_sec ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_State2 ,False
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Frequency2 ,10000000
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Amplitude2 ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Amplitude2_UI ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_PJ_Amplitude2_sec ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_BUJ_State ,False
M1 ,M1.DataOut2 ,HF Jitter ,HF_BUJ_Amplitude ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_BUJ_Amplitude_UI ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_BUJ_Amplitude_sec ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_BUJ_Polynom ,PRBS7
M1 ,M1.DataOut2 ,HF Jitter ,HF_BUJ_Polynom_DataRate ,RATE625
M1 ,M1.DataOut2 ,HF Jitter ,HF_BUJ_Filter ,FILTER200
M1 ,M1.DataOut2 ,HF Jitter ,HF_RJ_State ,False
M1 ,M1.DataOut2 ,HF Jitter ,HF_RJ_Amplitude ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_RJ_Amplitude_UI ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_RJ_Amplitude_sec ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_RJ_LowPassFilter ,FILTER100
M1 ,M1.DataOut2 ,HF Jitter ,HF_RJ_HighPassFilter ,FILTERDISABLE
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_State ,False
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Amplitude1 ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Amplitude1_UI ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Amplitude1_sec ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Amplitude2 ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Amplitude2_UI ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Amplitude2_sec ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Total ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Total_UI ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_Total_sec ,0
M1 ,M1.DataOut2 ,HF Jitter ,HF_sRJ_LowPassFilter ,True
M2 ,M2.CtrlInA ,Comparator ,TermVoltage ,0
M2 ,M2.CtrlInA ,Comparator ,Threshold ,0.25
M2 ,M2.DataIn ,Pattern Memory ,HwState ,None
M2 ,M2.DataIn ,Analyzer ,CounterCompareMode ,SequencerExpectedVsEyeSweep
M2 ,M2.DataIn ,Analyzer ,ForceBitCounterEnable ,False
M2 ,M2.DataIn ,Run Control ,RunState ,ReadyToRun
M2 ,M2.DataIn ,Run Control ,RecoveryStrategy ,AutomaticRestart
M2 ,M2.DataIn ,Run Control ,ActualRunMode ,Running
M2 ,M2.DataIn ,Run Control ,TargetRunMode ,Running
M2 ,M2.DataIn ,Analyzer ,DataLossMonitoringInterval ,30000000
M2 ,M2.CtrlOutA ,Amplifier ,Amplitude ,0.5
M2 ,M2.CtrlOutA ,Amplifier ,Offset ,0
M2 ,M2.CtrlOutA ,Amplifier ,High ,0.25
M2 ,M2.CtrlOutA ,Amplifier ,Low ,-0.25
M2 ,M2.CtrlOutA ,Amplifier ,State ,False
M2 ,M2.CtrlOutA ,Amplifier ,Polarity ,Normal
M2 ,M2.System ,Sequencing ,SequencesChangeRequests ,Reset:::::::::
M2 ,M2.System ,Sequencing ,SequencesCheck ,None
M2 ,M2.DataIn ,Clock ,ClockSource ,ClkIn
M2 ,M2.DataIn ,Clock ,ExtClockRecoverySelection ,None
M2 ,M2.DataIn ,Clock ,ExtClockRecoveryLocation ,None
M2 ,M2.DataIn ,Clock ,TrackState ,True
M2 ,M2.DataIn ,Clock ,Frequency ,2500000000
M2 ,M2.DataIn ,Clock ,MultiplierEnum ,ExpPlus1
M2 ,M2.DataIn ,Clock ,Multiplier ,2
M2 ,M2.DataIn ,Clock ,SymbolRate ,5000000000
M2 ,M2.DataIn ,Clock ,SamplingFactor ,Normal
M2 ,M2.DataIn ,Clock ,ClockIsGood ,True
M2 ,M2 ,Hardware ,M8046A_FpgaCapabilitySelector ,Default
M2 ,M2.DataIn ,Sequencing ,SequenceChannelExists ,True
M2 ,M2.DataIn ,Sequencing ,SequenceKind ,Bert
M2 ,M2.DataIn ,Sequencing ,SequenceGranularityMultiplier ,8
M2 ,M2.DataIn ,Sequencing ,SequenceChannelRestart ,None
M2 ,M2.DataIn ,Sequencing ,SequenceJumpTarget ,1
M2 ,M2.DataIn ,Sequencing ,CoderEnabled ,False
M2 ,M2.DataIn ,Sequencing ,SequenceChannelDownload ,None
M2 ,M2.DataIn ,Sequencing ,PhyProtocol ,None
M2 ,M2.DataIn ,Line Coding ,Coding ,NRZ
M2 ,M2.DataIn ,Line Coding ,BitsPerSymbol ,1
M2 ,M2.DataIn ,Line Coding ,PAM4_SymbolMapping ,Gray
M2 ,M2.DataIn ,Line Coding ,PAM4_CustomSymbolMapping ,00,01,11,10
M2 ,M2.DataIn ,Comparator ,PAM4_Threshold_23 ,0.125
M2 ,M2.DataIn ,Comparator ,PAM4_Threshold_12 ,0
M2 ,M2.DataIn ,Comparator ,PAM4_Threshold_01 ,-0.125
M2 ,M2.DataIn ,FIR ,State ,True
M2 ,M2.DataIn ,Analyzer ,SequenceChannelSyncNow ,None
M2 ,M2.DataIn ,Sequencing ,SyncRetries ,2
M2 ,M2.Simulation ,Output Timing ,Delay ,0
M2 ,M2.Simulation ,Output Timing ,DelayOffset ,0
M2 ,M2.Simulation ,Output Timing ,JitterDelay ,0
M2 ,M2.Simulation ,Output Timing ,CableDeskew ,0
M2 ,M2.Simulation ,Output Timing ,SymbolRate ,8000000000
M2 ,M2.Simulation ,Output Timing ,SymbolDuration ,2.0000000000000001E-10
M2 ,M2.Simulation ,Output Timing ,ChannelDataRate ,8000000000
M2 ,M2.Simulation ,Output Timing ,ChannelDataRateMultiplier ,1
M2 ,M2.Simulation ,Output Timing ,ChannelSubRate ,FullRate
M2 ,M2.DataIn ,Capture ,State ,False
M2 ,M2.DataIn ,Capture ,TriggeredBy ,Immediate
M2 ,M2.DataIn ,Capture ,SlaveTriggered ,False
M2 ,M2.DataIn ,Capture ,CtrlInSlope ,Rising
M2 ,M2.DataIn ,Capture ,ManualTrigger ,None
M2 ,M2.DataIn ,Capture ,Holdoff ,10000
M2 ,M2.DataIn ,Capture ,PostTriggerDepth ,10000
M2 ,M2.DataIn ,Capture ,CaptureState ,Stopped
M2 ,M2.DataIn ,CDR ,CDR_TransitionDensity_1stOrder ,50
M2 ,M2.DataIn ,CDR ,CDR_TransitionDensity_2ndOrder ,50
M2 ,M2.DataIn ,CDR ,CDR_LoopOrder ,FirstOrder
M2 ,M2.DataIn ,CDR ,CDR_LoopBandwidth_User_1stOrder ,2000000
M2 ,M2.DataIn ,CDR ,CDR_LoopBandwidth_User_2ndOrder ,2000000
M2 ,M2.DataIn ,CDR ,CDR_LoopSelection ,Loop1
M2 ,M2.DataIn ,CDR ,CDR_AutoMode_2ndOrder ,True
M2 ,M2.DataIn ,CDR ,CDR_Peaking_User ,1
M2 ,M2.DataIn ,CDR ,CDR_ControlledBy ,Manual
M2 ,M2.DataIn ,CDR ,CDR_State ,False
M2 ,M2.DataIn ,CDR ,CDR_PretuneMode ,False
M2 ,M2.DataIn ,CDR ,CDR_ConnectorOutState ,False
M2 ,M2.DataIn ,CDR ,CDR_ConnectorOutStateValidRange ,True
M2 ,M2.DataIn ,CDR ,AutoRelock ,True
M2 ,M2.DataIn ,JTOL ,JTOL_PJ_Frequency ,0
M2 ,M2.DataIn ,JTOL ,JTOL_PJ_AmplitudeUI ,0
M2 ,M2.DataIn ,JTOL ,JTOL_LBW_NumberOfSettings ,1
M2 ,M2.DataIn ,JTOL ,JTOL_LBW_Selection ,1
M2 ,M2.DataIn ,Comparator ,PeakingOffset ,0
M2 ,M2.DataIn ,Comparator ,Threshold ,0
M2 ,M2.DataIn ,Comparator ,Polarity ,Normal
M2 ,M2.DataIn ,Comparator ,InputVoltageWindow ,0.5
M2 ,M2.DataIn ,Comparator ,InputVoltageWindowState ,True
M2 ,M2.DataIn ,Comparator ,CommonModeVoltage ,0
M2 ,M2.DataIn ,Comparator ,Coupling ,Ac
M2 ,M2.DataIn ,Comparator ,Sensitivity ,Normal
M2 ,M2.DataIn ,Comparator ,TerminationConfiguration ,Balanced
M2 ,M2.DataIn ,Comparator ,TermVoltage ,0
M2 ,M2.DataIn ,Comparator ,CompareMode ,Differential
M2 ,M2.DataIn ,Analyzer ,PatternSyncMode ,Normal
M2 ,M2.DataIn ,Analyzer ,PatternSyncType ,Automatic
M2 ,M2.DataIn ,Analyzer ,PatternSyncBERThreshold ,ExpMinus3
M2 ,M2.DataIn ,Analyzer ,PatternSyncBERThresholdAsRatio ,0.001
M2 ,M2.DataIn ,Analyzer ,AlignmentBERThreshold ,0.001
M2 ,M2.DataIn ,Analyzer ,AlignmentBERThresholdAsRatio ,0.001
M2 ,M2.DataIn ,Alignment Results ,EyeWidth ,NaN
M2 ,M2.DataIn ,Alignment Results ,EyeHeight ,NaN
M2 ,M2.DataIn ,Alignment Results ,EyeHeight23 ,NaN
M2 ,M2.DataIn ,Alignment Results ,EyeHeight12 ,NaN
M2 ,M2.DataIn ,Alignment Results ,EyeHeight01 ,NaN
M2 ,M2.DataIn ,Alignment Results ,OptDelay ,NaN
M2 ,M2.DataIn ,Alignment Results ,InputRange ,NaN
M2 ,M2.DataIn ,Alignment Results ,OptThreshold ,NaN
M2 ,M2.DataIn ,Alignment Results ,PAM4_Threshold_23 ,NaN
M2 ,M2.DataIn ,Alignment Results ,PAM4_Threshold_12 ,0
M2 ,M2.DataIn ,Alignment Results ,PAM4_Threshold_01 ,NaN
M2 ,M2.DataIn ,Alignment Results ,Polarity ,Normal
M2 ,M2.DataIn ,Input Timing ,FrequencyMultiplier ,ExpPlus0
M2 ,M2.DataIn ,Input Timing ,Delay ,0
M2 ,M2.DataIn ,Input Timing ,Equalization ,Off
M2 ,M2.DataIn ,Equalization ,AutoSet ,None
M2 ,M2.DataIn ,Equalization ,EqMode ,PresetWithCableCompensation
M2 ,M2.DataIn ,Equalization ,EqLevel ,0
M2 ,M2.DataIn ,Equalization ,Cursor0 ,0
M2 ,M2.DataIn ,Equalization ,Cursor1 ,0.012999999999999999
M2 ,M2.DataIn ,Equalization ,Cursor2 ,1
M2 ,M2.DataIn ,Equalization ,Cursor3 ,0.012
M2 ,M2.DataIn ,Equalization ,Cursor4 ,0.001
M2 ,M2.DataIn ,Equalization ,Cursor5 ,0.001
M2 ,M2.DataIn ,Equalization ,Cursor6 ,0
M2 ,M2.DataIn ,Equalization ,Cursor7 ,0
M2 ,M2.DataIn ,Equalization ,Cursor8 ,0
M2 ,M2.DataIn ,Equalization ,Cursor9 ,0
M2 ,M2.DataIn ,Equalization ,Cursor10 ,0
M2 ,M2.DataIn ,Equalization ,Cursor11 ,0
M2 ,M2.DataIn ,Equalization ,Cursor12 ,0
M2 ,M2.DataIn ,Equalization ,Cursor13 ,0
M2 ,M2.DataIn ,Equalization ,Cursor14 ,0
M2 ,M2.DataIn ,Equalization ,Cursor15 ,0
M2 ,M2.DataIn ,Equalization ,SumOfCursors ,1.0289999999999999
M2 ,M2.DataIn ,Equalization ,AutoSetAdoptionRate ,0.01
M2 ,M2.DataIn ,Equalization ,AutoSetNumberOfUI ,1000000
M2 ,M2.DataIn ,Input Timing ,SymbolRate ,5000000000
M2 ,M2.DataIn ,Input Timing ,SymbolDuration ,2.0000000000000001E-10
M2 ,M2.DataIn ,Input Timing ,ChannelDataRate ,5000000000
M2 ,M2.DataIn ,Input Timing ,ChannelDataRateMultiplier ,1
M2 ,M2.DataIn ,Input Timing ,ChannelSubRate ,HalfRate
M2 ,M2.Simulation ,Generator ,MarkDensity ,50
M2 ,M2.Simulation ,Amplifier ,Polarity ,Normal
M2 ,M2.Simulation ,HF Jitter ,RandomJitter ,0.0025000000000000001
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Amplitude1_UI ,0
M2 ,M2.Simulation ,Generator ,RandomNoise ,0.0025000000000000001
M2 ,M2.Simulation ,Generator ,SINoise ,0
M2 ,M2.Simulation ,Amplifier ,Amplitude ,0.20000000000000001
M2 ,M2.Simulation ,Amplifier ,Offset ,0
M2 ,M2.Simulation ,Amplifier ,High ,0.10000000000000001
M2 ,M2.Simulation ,Amplifier ,Low ,-0.10000000000000001
M2 ,M2.Simulation ,Line Coding ,Coding ,NRZ
M2 ,M2.Simulation ,Line Coding ,PAM4_SymbolMapping ,Gray
M2 ,M2.Simulation ,Line Coding ,PAM4_CustomSymbolMapping ,00,01,11,10
M2 ,M2.Simulation ,Line Coding ,BitsPerSymbol ,1
M2 ,M2.Simulation ,Line Coding ,PAM4_Level_3 ,100
M2 ,M2.Simulation ,Line Coding ,PAM4_Level_2 ,66
M2 ,M2.Simulation ,Line Coding ,PAM4_Level_1 ,33
M2 ,M2.Simulation ,Line Coding ,PAM4_Level_0 ,0
M2 ,M2.Simulation ,Generator ,AngularFrequency ,10
M2 ,M2.Simulation ,Generator ,DampingFactor ,70
M2 ,M2.Simulation ,Error Insertion ,ErrorInsertionRateSelector ,ErrorRate10eMinus6
M2 ,M2.Simulation ,Error Insertion ,ErrorInsertionState ,False
M2 ,M2.Simulation ,LF Jitter ,LF_Jitter_State ,True
M2 ,M2.Simulation ,LF Jitter ,JitterUnit ,Jitter_UI
M2 ,M2.Simulation ,LF Jitter ,LF_Jitter_Delay ,0
M2 ,M2.Simulation ,LF Jitter ,LF_PJ_State ,False
M2 ,M2.Simulation ,LF Jitter ,LF_PJ_Amplitude ,0
M2 ,M2.Simulation ,LF Jitter ,LF_PJ_Amplitude_UI ,0
M2 ,M2.Simulation ,LF Jitter ,LF_PJ_Amplitude_sec ,0
M2 ,M2.Simulation ,LF Jitter ,LF_PJ_Frequency ,1000
M2 ,M2.Simulation ,LF Jitter ,LF_PJ_Waveform ,Sinusoid
M2 ,M2.Simulation ,LF Jitter ,LF_RSSC_State ,False
M2 ,M2.Simulation ,LF Jitter ,LF_RSSC_Amplitude ,0
M2 ,M2.Simulation ,LF Jitter ,LF_RSSC_Amplitude_UI ,0
M2 ,M2.Simulation ,LF Jitter ,LF_RSSC_Amplitude_sec ,0
M2 ,M2.Simulation ,LF Jitter ,LF_RSSC_Frequency ,33000
M2 ,M2.Simulation ,HF Jitter ,HF_Jitter_State ,True
M2 ,M2.Simulation ,HF Jitter ,JitterUnit ,Jitter_UI
M2 ,M2.Simulation ,HF Jitter ,HF_Jitter_Delay ,0
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_State1 ,False
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Frequency1 ,10000000
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Amplitude1 ,0
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Amplitude1_sec ,0
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_State2 ,False
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Frequency2 ,10000000
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Amplitude2 ,0
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Amplitude2_UI ,0
M2 ,M2.Simulation ,HF Jitter ,HF_PJ_Amplitude2_sec ,0
M2 ,M2.Simulation ,HF Jitter ,HF_BUJ_State ,False
M2 ,M2.Simulation ,HF Jitter ,HF_BUJ_Amplitude ,0
M2 ,M2.Simulation ,HF Jitter ,HF_BUJ_Amplitude_UI ,0
M2 ,M2.Simulation ,HF Jitter ,HF_BUJ_Amplitude_sec ,0
M2 ,M2.Simulation ,HF Jitter ,HF_BUJ_Polynom ,PRBS7
M2 ,M2.Simulation ,HF Jitter ,HF_BUJ_Polynom_DataRate ,RATE625
M2 ,M2.Simulation ,HF Jitter ,HF_BUJ_Filter ,FILTER200
M2 ,M2.Simulation ,HF Jitter ,HF_RJ_State ,False
M2 ,M2.Simulation ,HF Jitter ,HF_RJ_Amplitude ,0
M2 ,M2.Simulation ,HF Jitter ,HF_RJ_Amplitude_UI ,0
M2 ,M2.Simulation ,HF Jitter ,HF_RJ_Amplitude_sec ,0
M2 ,M2.Simulation ,HF Jitter ,HF_RJ_LowPassFilter ,FILTER100
M2 ,M2.Simulation ,HF Jitter ,HF_RJ_HighPassFilter ,FILTERDISABLE
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_State ,False
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Amplitude1 ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Amplitude1_UI ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Amplitude1_sec ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Amplitude2 ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Amplitude2_UI ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Amplitude2_sec ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Total ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Total_UI ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_Total_sec ,0
M2 ,M2.Simulation ,HF Jitter ,HF_sRJ_LowPassFilter ,True

