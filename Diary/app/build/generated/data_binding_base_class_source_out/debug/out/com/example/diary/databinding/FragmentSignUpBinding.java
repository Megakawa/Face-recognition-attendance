// Generated by view binder compiler. Do not edit!
package com.example.diary.databinding;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.viewbinding.ViewBinding;
import androidx.viewbinding.ViewBindings;
import com.example.diary.R;
import java.lang.NullPointerException;
import java.lang.Override;
import java.lang.String;

public final class FragmentSignUpBinding implements ViewBinding {
  @NonNull
  private final FrameLayout rootView;

  @NonNull
  public final TextView Login;

  @NonNull
  public final TextView Warning;

  @NonNull
  public final Button btSignUp;

  @NonNull
  public final EditText etPass;

  @NonNull
  public final EditText etRepass;

  @NonNull
  public final EditText etUser;

  private FragmentSignUpBinding(@NonNull FrameLayout rootView, @NonNull TextView Login,
      @NonNull TextView Warning, @NonNull Button btSignUp, @NonNull EditText etPass,
      @NonNull EditText etRepass, @NonNull EditText etUser) {
    this.rootView = rootView;
    this.Login = Login;
    this.Warning = Warning;
    this.btSignUp = btSignUp;
    this.etPass = etPass;
    this.etRepass = etRepass;
    this.etUser = etUser;
  }

  @Override
  @NonNull
  public FrameLayout getRoot() {
    return rootView;
  }

  @NonNull
  public static FragmentSignUpBinding inflate(@NonNull LayoutInflater inflater) {
    return inflate(inflater, null, false);
  }

  @NonNull
  public static FragmentSignUpBinding inflate(@NonNull LayoutInflater inflater,
      @Nullable ViewGroup parent, boolean attachToParent) {
    View root = inflater.inflate(R.layout.fragment_sign_up, parent, false);
    if (attachToParent) {
      parent.addView(root);
    }
    return bind(root);
  }

  @NonNull
  public static FragmentSignUpBinding bind(@NonNull View rootView) {
    // The body of this method is generated in a way you would not otherwise write.
    // This is done to optimize the compiled bytecode for size and performance.
    int id;
    missingId: {
      id = R.id.Login;
      TextView Login = ViewBindings.findChildViewById(rootView, id);
      if (Login == null) {
        break missingId;
      }

      id = R.id.Warning;
      TextView Warning = ViewBindings.findChildViewById(rootView, id);
      if (Warning == null) {
        break missingId;
      }

      id = R.id.bt_SignUp;
      Button btSignUp = ViewBindings.findChildViewById(rootView, id);
      if (btSignUp == null) {
        break missingId;
      }

      id = R.id.et_pass;
      EditText etPass = ViewBindings.findChildViewById(rootView, id);
      if (etPass == null) {
        break missingId;
      }

      id = R.id.et_repass;
      EditText etRepass = ViewBindings.findChildViewById(rootView, id);
      if (etRepass == null) {
        break missingId;
      }

      id = R.id.et_user;
      EditText etUser = ViewBindings.findChildViewById(rootView, id);
      if (etUser == null) {
        break missingId;
      }

      return new FragmentSignUpBinding((FrameLayout) rootView, Login, Warning, btSignUp, etPass,
          etRepass, etUser);
    }
    String missingId = rootView.getResources().getResourceName(id);
    throw new NullPointerException("Missing required view with ID: ".concat(missingId));
  }
}