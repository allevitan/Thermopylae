# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/cmake-gui

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/camcv

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/camcv

# Include any dependencies generated for this target.
include CMakeFiles/camcv_vid0.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/camcv_vid0.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/camcv_vid0.dir/flags.make

CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o: CMakeFiles/camcv_vid0.dir/flags.make
CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o: RaspiCamControl.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pi/camcv/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o   -c /home/pi/camcv/RaspiCamControl.c

CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /home/pi/camcv/RaspiCamControl.c > CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.i

CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /home/pi/camcv/RaspiCamControl.c -o CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.s

CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.requires:
.PHONY : CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.requires

CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.provides: CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.requires
	$(MAKE) -f CMakeFiles/camcv_vid0.dir/build.make CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.provides.build
.PHONY : CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.provides

CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.provides.build: CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o

CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o: CMakeFiles/camcv_vid0.dir/flags.make
CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o: RaspiCLI.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pi/camcv/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o   -c /home/pi/camcv/RaspiCLI.c

CMakeFiles/camcv_vid0.dir/RaspiCLI.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/camcv_vid0.dir/RaspiCLI.c.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /home/pi/camcv/RaspiCLI.c > CMakeFiles/camcv_vid0.dir/RaspiCLI.c.i

CMakeFiles/camcv_vid0.dir/RaspiCLI.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/camcv_vid0.dir/RaspiCLI.c.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /home/pi/camcv/RaspiCLI.c -o CMakeFiles/camcv_vid0.dir/RaspiCLI.c.s

CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.requires:
.PHONY : CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.requires

CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.provides: CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.requires
	$(MAKE) -f CMakeFiles/camcv_vid0.dir/build.make CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.provides.build
.PHONY : CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.provides

CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.provides.build: CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o

CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o: CMakeFiles/camcv_vid0.dir/flags.make
CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o: RaspiPreview.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pi/camcv/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o   -c /home/pi/camcv/RaspiPreview.c

CMakeFiles/camcv_vid0.dir/RaspiPreview.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/camcv_vid0.dir/RaspiPreview.c.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /home/pi/camcv/RaspiPreview.c > CMakeFiles/camcv_vid0.dir/RaspiPreview.c.i

CMakeFiles/camcv_vid0.dir/RaspiPreview.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/camcv_vid0.dir/RaspiPreview.c.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /home/pi/camcv/RaspiPreview.c -o CMakeFiles/camcv_vid0.dir/RaspiPreview.c.s

CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.requires:
.PHONY : CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.requires

CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.provides: CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.requires
	$(MAKE) -f CMakeFiles/camcv_vid0.dir/build.make CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.provides.build
.PHONY : CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.provides

CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.provides.build: CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o

CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o: CMakeFiles/camcv_vid0.dir/flags.make
CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o: camcv_vid0.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pi/camcv/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o   -c /home/pi/camcv/camcv_vid0.c

CMakeFiles/camcv_vid0.dir/camcv_vid0.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/camcv_vid0.dir/camcv_vid0.c.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /home/pi/camcv/camcv_vid0.c > CMakeFiles/camcv_vid0.dir/camcv_vid0.c.i

CMakeFiles/camcv_vid0.dir/camcv_vid0.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/camcv_vid0.dir/camcv_vid0.c.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /home/pi/camcv/camcv_vid0.c -o CMakeFiles/camcv_vid0.dir/camcv_vid0.c.s

CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.requires:
.PHONY : CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.requires

CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.provides: CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.requires
	$(MAKE) -f CMakeFiles/camcv_vid0.dir/build.make CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.provides.build
.PHONY : CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.provides

CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.provides.build: CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o

# Object files for target camcv_vid0
camcv_vid0_OBJECTS = \
"CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o" \
"CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o" \
"CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o" \
"CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o"

# External object files for target camcv_vid0
camcv_vid0_EXTERNAL_OBJECTS =

camcv_vid0: CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o
camcv_vid0: CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o
camcv_vid0: CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o
camcv_vid0: CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o
camcv_vid0: CMakeFiles/camcv_vid0.dir/build.make
camcv_vid0: /opt/vc/lib/libmmal_core.so
camcv_vid0: /opt/vc/lib/libmmal_util.so
camcv_vid0: /opt/vc/lib/libmmal_vc_client.so
camcv_vid0: /opt/vc/lib/libvcos.so
camcv_vid0: /opt/vc/lib/libbcm_host.so
camcv_vid0: /usr/local/lib/libopencv_calib3d.so
camcv_vid0: /usr/local/lib/libopencv_contrib.so
camcv_vid0: /usr/local/lib/libopencv_core.so
camcv_vid0: /usr/local/lib/libopencv_features2d.so
camcv_vid0: /usr/local/lib/libopencv_flann.so
camcv_vid0: /usr/local/lib/libopencv_gpu.so
camcv_vid0: /usr/local/lib/libopencv_highgui.so
camcv_vid0: /usr/local/lib/libopencv_imgproc.so
camcv_vid0: /usr/local/lib/libopencv_legacy.so
camcv_vid0: /usr/local/lib/libopencv_ml.so
camcv_vid0: /usr/local/lib/libopencv_nonfree.so
camcv_vid0: /usr/local/lib/libopencv_objdetect.so
camcv_vid0: /usr/local/lib/libopencv_photo.so
camcv_vid0: /usr/local/lib/libopencv_stitching.so
camcv_vid0: /usr/local/lib/libopencv_superres.so
camcv_vid0: /usr/local/lib/libopencv_ts.so
camcv_vid0: /usr/local/lib/libopencv_video.so
camcv_vid0: /usr/local/lib/libopencv_videostab.so
camcv_vid0: CMakeFiles/camcv_vid0.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable camcv_vid0"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/camcv_vid0.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/camcv_vid0.dir/build: camcv_vid0
.PHONY : CMakeFiles/camcv_vid0.dir/build

CMakeFiles/camcv_vid0.dir/requires: CMakeFiles/camcv_vid0.dir/RaspiCamControl.c.o.requires
CMakeFiles/camcv_vid0.dir/requires: CMakeFiles/camcv_vid0.dir/RaspiCLI.c.o.requires
CMakeFiles/camcv_vid0.dir/requires: CMakeFiles/camcv_vid0.dir/RaspiPreview.c.o.requires
CMakeFiles/camcv_vid0.dir/requires: CMakeFiles/camcv_vid0.dir/camcv_vid0.c.o.requires
.PHONY : CMakeFiles/camcv_vid0.dir/requires

CMakeFiles/camcv_vid0.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/camcv_vid0.dir/cmake_clean.cmake
.PHONY : CMakeFiles/camcv_vid0.dir/clean

CMakeFiles/camcv_vid0.dir/depend:
	cd /home/pi/camcv && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/camcv /home/pi/camcv /home/pi/camcv /home/pi/camcv /home/pi/camcv/CMakeFiles/camcv_vid0.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/camcv_vid0.dir/depend

