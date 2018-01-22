# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_misc_swig', [dirname(__file__)])
        except ImportError:
            import _misc_swig
            return _misc_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_misc_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _misc_swig = swig_import_helper()
    del swig_import_helper
else:
    import _misc_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _misc_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _misc_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _misc_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _misc_swig.high_res_timer_epoch()
class preamble_detector(object):
    """Proxy of C++ gr::misc::preamble_detector class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(data, preamble_length, message_lenght):
        """make(unsigned char * data, int preamble_length, int message_lenght) -> preamble_detector_sptr"""
        return _misc_swig.preamble_detector_make(data, preamble_length, message_lenght)

    make = staticmethod(make)
    __swig_destroy__ = _misc_swig.delete_preamble_detector
    __del__ = lambda self: None
preamble_detector_swigregister = _misc_swig.preamble_detector_swigregister
preamble_detector_swigregister(preamble_detector)

def preamble_detector_make(data, preamble_length, message_lenght):
    """preamble_detector_make(unsigned char * data, int preamble_length, int message_lenght) -> preamble_detector_sptr"""
    return _misc_swig.preamble_detector_make(data, preamble_length, message_lenght)

class preamble_detector_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::misc::preamble_detector)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::misc::preamble_detector)> self) -> preamble_detector_sptr
        __init__(boost::shared_ptr<(gr::misc::preamble_detector)> self, preamble_detector p) -> preamble_detector_sptr
        """
        this = _misc_swig.new_preamble_detector_sptr(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __deref__(self):
        """__deref__(preamble_detector_sptr self) -> preamble_detector"""
        return _misc_swig.preamble_detector_sptr___deref__(self)

    __swig_destroy__ = _misc_swig.delete_preamble_detector_sptr
    __del__ = lambda self: None

    def make(self, data, preamble_length, message_lenght):
        """make(preamble_detector_sptr self, unsigned char * data, int preamble_length, int message_lenght) -> preamble_detector_sptr"""
        return _misc_swig.preamble_detector_sptr_make(self, data, preamble_length, message_lenght)


    def history(self):
        """history(preamble_detector_sptr self) -> unsigned int"""
        return _misc_swig.preamble_detector_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(preamble_detector_sptr self, int which, int delay)
        declare_sample_delay(preamble_detector_sptr self, unsigned int delay)
        """
        return _misc_swig.preamble_detector_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(preamble_detector_sptr self, int which) -> unsigned int"""
        return _misc_swig.preamble_detector_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(preamble_detector_sptr self) -> int"""
        return _misc_swig.preamble_detector_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(preamble_detector_sptr self) -> double"""
        return _misc_swig.preamble_detector_sptr_relative_rate(self)


    def start(self):
        """start(preamble_detector_sptr self) -> bool"""
        return _misc_swig.preamble_detector_sptr_start(self)


    def stop(self):
        """stop(preamble_detector_sptr self) -> bool"""
        return _misc_swig.preamble_detector_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(preamble_detector_sptr self, unsigned int which_input) -> uint64_t"""
        return _misc_swig.preamble_detector_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(preamble_detector_sptr self, unsigned int which_output) -> uint64_t"""
        return _misc_swig.preamble_detector_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(preamble_detector_sptr self) -> int"""
        return _misc_swig.preamble_detector_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(preamble_detector_sptr self, int m)"""
        return _misc_swig.preamble_detector_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(preamble_detector_sptr self)"""
        return _misc_swig.preamble_detector_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(preamble_detector_sptr self) -> bool"""
        return _misc_swig.preamble_detector_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(preamble_detector_sptr self, int m)"""
        return _misc_swig.preamble_detector_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(preamble_detector_sptr self) -> int"""
        return _misc_swig.preamble_detector_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(preamble_detector_sptr self, int i) -> long"""
        return _misc_swig.preamble_detector_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(preamble_detector_sptr self, long max_output_buffer)
        set_max_output_buffer(preamble_detector_sptr self, int port, long max_output_buffer)
        """
        return _misc_swig.preamble_detector_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(preamble_detector_sptr self, int i) -> long"""
        return _misc_swig.preamble_detector_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(preamble_detector_sptr self, long min_output_buffer)
        set_min_output_buffer(preamble_detector_sptr self, int port, long min_output_buffer)
        """
        return _misc_swig.preamble_detector_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(preamble_detector_sptr self, int which) -> float
        pc_input_buffers_full(preamble_detector_sptr self) -> pmt_vector_float
        """
        return _misc_swig.preamble_detector_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(preamble_detector_sptr self, int which) -> float
        pc_input_buffers_full_avg(preamble_detector_sptr self) -> pmt_vector_float
        """
        return _misc_swig.preamble_detector_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(preamble_detector_sptr self, int which) -> float
        pc_input_buffers_full_var(preamble_detector_sptr self) -> pmt_vector_float
        """
        return _misc_swig.preamble_detector_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(preamble_detector_sptr self, int which) -> float
        pc_output_buffers_full(preamble_detector_sptr self) -> pmt_vector_float
        """
        return _misc_swig.preamble_detector_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(preamble_detector_sptr self, int which) -> float
        pc_output_buffers_full_avg(preamble_detector_sptr self) -> pmt_vector_float
        """
        return _misc_swig.preamble_detector_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(preamble_detector_sptr self, int which) -> float
        pc_output_buffers_full_var(preamble_detector_sptr self) -> pmt_vector_float
        """
        return _misc_swig.preamble_detector_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(preamble_detector_sptr self) -> float"""
        return _misc_swig.preamble_detector_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(preamble_detector_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _misc_swig.preamble_detector_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(preamble_detector_sptr self)"""
        return _misc_swig.preamble_detector_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(preamble_detector_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _misc_swig.preamble_detector_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(preamble_detector_sptr self) -> int"""
        return _misc_swig.preamble_detector_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(preamble_detector_sptr self) -> int"""
        return _misc_swig.preamble_detector_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(preamble_detector_sptr self, int priority) -> int"""
        return _misc_swig.preamble_detector_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(preamble_detector_sptr self) -> std::string"""
        return _misc_swig.preamble_detector_sptr_name(self)


    def symbol_name(self):
        """symbol_name(preamble_detector_sptr self) -> std::string"""
        return _misc_swig.preamble_detector_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(preamble_detector_sptr self) -> io_signature_sptr"""
        return _misc_swig.preamble_detector_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(preamble_detector_sptr self) -> io_signature_sptr"""
        return _misc_swig.preamble_detector_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(preamble_detector_sptr self) -> long"""
        return _misc_swig.preamble_detector_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(preamble_detector_sptr self) -> basic_block_sptr"""
        return _misc_swig.preamble_detector_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(preamble_detector_sptr self, int ninputs, int noutputs) -> bool"""
        return _misc_swig.preamble_detector_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(preamble_detector_sptr self) -> std::string"""
        return _misc_swig.preamble_detector_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(preamble_detector_sptr self, std::string name)"""
        return _misc_swig.preamble_detector_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(preamble_detector_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _misc_swig.preamble_detector_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(preamble_detector_sptr self) -> swig_int_ptr"""
        return _misc_swig.preamble_detector_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(preamble_detector_sptr self) -> swig_int_ptr"""
        return _misc_swig.preamble_detector_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(preamble_detector_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _misc_swig.preamble_detector_sptr_message_subscribers(self, which_port)

preamble_detector_sptr_swigregister = _misc_swig.preamble_detector_sptr_swigregister
preamble_detector_sptr_swigregister(preamble_detector_sptr)


preamble_detector_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
preamble_detector = preamble_detector.make;


