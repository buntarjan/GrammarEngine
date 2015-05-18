# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_desr', [dirname(__file__)])
        except ImportError:
            import _desr
            return _desr
        if fp is not None:
            try:
                _mod = imp.load_module('_desr', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _desr = swig_import_helper()
    del swig_import_helper
else:
    import _desr
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _desr.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _desr.SwigPyIterator_value(self)
    def incr(self, n = 1): return _desr.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _desr.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _desr.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _desr.SwigPyIterator_equal(self, *args)
    def copy(self): return _desr.SwigPyIterator_copy(self)
    def next(self): return _desr.SwigPyIterator_next(self)
    def __next__(self): return _desr.SwigPyIterator___next__(self)
    def previous(self): return _desr.SwigPyIterator_previous(self)
    def advance(self, *args): return _desr.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _desr.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _desr.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _desr.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _desr.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _desr.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _desr.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _desr.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class ios_base(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ios_base, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ios_base, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    erase_event = _desr.ios_base_erase_event
    imbue_event = _desr.ios_base_imbue_event
    copyfmt_event = _desr.ios_base_copyfmt_event
    def register_callback(self, *args): return _desr.ios_base_register_callback(self, *args)
    def flags(self, *args): return _desr.ios_base_flags(self, *args)
    def setf(self, *args): return _desr.ios_base_setf(self, *args)
    def unsetf(self, *args): return _desr.ios_base_unsetf(self, *args)
    def precision(self, *args): return _desr.ios_base_precision(self, *args)
    def width(self, *args): return _desr.ios_base_width(self, *args)
    __swig_getmethods__["sync_with_stdio"] = lambda x: _desr.ios_base_sync_with_stdio
    if _newclass:sync_with_stdio = staticmethod(_desr.ios_base_sync_with_stdio)
    def imbue(self, *args): return _desr.ios_base_imbue(self, *args)
    def getloc(self): return _desr.ios_base_getloc(self)
    __swig_getmethods__["xalloc"] = lambda x: _desr.ios_base_xalloc
    if _newclass:xalloc = staticmethod(_desr.ios_base_xalloc)
    def iword(self, *args): return _desr.ios_base_iword(self, *args)
    def pword(self, *args): return _desr.ios_base_pword(self, *args)
    __swig_destroy__ = _desr.delete_ios_base
    __del__ = lambda self : None;
ios_base_swigregister = _desr.ios_base_swigregister
ios_base_swigregister(ios_base)
cvar = _desr.cvar
ios_base.boolalpha = _desr.cvar.ios_base_boolalpha
ios_base.dec = _desr.cvar.ios_base_dec
ios_base.fixed = _desr.cvar.ios_base_fixed
ios_base.hex = _desr.cvar.ios_base_hex
ios_base.internal = _desr.cvar.ios_base_internal
ios_base.left = _desr.cvar.ios_base_left
ios_base.oct = _desr.cvar.ios_base_oct
ios_base.right = _desr.cvar.ios_base_right
ios_base.scientific = _desr.cvar.ios_base_scientific
ios_base.showbase = _desr.cvar.ios_base_showbase
ios_base.showpoint = _desr.cvar.ios_base_showpoint
ios_base.showpos = _desr.cvar.ios_base_showpos
ios_base.skipws = _desr.cvar.ios_base_skipws
ios_base.unitbuf = _desr.cvar.ios_base_unitbuf
ios_base.uppercase = _desr.cvar.ios_base_uppercase
ios_base.adjustfield = _desr.cvar.ios_base_adjustfield
ios_base.basefield = _desr.cvar.ios_base_basefield
ios_base.floatfield = _desr.cvar.ios_base_floatfield
ios_base.badbit = _desr.cvar.ios_base_badbit
ios_base.eofbit = _desr.cvar.ios_base_eofbit
ios_base.failbit = _desr.cvar.ios_base_failbit
ios_base.goodbit = _desr.cvar.ios_base_goodbit
ios_base.app = _desr.cvar.ios_base_app
ios_base.ate = _desr.cvar.ios_base_ate
ios_base.binary = _desr.cvar.ios_base_binary
ios_base.ios_base_in = _desr.cvar.ios_base_ios_base_in
ios_base.out = _desr.cvar.ios_base_out
ios_base.trunc = _desr.cvar.ios_base_trunc
ios_base.beg = _desr.cvar.ios_base_beg
ios_base.cur = _desr.cvar.ios_base_cur
ios_base.end = _desr.cvar.ios_base_end

def ios_base_sync_with_stdio(__sync = True):
  return _desr.ios_base_sync_with_stdio(__sync)
ios_base_sync_with_stdio = _desr.ios_base_sync_with_stdio

def ios_base_xalloc():
  return _desr.ios_base_xalloc()
ios_base_xalloc = _desr.ios_base_xalloc

class ios(ios_base):
    __swig_setmethods__ = {}
    for _s in [ios_base]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ios, name, value)
    __swig_getmethods__ = {}
    for _s in [ios_base]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ios, name)
    __repr__ = _swig_repr
    def rdstate(self): return _desr.ios_rdstate(self)
    def clear(self, *args): return _desr.ios_clear(self, *args)
    def setstate(self, *args): return _desr.ios_setstate(self, *args)
    def good(self): return _desr.ios_good(self)
    def eof(self): return _desr.ios_eof(self)
    def fail(self): return _desr.ios_fail(self)
    def bad(self): return _desr.ios_bad(self)
    def exceptions(self, *args): return _desr.ios_exceptions(self, *args)
    def __init__(self, *args): 
        this = _desr.new_ios(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_ios
    __del__ = lambda self : None;
    def tie(self, *args): return _desr.ios_tie(self, *args)
    def rdbuf(self, *args): return _desr.ios_rdbuf(self, *args)
    def copyfmt(self, *args): return _desr.ios_copyfmt(self, *args)
    def fill(self, *args): return _desr.ios_fill(self, *args)
    def imbue(self, *args): return _desr.ios_imbue(self, *args)
    def narrow(self, *args): return _desr.ios_narrow(self, *args)
    def widen(self, *args): return _desr.ios_widen(self, *args)
ios_swigregister = _desr.ios_swigregister
ios_swigregister(ios)

class ostream(ios):
    __swig_setmethods__ = {}
    for _s in [ios]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ostream, name, value)
    __swig_getmethods__ = {}
    for _s in [ios]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ostream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_ostream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_ostream
    __del__ = lambda self : None;
    def __lshift__(self, *args): return _desr.ostream___lshift__(self, *args)
    def put(self, *args): return _desr.ostream_put(self, *args)
    def write(self, *args): return _desr.ostream_write(self, *args)
    def flush(self): return _desr.ostream_flush(self)
    def tellp(self): return _desr.ostream_tellp(self)
    def seekp(self, *args): return _desr.ostream_seekp(self, *args)
