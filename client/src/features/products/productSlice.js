import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import productService from './productService'

const initialState = {
    products: [],
    product: {},
    updatedProduct: {},
    newProduct: {},
    isLoading: false,
    isSuccess: false,
    newProductSuccess: false,
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

//Get one product
export const getOneProduct = createAsyncThunk(
    'products/getOne',
    async (productItemId, thunkAPI) => {
        try {
            // console.log(
            //     'Get one product function called with id:',
            //     productItemId
            // )
            return await productService.getOneProduct(productItemId)
        } catch (error) {
            const message =
                (error.response &&
                    error.response.data &&
                    error.response.data.message) ||
                error.message ||
                error.toString()

            return thunkAPI.rejectWithValue(message)
        }
    }
)

//Edit one product
export const editOneProduct = createAsyncThunk(
    'products/editOne',
    async ({ productItemId, updateData }, thunkAPI) => {
        try {
            // console.log('Updated product from slice:')
            // console.log(productItemId)
            // console.log(updateData)
            return await productService.editOneProduct(
                productItemId,
                updateData
            )
        } catch (error) {
            const message =
                (error.response &&
                    error.response.data &&
                    error.response.data.message) ||
                error.message ||
                error.toString()

            return thunkAPI.rejectWithValue(message)
        }
    }
)

//Add a product
export const addProduct = createAsyncThunk(
    'products/addOne',
    async (productData, thunkAPI) => {
        try {
            // console.log(productData)
            return await productService.addProduct(productData)
        } catch (error) {
            const message =
                (error.response &&
                    error.response.data &&
                    error.response.data.message) ||
                error.message ||
                error.toString()

            return thunkAPI.rejectWithValue(message)
        }
    }
)

const productSlice = createSlice({
    name: 'products',
    initialState,
    reducers: {
        reset: (state) => initialState,
    },
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
            .addCase(getAllProducts.rejected, (state, action) => {
                state.isLoading = false
                state.isError = true
                state.message = action.payload
            })
            .addCase(getOneProduct.pending, (state) => {
                state.isLoading = true
            })
            .addCase(getOneProduct.fulfilled, (state, action) => {
                state.isLoading = false
                state.isSuccess = true
                state.product = action.payload
            })
            .addCase(getOneProduct.rejected, (state, action) => {
                state.isLoading = false
                state.isError = true
                state.message = action.payload
            })
            .addCase(editOneProduct.pending, (state) => {
                state.isLoading = true
            })
            .addCase(editOneProduct.fulfilled, (state, action) => {
                state.isLoading = false
                state.isSuccess = true
                state.updatedProduct = action.payload
            })
            .addCase(editOneProduct.rejected, (state, action) => {
                state.isLoading = false
                state.isError = true
                state.message = action.payload
            })
            .addCase(addProduct.pending, (state) => {
                state.isLoading = true
            })
            .addCase(addProduct.fulfilled, (state, action) => {
                state.isLoading = false
                state.newProductSuccess = true
                state.newProduct = action.payload
            })
            .addCase(addProduct.rejected, (state, action) => {
                state.isLoading = false
                state.isError = true
                state.message = action.payload
            })
    },
})

export const { reset } = productSlice.actions
export default productSlice.reducer
