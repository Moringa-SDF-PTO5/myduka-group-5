import { configureStore } from '@reduxjs/toolkit'
import userReducer from '../features/userSlice'
import productReducer from '../features/products/productSlice'

export const store = configureStore({
    reducer: {
        user: userReducer,
        products: productReducer,
    },
})