ostream_swigregister = _desr.ostream_swigregister
ostream_swigregister(ostream)
cin = cvar.cin
cout = cvar.cout
cerr = cvar.cerr
clog = cvar.clog

class istream(ios):
    __swig_setmethods__ = {}
    for _s in [ios]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, istream, name, value)
    __swig_getmethods__ = {}
    for _s in [ios]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, istream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_istream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_istream
    __del__ = lambda self : None;
    def __rshift__(self, *args): return _desr.istream___rshift__(self, *args)
    def gcount(self): return _desr.istream_gcount(self)
    def get(self, *args): return _desr.istream_get(self, *args)
    def getline(self, *args): return _desr.istream_getline(self, *args)
    def ignore(self, *args): return _desr.istream_ignore(self, *args)
    def peek(self): return _desr.istream_peek(self)
    def read(self, *args): return _desr.istream_read(self, *args)
    def readsome(self, *args): return _desr.istream_readsome(self, *args)
    def putback(self, *args): return _desr.istream_putback(self, *args)
    def unget(self): return _desr.istream_unget(self)
    def sync(self): return _desr.istream_sync(self)
    def tellg(self): return _desr.istream_tellg(self)
    def seekg(self, *args): return _desr.istream_seekg(self, *args)
istream_swigregister = _desr.istream_swigregister
istream_swigregister(istream)

