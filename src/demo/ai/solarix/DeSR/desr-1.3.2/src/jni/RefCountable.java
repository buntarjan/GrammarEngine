/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.40
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package jni;

public class RefCountable {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  protected RefCountable(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(RefCountable obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        desrJNI.delete_RefCountable(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public RefCountable() {
    this(desrJNI.new_RefCountable(), true);
  }

  public void setRefCount(long value) {
    desrJNI.RefCountable_refCount_set(swigCPtr, this, value);
  }

  public long getRefCount() {
    return desrJNI.RefCountable_refCount_get(swigCPtr, this);
  }

  public long incRef() {
    return desrJNI.RefCountable_incRef(swigCPtr, this);
  }

  public long decRef() {
    return desrJNI.RefCountable_decRef(swigCPtr, this);
  }

}
