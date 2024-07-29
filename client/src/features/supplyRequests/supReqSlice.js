import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import supReqService from './supReqService'

const initialState = {
    supplyRequests: [],
    supplyRequest: {},
    isReqLoading: false,
    isReqSuccess: false,
    isReqError: false,
    reqMessage: '',
}

//Add a supply request to the db
export const addSupplyRequest = createAsyncThunk(
    'supplyRequests/addOne',
    async (supReqData, thunkAPI) => {
        try {
            return await supReqService.addSupplyRequest(supReqData)
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

//Get all supply requests
export const getAllSupplyRequests = createAsyncThunk(
    'supplyRequests/getAll',
    async (_, thunkAPI) => {
        try {
            return await supReqService.getAllSupplyRequests()
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

const supReqSlice = createSlice({
    name: 'supplyRequests',
    initialState,
    reducers: {
        resetIsReqSuccess: () => {
            const resetSuccess = false

            return {
                ...initialState,
                isReqSuccess: resetSuccess,
            }
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(addSupplyRequest.pending, (state) => {
                state.isReqLoading = true
            })
            .addCase(addSupplyRequest.fulfilled, (state, action) => {
                state.isReqLoading = false
                state.isReqSuccess = true
                state.supplyRequest = action.payload
            })
            .addCase(addSupplyRequest.rejected, (state, action) => {
                state.isReqLoading = false
                state.isReqError = true
                state.reqMessage = action.payload
            })
            .addCase(getAllSupplyRequests.pending, (state) => {
                state.isReqLoading = true
            })
            .addCase(getAllSupplyRequests.fulfilled, (state, action) => {
                state.isReqLoading = false
                state.isReqSuccess = true
                state.supplyRequests = action.payload
            })
            .addCase(getAllSupplyRequests.rejected, (state, action) => {
                state.isReqLoading = false
                state.isReqError = true
                state.reqMessage = action.payload
            })
    },
})

export const { resetIsReqSuccess } = supReqSlice.actions
export default supReqSlice.reducer