class iostream(istream,ostream):
    __swig_setmethods__ = {}
    for _s in [istream,ostream]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, iostream, name, value)
    __swig_getmethods__ = {}
    for _s in [istream,ostream]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, iostream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_iostream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_iostream
    __del__ = lambda self : None;
iostream_swigregister = _desr.iostream_swigregister
iostream_swigregister(iostream)

endl_cb_ptr = _desr.endl_cb_ptr

def endl(*args):
  return _desr.endl(*args)
endl = _desr.endl
ends_cb_ptr = _desr.ends_cb_ptr

def ends(*args):
  return _desr.ends(*args)
ends = _desr.ends
flush_cb_ptr = _desr.flush_cb_ptr

def flush(*args):
  return _desr.flush(*args)
flush = _desr.flush
class ifstream(istream):
    __swig_setmethods__ = {}
    for _s in [istream]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ifstream, name, value)
    __swig_getmethods__ = {}
    for _s in [istream]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ifstream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_ifstream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_ifstream
    __del__ = lambda self : None;
ifstream_swigregister = _desr.ifstream_swigregister
ifstream_swigregister(ifstream)

class ofstream(istream):
    __swig_setmethods__ = {}
    for _s in [istream]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ofstream, name, value)
    __swig_getmethods__ = {}
    for _s in [istream]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ofstream, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_ofstream(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_ofstream
    __del__ = lambda self : None;
ofstream_swigregister = _desr.ofstream_swigregister
ofstream_swigregister(ofstream)

class Disposable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Disposable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Disposable, name)
    __repr__ = _swig_repr
    def Dispose(self): return _desr.Disposable_Dispose(self)
    def __init__(self): 
        this = _desr.new_Disposable()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_Disposable
    __del__ = lambda self : None;
Disposable_swigregister = _desr.Disposable_swigregister
Disposable_swigregister(Disposable)

class RefCountable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RefCountable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RefCountable, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _desr.new_RefCountable()
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["refCount"] = _desr.RefCountable_refCount_set
    __swig_getmethods__["refCount"] = _desr.RefCountable_refCount_get
    if _newclass:refCount = _swig_property(_desr.RefCountable_refCount_get, _desr.RefCountable_refCount_set)
    def incRef(self): return _desr.RefCountable_incRef(self)
    def decRef(self): return _desr.RefCountable_decRef(self)
    __swig_destroy__ = _desr.delete_RefCountable
    __del__ = lambda self : None;
RefCountable_swigregister = _desr.RefCountable_swigregister
RefCountable_swigregister(RefCountable)

