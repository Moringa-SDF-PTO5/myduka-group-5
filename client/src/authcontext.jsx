import { createContext, useContext, useState } from "react";

const AuthContext = createContext()

export const AuthProvider = ({children}) => {
    const [isLoggedIn,setIsLoggedIn] =  useState(false)
    function login() {
        setIsLoggedIn(true)
    }
    function logout() {
        setIsLoggedIn(false)
    }

    return <AuthContext.Provider value={{isLoggedIn, login, logout}}>{children}</AuthContext.Provider>

}

export const useAuth = () => {
    return useContext(AuthContext)
}