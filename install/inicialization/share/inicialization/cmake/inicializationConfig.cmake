# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_inicialization_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED inicialization_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(inicialization_FOUND FALSE)
  elseif(NOT inicialization_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(inicialization_FOUND FALSE)
  endif()
  return()
endif()
set(_inicialization_CONFIG_INCLUDED TRUE)

# output package information
if(NOT inicialization_FIND_QUIETLY)
  message(STATUS "Found inicialization: 0.0.0 (${inicialization_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'inicialization' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${inicialization_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(inicialization_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${inicialization_DIR}/${_extra}")
endforeach()