class VectorToken(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorToken, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorToken, name)
    def iterator(self): return _desr.VectorToken_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _desr.VectorToken___nonzero__(self)
    def __bool__(self): return _desr.VectorToken___bool__(self)
    def __len__(self): return _desr.VectorToken___len__(self)
    def pop(self): return _desr.VectorToken_pop(self)
    def __getslice__(self, *args): return _desr.VectorToken___getslice__(self, *args)
    def __setslice__(self, *args): return _desr.VectorToken___setslice__(self, *args)
    def __delslice__(self, *args): return _desr.VectorToken___delslice__(self, *args)
    def __delitem__(self, *args): return _desr.VectorToken___delitem__(self, *args)
    def __getitem__(self, *args): return _desr.VectorToken___getitem__(self, *args)
    def __setitem__(self, *args): return _desr.VectorToken___setitem__(self, *args)
    def append(self, *args): return _desr.VectorToken_append(self, *args)
    def empty(self): return _desr.VectorToken_empty(self)
    def size(self): return _desr.VectorToken_size(self)
    def clear(self): return _desr.VectorToken_clear(self)
    def swap(self, *args): return _desr.VectorToken_swap(self, *args)
    def get_allocator(self): return _desr.VectorToken_get_allocator(self)
    def begin(self): return _desr.VectorToken_begin(self)
    def end(self): return _desr.VectorToken_end(self)
    def rbegin(self): return _desr.VectorToken_rbegin(self)
    def rend(self): return _desr.VectorToken_rend(self)
    def pop_back(self): return _desr.VectorToken_pop_back(self)
    def erase(self, *args): return _desr.VectorToken_erase(self, *args)
    def __init__(self, *args): 
        this = _desr.new_VectorToken(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _desr.VectorToken_push_back(self, *args)
    def front(self): return _desr.VectorToken_front(self)
    def back(self): return _desr.VectorToken_back(self)
    def assign(self, *args): return _desr.VectorToken_assign(self, *args)
    def resize(self, *args): return _desr.VectorToken_resize(self, *args)
    def insert(self, *args): return _desr.VectorToken_insert(self, *args)
    def reserve(self, *args): return _desr.VectorToken_reserve(self, *args)
    def capacity(self): return _desr.VectorToken_capacity(self)
    def __repr__(self): return _desr.VectorToken___repr__(self)
    __swig_destroy__ = _desr.delete_VectorToken
    __del__ = lambda self : None;
VectorToken_swigregister = _desr.VectorToken_swigregister
VectorToken_swigregister(VectorToken)

class AttributeIndex(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttributeIndex, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttributeIndex, name)
    __repr__ = _swig_repr
    def insert(self, *args): return _desr.AttributeIndex_insert(self, *args)
    __swig_setmethods__["names"] = _desr.AttributeIndex_names_set
    __swig_getmethods__["names"] = _desr.AttributeIndex_names_get
    if _newclass:names = _swig_property(_desr.AttributeIndex_names_get, _desr.AttributeIndex_names_set)
    def __init__(self): 
        this = _desr.new_AttributeIndex()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_AttributeIndex
    __del__ = lambda self : None;
AttributeIndex_swigregister = _desr.AttributeIndex_swigregister
AttributeIndex_swigregister(AttributeIndex)

class Language(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Language, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Language, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_Language(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _desr.delete_Language
    __del__ = lambda self : None;
Language_swigregister = _desr.Language_swigregister
Language_swigregister(Language)

class Corpus(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Corpus, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Corpus, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_Corpus(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_getmethods__["create"] = lambda x: _desr.Corpus_create
    if _newclass:create = staticmethod(_desr.Corpus_create)
    def sentenceReader(self, *args): return _desr.Corpus_sentenceReader(self, *args)
    def toString(self, *args): return _desr.Corpus_toString(self, *args)
    __swig_setmethods__["index"] = _desr.Corpus_index_set
    __swig_getmethods__["index"] = _desr.Corpus_index_get
    if _newclass:index = _swig_property(_desr.Corpus_index_get, _desr.Corpus_index_set)
    __swig_destroy__ = _desr.delete_Corpus
    __del__ = lambda self : None;
Corpus_swigregister = _desr.Corpus_swigregister
Corpus_swigregister(Corpus)

def Corpus_create(*args):
  return _desr.Corpus_create(*args)
Corpus_create = _desr.Corpus_create

class Attributes(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Attributes, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Attributes, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_Attributes(*args)
        try: self.this.append(this)
        except: self.this = this
    def get(self, *args): return _desr.Attributes_get(self, *args)
    def index(self, *args): return _desr.Attributes_index(self, *args)
    def insert(self, *args): return _desr.Attributes_insert(self, *args)
    __swig_destroy__ = _desr.delete_Attributes
    __del__ = lambda self : None;
Attributes_swigregister = _desr.Attributes_swigregister
Attributes_swigregister(Attributes)

class TokenLink(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TokenLink, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TokenLink, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_TokenLink(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["head"] = _desr.TokenLink_head_set
    __swig_getmethods__["head"] = _desr.TokenLink_head_get
    if _newclass:head = _swig_property(_desr.TokenLink_head_get, _desr.TokenLink_head_set)
    __swig_setmethods__["label"] = _desr.TokenLink_label_set
    __swig_getmethods__["label"] = _desr.TokenLink_label_get
    if _newclass:label = _swig_property(_desr.TokenLink_label_get, _desr.TokenLink_label_set)
    __swig_destroy__ = _desr.delete_TokenLink
    __del__ = lambda self : None;
TokenLink_swigregister = _desr.TokenLink_swigregister
TokenLink_swigregister(TokenLink)

class Tag(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tag, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tag, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_Tag(*args)
        try: self.this.append(this)
        except: self.this = this
    def open(self): return _desr.Tag_open(self)
    def close(self): return _desr.Tag_close(self)
    __swig_setmethods__["name"] = _desr.Tag_name_set
    __swig_getmethods__["name"] = _desr.Tag_name_get
    if _newclass:name = _swig_property(_desr.Tag_name_get, _desr.Tag_name_set)
    def __getitem__(self, *args): return _desr.Tag___getitem__(self, *args)
    def __setitem__(self, *args): return _desr.Tag___setitem__(self, *args)
    __swig_destroy__ = _desr.delete_Tag
    __del__ = lambda self : None;
Tag_swigregister = _desr.Tag_swigregister
Tag_swigregister(Tag)

class Context(RefCountable):
    __swig_setmethods__ = {}
    for _s in [RefCountable]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Context, name, value)
    __swig_getmethods__ = {}
    for _s in [RefCountable]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Context, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_Context(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["tag"] = _desr.Context_tag_set
    __swig_getmethods__["tag"] = _desr.Context_tag_get
    if _newclass:tag = _swig_property(_desr.Context_tag_get, _desr.Context_tag_set)
    __swig_setmethods__["parent"] = _desr.Context_parent_set
    __swig_getmethods__["parent"] = _desr.Context_parent_get
    if _newclass:parent = _swig_property(_desr.Context_parent_get, _desr.Context_parent_set)
    def __eq__(self, *args): return _desr.Context___eq__(self, *args)
    def __ne__(self, *args): return _desr.Context___ne__(self, *args)
    __swig_destroy__ = _desr.delete_Context
    __del__ = lambda self : None;
Context_swigregister = _desr.Context_swigregister
Context_swigregister(Context)

class Token(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Token, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Token, name)
    def __init__(self, *args): 
        this = _desr.new_Token(*args)
        try: self.this.append(this)
        except: self.this = this
    def attrIndex(self, *args): return _desr.Token_attrIndex(self, *args)
    __swig_setmethods__["form"] = _desr.Token_form_set
    __swig_getmethods__["form"] = _desr.Token_form_get
    if _newclass:form = _swig_property(_desr.Token_form_get, _desr.Token_form_set)
    __swig_setmethods__["attributes"] = _desr.Token_attributes_set
    __swig_getmethods__["attributes"] = _desr.Token_attributes_get
    if _newclass:attributes = _swig_property(_desr.Token_attributes_get, _desr.Token_attributes_set)
    __swig_setmethods__["links"] = _desr.Token_links_set
    __swig_getmethods__["links"] = _desr.Token_links_get
    if _newclass:links = _swig_property(_desr.Token_links_get, _desr.Token_links_set)
    def context(self): return _desr.Token_context(self)
    def __repr__(self): return _desr.Token___repr__(self)
    def __setitem__(self, *args): return _desr.Token___setitem__(self, *args)
    def __getitem__(self, *args): return _desr.Token___getitem__(self, *args)
    __swig_destroy__ = _desr.delete_Token
    __del__ = lambda self : None;
Token_swigregister = _desr.Token_swigregister
Token_swigregister(Token)

class TreeToken(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TreeToken, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TreeToken, name)
    def __init__(self, *args): 
        this = _desr.new_TreeToken(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["token"] = _desr.TreeToken_token_set
    __swig_getmethods__["token"] = _desr.TreeToken_token_get
    if _newclass:token = _swig_property(_desr.TreeToken_token_get, _desr.TreeToken_token_set)
    __swig_setmethods__["id"] = _desr.TreeToken_id_set
    __swig_getmethods__["id"] = _desr.TreeToken_id_get
    if _newclass:id = _swig_property(_desr.TreeToken_id_get, _desr.TreeToken_id_set)
    __swig_setmethods__["left"] = _desr.TreeToken_left_set
    __swig_getmethods__["left"] = _desr.TreeToken_left_get
    if _newclass:left = _swig_property(_desr.TreeToken_left_get, _desr.TreeToken_left_set)
    __swig_setmethods__["right"] = _desr.TreeToken_right_set
    __swig_getmethods__["right"] = _desr.TreeToken_right_get
    if _newclass:right = _swig_property(_desr.TreeToken_right_get, _desr.TreeToken_right_set)
    def form(self): return _desr.TreeToken_form(self)
    def get(self, *args): return _desr.TreeToken_get(self, *args)
    def set(self, *args): return _desr.TreeToken_set(self, *args)
    def linkHead(self, i = 0): return _desr.TreeToken_linkHead(self, i)
    def linkLabel(self, i = 0): return _desr.TreeToken_linkLabel(self, i)
    def __repr__(self): return _desr.TreeToken___repr__(self)
    def __getitem__(self, *args): return _desr.TreeToken___getitem__(self, *args)
    __swig_destroy__ = _desr.delete_TreeToken
    __del__ = lambda self : None;
TreeToken_swigregister = _desr.TreeToken_swigregister
TreeToken_swigregister(TreeToken)

class VectorTreeToken(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorTreeToken, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorTreeToken, name)
    __repr__ = _swig_repr
    def iterator(self): return _desr.VectorTreeToken_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _desr.VectorTreeToken___nonzero__(self)
    def __bool__(self): return _desr.VectorTreeToken___bool__(self)
    def __len__(self): return _desr.VectorTreeToken___len__(self)
    def pop(self): return _desr.VectorTreeToken_pop(self)
    def __getslice__(self, *args): return _desr.VectorTreeToken___getslice__(self, *args)
    def __setslice__(self, *args): return _desr.VectorTreeToken___setslice__(self, *args)
    def __delslice__(self, *args): return _desr.VectorTreeToken___delslice__(self, *args)
    def __delitem__(self, *args): return _desr.VectorTreeToken___delitem__(self, *args)
    def __getitem__(self, *args): return _desr.VectorTreeToken___getitem__(self, *args)
    def __setitem__(self, *args): return _desr.VectorTreeToken___setitem__(self, *args)
    def append(self, *args): return _desr.VectorTreeToken_append(self, *args)
    def empty(self): return _desr.VectorTreeToken_empty(self)
    def size(self): return _desr.VectorTreeToken_size(self)
    def clear(self): return _desr.VectorTreeToken_clear(self)
    def swap(self, *args): return _desr.VectorTreeToken_swap(self, *args)
    def get_allocator(self): return _desr.VectorTreeToken_get_allocator(self)
    def begin(self): return _desr.VectorTreeToken_begin(self)
    def end(self): return _desr.VectorTreeToken_end(self)
    def rbegin(self): return _desr.VectorTreeToken_rbegin(self)
    def rend(self): return _desr.VectorTreeToken_rend(self)
    def pop_back(self): return _desr.VectorTreeToken_pop_back(self)
    def erase(self, *args): return _desr.VectorTreeToken_erase(self, *args)
    def __init__(self, *args): 
        this = _desr.new_VectorTreeToken(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _desr.VectorTreeToken_push_back(self, *args)
    def front(self): return _desr.VectorTreeToken_front(self)
    def back(self): return _desr.VectorTreeToken_back(self)
    def assign(self, *args): return _desr.VectorTreeToken_assign(self, *args)
    def resize(self, *args): return _desr.VectorTreeToken_resize(self, *args)
    def insert(self, *args): return _desr.VectorTreeToken_insert(self, *args)
    def reserve(self, *args): return _desr.VectorTreeToken_reserve(self, *args)
    def capacity(self): return _desr.VectorTreeToken_capacity(self)
    __swig_destroy__ = _desr.delete_VectorTreeToken
    __del__ = lambda self : None;
VectorTreeToken_swigregister = _desr.VectorTreeToken_swigregister
VectorTreeToken_swigregister(VectorTreeToken)

class EnumeratorSentence(Disposable):
    __swig_setmethods__ = {}
    for _s in [Disposable]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, EnumeratorSentence, name, value)
    __swig_getmethods__ = {}
    for _s in [Disposable]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, EnumeratorSentence, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def MoveNext(self): return _desr.EnumeratorSentence_MoveNext(self)
    def Current(self): return _desr.EnumeratorSentence_Current(self)
    def Reset(self): return _desr.EnumeratorSentence_Reset(self)
    __swig_destroy__ = _desr.delete_EnumeratorSentence
    __del__ = lambda self : None;
    def __iter__(self): return _desr.EnumeratorSentence___iter__(self)
    def next(self): return _desr.EnumeratorSentence_next(self)
EnumeratorSentence_swigregister = _desr.EnumeratorSentence_swigregister
EnumeratorSentence_swigregister(EnumeratorSentence)

class Sentence(VectorTreeToken):
    __swig_setmethods__ = {}
    for _s in [VectorTreeToken]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Sentence, name, value)
    __swig_getmethods__ = {}
    for _s in [VectorTreeToken]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Sentence, name)
    def __init__(self, language = None): 
        this = _desr.new_Sentence(language)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["language"] = _desr.Sentence_language_set
    __swig_getmethods__["language"] = _desr.Sentence_language_get
    if _newclass:language = _swig_property(_desr.Sentence_language_get, _desr.Sentence_language_set)
    def deref(self): return _desr.Sentence_deref(self)
    def __repr__(self): return _desr.Sentence___repr__(self)
    __swig_destroy__ = _desr.delete_Sentence
    __del__ = lambda self : None;
Sentence_swigregister = _desr.Sentence_swigregister
Sentence_swigregister(Sentence)

class SentenceReader(EnumeratorSentence):
    __swig_setmethods__ = {}
    for _s in [EnumeratorSentence]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SentenceReader, name, value)
    __swig_getmethods__ = {}
    for _s in [EnumeratorSentence]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SentenceReader, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _desr.new_SentenceReader(*args)
        try: self.this.append(this)
        except: self.this = this
    def MoveNext(self): return _desr.SentenceReader_MoveNext(self)
    def Current(self): return _desr.SentenceReader_Current(self)
    __swig_destroy__ = _desr.delete_SentenceReader
    __del__ = lambda self : None;
SentenceReader_swigregister = _desr.SentenceReader_swigregister
SentenceReader_swigregister(SentenceReader)

class Parser(RefCountable):
    __swig_setmethods__ = {}
    for _s in [RefCountable]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Parser, name, value)
    __swig_getmethods__ = {}
    for _s in [RefCountable]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Parser, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["create"] = lambda x: _desr.Parser_create
    if _newclass:create = staticmethod(_desr.Parser_create)
    def pipe(self, *args): return _desr.Parser_pipe(self, *args)
    def parse(self, *args): return _desr.Parser_parse(self, *args)
    def showPerplexity(self): return _desr.Parser_showPerplexity(self)
    __swig_destroy__ = _desr.delete_Parser
    __del__ = lambda self : None;
Parser_swigregister = _desr.Parser_swigregister
Parser_swigregister(Parser)

def Parser_create(*args):
  return _desr.Parser_create(*args)
Parser_create = _desr.Parser_create

# This file is compatible with both classic and new-style classes.


