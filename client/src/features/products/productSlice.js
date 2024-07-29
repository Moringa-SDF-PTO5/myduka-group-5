import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import productService from './productService'

const initialState = {
    products: [],
    isLoading: false,
    isSuccess: false,
    isError: false,
    message: '',
}

//Get all products
export const getAllProducts = createAsyncThunk('products/getAll', async () => {
    try {
        return await productService.getAllProducts()
    } catch (error) {
        console.log(error)
    }
})

const productSlice = createSlice({
    name: 'products',
    initialState,
    extraReducers: (builder) => {
        builder
            .addCase(getAllProducts.pending, (state) => {
                state.isLoading = true
            })
            .addCase(getAllProducts.fulfilled, (state, action) => {
                state.isLoading = false
                state.isSuccess = true
                state.products = action.payload
            })
    },
})

export default productSlice.reducer
