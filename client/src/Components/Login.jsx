import React, { useState } from 'react';
import './css/Login.css'
// import { useDispatch } from 'react-redux';
// import { login } from '../features/userSlice';
import { useAuth } from "../authcontext";
import { useNavigate } from "react-router-dom";


const Login = () => {
    const  [username, setUsername] = useState("");
    const  [email, setEmail] = useState("");
    const  [password, setPassword] = useState("");
    const { login } = useAuth()
    const navigate = useNavigate()

async function onSubmit (values) {
    console.log(values)
    login()
    navigate('/dashboard')
}

    // const dispatch = useDispatch();

    const handleSubmit = (e) => {
        e.preventDefault();

    //     dispatch(
    //         login({
    //         username: username,
    //         email:email,
    //         password:password,
    //         loggedIn:true,
    //     })
    // )
    }


  return (
    <div className='login'>
        <form className='login_form' onSubmit={(e) => handleSubmit(e)}>
        <h1>Login</h1>
        <input
            type='username'
            placeholder='Username'
            value={username}
            onChange={(e) => setUsername=(e.target.value)}
        />
        <input
            type='email'
            placeholder='Email'
            value={email}
            onChange={(e) => setEmail=(e.target.value)}
        />
        <input
            type='password'
            placeholder='Password'
            value={password}
            onChange={(e) => setPassword=(e.target.value)}
        />
        <button type='submit' className='submit_btn'>Submit</button> 
        </form>
    </div>
  );
};

export default Login
