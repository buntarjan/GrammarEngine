/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.40
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package jni;

public class TokenLink {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  protected TokenLink(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(TokenLink obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        desrJNI.delete_TokenLink(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public TokenLink(int head, String label) {
    this(desrJNI.new_TokenLink__SWIG_0(head, label), true);
  }

  public TokenLink(int head) {
    this(desrJNI.new_TokenLink__SWIG_1(head), true);
  }

  public TokenLink() {
    this(desrJNI.new_TokenLink__SWIG_2(), true);
  }

  public void setHead(int value) {
    desrJNI.TokenLink_head_set(swigCPtr, this, value);
  }

  public int getHead() {
    return desrJNI.TokenLink_head_get(swigCPtr, this);
  }

  public void setLabel(String value) {
    desrJNI.TokenLink_label_set(swigCPtr, this, value);
  }

  public String getLabel() {
    return desrJNI.TokenLink_label_get(swigCPtr, this);
  }

}
