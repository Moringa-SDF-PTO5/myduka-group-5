import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import storeService from './storeService'

const initialState = {
    stores: [],
    storesCount: 0,
    isStoresLoading: false,
}

//Get all stores
export const getAllStores = createAsyncThunk('stores/getAll', async () => {
    return await storeService.getAllStores()
})

//Get the count of stores
export const getStoresCount = createAsyncThunk('stores/count', async () => {
    return await storeService.getStoresCount()
})

const storeSlice = createSlice({
    name: 'stores',
    initialState,
    extraReducers: (builder) => {
        builder
            .addCase(getAllStores.fulfilled, (state, action) => {
                state.stores = action.payload
            })
            .addCase(getStoresCount.pending, (state) => {
                state.isLoading = true
            })
            .addCase(getStoresCount.fulfilled, (state, action) => {
                state.isLoading = false
                state.storesCount = action.payload
            })
    },
})

export default storeSlice.reducer
