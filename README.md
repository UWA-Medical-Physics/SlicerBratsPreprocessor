# SlicerBratsPreprocessor
Slicer Brats Preprocessor is the wrapper for performing the preprocessing steps of the brattoolkit. The brats-toolkit will be installed automatically with the first use of the module. 

For installing the docker installation follow the steps on https://github.com/UWA-Medical-Physics/SlicerBatchBrainMRTumorSegmentation.

Slicer scriptedcli module for brats preprocessor steps.
Following the GUI for the brats preprocessor. 
## Inputs
The inputs are:
- Directory path to the patients data
- Flair file path
- T1 file path
- T2 file path
- T1c file path
![image](https://github.com/user-attachments/assets/3f4e9f6d-bf34-41d3-8d50-c905499a0e25)




## Outputs
The outputs from the brats preprocessor are the following folders.
![image](https://github.com/user-attachments/assets/101b517b-56ab-44d5-9f20-02729389f20c)

The outputs from the first folder are used to perform further processing in the pipeline. The segmentation of the pre-processed data. 
For segmenting the above acquired preprocessed data, use the SlicerBratsSegmentator module. https://github.com/UWA-Medical-Physics/SlicerBratsSegmentator

