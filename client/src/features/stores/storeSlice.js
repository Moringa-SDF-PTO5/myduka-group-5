import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import storeService from './storeService'

const initialState = {
    stores: [],
}

//Get all stores
export const getAllStores = createAsyncThunk('stores/getAll', async () => {
    return await storeService.getAllStores()
})

const storeSlice = createSlice({
    name: 'stores',
    initialState,
    extraReducers: (builder) => {
        builder.addCase(getAllStores.fulfilled, (state, action) => {
            state.stores = action.payload
        })
    },
})

export default storeSlice.reducer
