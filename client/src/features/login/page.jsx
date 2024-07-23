import React from "react";
import {useForm} from 'react-hook-form'
import {useNavigate} from 'react-router-dom'
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

const LoginPage = () => {
  const { register, handleSubmit,formState:{errors,isSubmitting} } = useForm();
  const navigate = useNavigate()
 
  function onSubmit(values){
    // TODO LOGIN FROM BACKEND
    console.log(values)
    navigate('/dashboard')
  }


  return (
    <main className="h-full flex items-center justify-center">
      <div className="max-w-xl w-full shadow-md rounded-md p-4">
        <h1 className="text-2xl font-medium text-center">Login to continue</h1>
        <form onSubmit={handleSubmit(onSubmit)} className="mt-6 space-y-4">
          <TextField
            size="small"
            type="email"
            id="outlined-basic"
            label="Email"
            variant="outlined"
            fullWidth
            error={!!errors.email}
            {...register('email',{required: 'Email is required.',pattern: {
              value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
              message: 'Invalid email address'
            }})}
            helperText={errors.email && errors.email.message}
          />
          <TextField
            size="small"
            type="password"
            id="password"
            label="Password"
            variant="outlined"
            fullWidth
            error={!!errors.password}
            helperText={errors.password && errors.password.message}
            {...register('password',{required: 'Password is required.',min: {value: 6, message: 'Password has to be six characters or more.'}})}
          />
          <Button disabled={isSubmitting} type='submit' fullWidth variant='contained'>{isSubmitting ? 'Please wait...' : 'Login'}</Button>
        </form>
      </div>
    </main>
  );
};

export default LoginPage;
