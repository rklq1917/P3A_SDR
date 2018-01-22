/* -*- c++ -*- */

#define MISC_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "misc_swig_doc.i"

%{
#include "misc/preamble_detector.h"
%}


%include "misc/preamble_detector.h"
GR_SWIG_BLOCK_MAGIC2(misc, preamble_detector);
