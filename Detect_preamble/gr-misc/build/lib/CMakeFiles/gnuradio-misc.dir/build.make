# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


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

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/raphael/gr-misc

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/raphael/gr-misc/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/gnuradio-misc.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/gnuradio-misc.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/gnuradio-misc.dir/flags.make

lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o: lib/CMakeFiles/gnuradio-misc.dir/flags.make
lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o: ../lib/preamble_detector_impl.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raphael/gr-misc/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o"
	cd /home/raphael/gr-misc/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o -c /home/raphael/gr-misc/lib/preamble_detector_impl.cc

lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.i"
	cd /home/raphael/gr-misc/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raphael/gr-misc/lib/preamble_detector_impl.cc > CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.i

lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.s"
	cd /home/raphael/gr-misc/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raphael/gr-misc/lib/preamble_detector_impl.cc -o CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.s

lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.requires:

.PHONY : lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.requires

lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.provides: lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-misc.dir/build.make lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.provides

lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o


# Object files for target gnuradio-misc
gnuradio__misc_OBJECTS = \
"CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o"

# External object files for target gnuradio-misc
gnuradio__misc_EXTERNAL_OBJECTS =

lib/libgnuradio-misc.so: lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o
lib/libgnuradio-misc.so: lib/CMakeFiles/gnuradio-misc.dir/build.make
lib/libgnuradio-misc.so: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/libgnuradio-misc.so: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/libgnuradio-misc.so: /usr/lib/x86_64-linux-gnu/libgnuradio-runtime.so
lib/libgnuradio-misc.so: /usr/lib/x86_64-linux-gnu/libgnuradio-pmt.so
lib/libgnuradio-misc.so: lib/CMakeFiles/gnuradio-misc.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/raphael/gr-misc/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libgnuradio-misc.so"
	cd /home/raphael/gr-misc/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gnuradio-misc.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/gnuradio-misc.dir/build: lib/libgnuradio-misc.so

.PHONY : lib/CMakeFiles/gnuradio-misc.dir/build

lib/CMakeFiles/gnuradio-misc.dir/requires: lib/CMakeFiles/gnuradio-misc.dir/preamble_detector_impl.cc.o.requires

.PHONY : lib/CMakeFiles/gnuradio-misc.dir/requires

lib/CMakeFiles/gnuradio-misc.dir/clean:
	cd /home/raphael/gr-misc/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/gnuradio-misc.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/gnuradio-misc.dir/clean

lib/CMakeFiles/gnuradio-misc.dir/depend:
	cd /home/raphael/gr-misc/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/raphael/gr-misc /home/raphael/gr-misc/lib /home/raphael/gr-misc/build /home/raphael/gr-misc/build/lib /home/raphael/gr-misc/build/lib/CMakeFiles/gnuradio-misc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/gnuradio-misc.dir/depend

