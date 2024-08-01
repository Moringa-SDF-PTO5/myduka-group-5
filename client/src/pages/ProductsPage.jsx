import { useEffect, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { getAllProducts } from '../features/products/productSlice'
import {
    addSupplyRequest,
    resetIsReqSuccess,
} from '../features/supplyRequests/supReqSlice'
import { useFormik } from 'formik'
import * as Yup from 'yup'
import ProductItem from '../Components/ProductItem'
import Spinner from '../Components/Spinner'

const ProductsPage = () => {
    const { products, isLoading, isSuccess } = useSelector(
        (state) => state.products
    )
    const { supplyRequest, isReqLoading, isReqSuccess } = useSelector(
        (state) => state.supplyRequests
    )

    const inputRef = useRef(null)
    const dispatch = useDispatch()

    const requestFormSchema = Yup.object().shape({
        product_id: Yup.number().required('*Required'),
        number_requested: Yup.number().required('*Required'),
    })
    const requestFormik = useFormik({
        initialValues: {
            product_id: '',
            number_requested: '',
        },
        validationSchema: requestFormSchema,
        onSubmit: (values, { resetForm }) => {
            dispatch(addSupplyRequest(values))
            resetForm()
        },
    })

    const navigate = useNavigate()

    useEffect(() => {
        dispatch(getAllProducts())
    }, [dispatch])

    function focusInput() {
        inputRef.current.focus()
    }

    if (isLoading || isReqLoading) {
        return <Spinner />
    }

    if (isReqSuccess) {
        setTimeout(() => {
            dispatch(resetIsReqSuccess())
        }, 3000)
    }

    return (
        <>
            <section>
                <div className='flex justify-between'>
                    <h2 className='text-base font-bold'>Products</h2>
                    <div className='flex justify-end gap-x-3'>
                        <button
                            className='btn btn-sm bg-edit-blue text-slate-50'
                            onClick={() => navigate('/addproduct')}
                        >
                            Add Product
                        </button>
                        <button
                            className='btn btn-sm bg-edit-blue text-slate-50'
                            onClick={() => navigate('/payments')}
                        >
                            Manage Payments
                        </button>
                    </div>
                </div>
                <div className='grid grid-cols-5 justify-between items-center gap-x-3 my-2'>
                    <div className='flex justify-center items-center font-bold text-black'>
                        ID
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Name
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        In Stock
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Store Name
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Action
                    </div>
                </div>
                <div>
                    {products.map((product) => (
                        <ProductItem
                            key={product.product_id}
                            productItem={product}
                            focusInput={focusInput}
                        />
                    ))}
                </div>
            </section>
            <section id='supply-request'>
                <h2 className='text-base font-bold'>Supply Request</h2>
                <form
                    onSubmit={requestFormik.handleSubmit}
                    className='flex flex-col w-4/5'
                >
                    <label
                        htmlFor='product_id'
                        className='mt-2'
                    >
                        Product ID
                    </label>
                    <input
                        type='number'
                        id='product_id'
                        name='product_id'
                        value={requestFormik.values.product_id}
                        onChange={requestFormik.handleChange}
                        ref={inputRef}
                        className='w-1/2 bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                    />
                    {requestFormik.errors.product_id &&
                    requestFormik.touched.product_id ? (
                        <p className='text-delete-red'>
                            {requestFormik.errors.product_id}
                        </p>
                    ) : null}
                    <label
                        htmlFor='number_requested'
                        className='mt-2'
                    >
                        Number Requested
                    </label>
                    <input
                        type='number'
                        id='number_requested'
                        name='number_requested'
                        value={requestFormik.values.number_requested}
                        onChange={requestFormik.handleChange}
                        className='w-1/2 bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                    />
                    {requestFormik.errors.number_requested &&
                    requestFormik.touched.number_requested ? (
                        <p className='text-delete-red'>
                            {requestFormik.errors.number_requested}
                        </p>
                    ) : null}
                    <button
                        type='submit'
                        className='btn btn-outline w-min mt-2 border border-solid border-black'
                    >
                        Send Request
                    </button>
                </form>
                {isReqSuccess ? (
                    <div className='flex justify-center items-center'>
                        <p className='text-white bg-edit-blue w-2/5 rounded-sm mt-2'>
                            Request added.
                        </p>
                    </div>
                ) : null}
                <div className='flex justify-center items-center mt-2'>
                    <button
                        type='button'
                        className='btn btn-ghost w-1/2'
                        onClick={() => navigate('/supply_requests')}
                    >
                        View Supply Requests
                    </button>
                </div>
            </section>
        </>
    )
}

export default ProductsPage
