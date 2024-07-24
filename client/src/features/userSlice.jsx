import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

export const userSlice = createSlice({
    name: 'user',
    initialState: {
        // TODO: Reset when login functionality is connected to backend
        // user: null 
        user: {
            userName: 'Frasia',
            role: 'admin',
            email: 'frasia.nyakundi@student.moringaschool.com'
        },
        users: []
    },
    reducers: {
        login: (state, action) => {
            state.user = action.payload;
        },
        logout: (state) => {
            state.user = null
        },
        fetchUsers: (state, action) => {
            state.users = action.payload;
        },
        extraReducers: (builder) => {
            builder.addCase(getUsers.fulfilled, (state, action) => {
                state.users = action.payload
            })
        }
    }

})
export const getUsers = createAsyncThunk(
    'user/getUsers',
    async() => {
        const response = await fetch (
            "https://myduka-group-5-mnnj.onrender.com/users"
        )
        const data =  await response.json()
        return data.data
    } 
)

export const {login, logout, fetchUsers} = userSlice.actions

export const selectUser = (state) => state.user.user 

export default userSlice.reducer;