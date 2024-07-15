cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(SlicerBratsPreprocessor)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/UWA-Medical-Physics/SlicerBratsPreprocessor")
set(EXTENSION_CATEGORY "segmentation")
set(EXTENSION_CONTRIBUTORS "saima safdar (UWA)")
set(EXTENSION_DESCRIPTION "Supports image preprocessing steps and is based on the brats toolkit preprocessor.")
set(EXTENSION_ICONURL "https://github.com/UWA-Medical-Physics/SlicerBratsPreprocessor/blob/main/SlicerBratsPreprocessor1.png")
set(EXTENSION_SCREENSHOTURLS "https://github.com/UWA-Medical-Physics/SlicerBratsPreprocessor/blob/main/SlicerBratsPreprocessor.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(SlicerBratsPreprocessor)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
