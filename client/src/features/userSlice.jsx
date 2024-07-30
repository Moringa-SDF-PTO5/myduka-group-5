import { createSlice } from '@reduxjs/toolkit'

export const userSlice = createSlice({
    name: 'user',
    initialState: {
        // TODO: Reset when login functionality is connected to backend
        // user: null 
        user: {
            userName: 'Frasia',
            role: 'admin',
            email: 'frasia.nyakundi@student.moringaschool.com'
        }
    },
    reducers: {
        login: (state, action) => {
            state.user = action.payload;
        },
        logout: (state) => {
            state.user = null
        }
    }
})

export const {login, logout} = userSlice.actions

export const selectUser = (state) => state.user.user 

export default userSlice.reducer;