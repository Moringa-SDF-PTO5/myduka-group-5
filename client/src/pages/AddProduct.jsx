import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { getAllStores } from '../features/stores/storeSlice'
import { addProduct, reset } from '../features/products/productSlice'
import { useFormik } from 'formik'
import * as Yup from 'yup'
import Spinner from '../Components/Spinner'

function AddProduct() {
    const { stores } = useSelector((state) => state.stores)
    const { newProduct, newProductSuccess, isLoading } = useSelector(
        (state) => state.products
    )
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const formSchema = Yup.object().shape({
        product_name: Yup.string().required('Required'),
        store_id: Yup.number().required('Required'),
        number_received: Yup.number(),
        number_dispatched: Yup.number().max(
            50,
            'Cannot dispatch more than 50 pieces.'
        ),
        buying_price: Yup.number().required('Required'),
        selling_price: Yup.number().required('Required'),
    })

    const formik = useFormik({
        initialValues: {
            product_name: '',
            store_id: '1',
            number_received: 0,
            number_dispatched: 0,
            buying_price: '',
            selling_price: '',
        },
        validationSchema: formSchema,
        onSubmit: (values, { resetForm }) => {
            dispatch(addProduct(values))
            resetForm()
        },
    })

    useEffect(() => {
        dispatch(getAllStores())

        return () => {
            dispatch(reset())
        }
    }, [dispatch])

    if (newProductSuccess) {
        setTimeout(() => {
            dispatch(reset())
        }, 3000)
    }

    if (isLoading) {
        return <Spinner />
    }

    return (
        <>
            <section>
                <div className='flex justify-between'>
                    <h2 className='text-base font-bold'>Add Product</h2>
                    <button
                        className='btn btn-sm bg-black text-slate-50'
                        onClick={() => navigate('/products')}
                    >
                        Back
                    </button>
                </div>
            </section>
            <section>
                <form
                    onSubmit={formik.handleSubmit}
                    className='grid grid-cols-2 grid-rows-4 gap-3'
                >
                    <div className='flex flex-col'>
                        <label htmlFor='product_name'>Name</label>
                        <input
                            type='text'
                            id='product_name'
                            name='product_name'
                            value={formik.values.product_name}
                            onChange={formik.handleChange}
                            className='bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                        />
                        {formik.errors.product_name &&
                        formik.touched.product_name ? (
                            <p className='text-delete-red'>
                                {formik.errors.product_name}
                            </p>
                        ) : null}
                    </div>
                    <div className='flex flex-col'>
                        <label htmlFor='store_id'>Store Id</label>
                        <select
                            id='store_id'
                            name='store_id'
                            value={formik.values.store_id}
                            onChange={formik.handleChange}
                            className='bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                        >
                            {stores.map((store) => (
                                <option
                                    key={store.store_id}
                                    value={store.store_id}
                                >
                                    {store.store_id}
                                </option>
                            ))}
                        </select>
                    </div>
                    <div className='flex flex-col'>
                        <label htmlFor='number_received'>Number Received</label>
                        <input
                            type='number'
                            id='number_received'
                            name='number_received'
                            value={formik.values.number_received}
                            onChange={formik.handleChange}
                            className='bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                        />
                    </div>
                    <div className='flex flex-col'>
                        <label htmlFor='number_dispatched'>
                            Number Dispatched
                        </label>
                        <input
                            type='number'
                            id='number_dispatched'
                            name='number_dispatched'
                            value={formik.values.number_dispatched}
                            onChange={formik.handleChange}
                            className='bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                        />
                    </div>
                    <div className='flex flex-col'>
                        <label htmlFor='buying_price'>Buying Price</label>
                        <input
                            type='number'
                            step={'any'}
                            id='buying_price'
                            name='buying_price'
                            value={formik.values.buying_price}
                            onChange={formik.handleChange}
                            className='bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                        />
                        {formik.errors.buying_price &&
                        formik.touched.buying_price ? (
                            <p className='text-delete-red'>
                                {formik.errors.buying_price}
                            </p>
                        ) : null}
                    </div>
                    <div className='flex flex-col'>
                        <label htmlFor='selling_price'>Selling Price</label>
                        <input
                            type='number'
                            step={'any'}
                            id='selling_price'
                            name='selling_price'
                            value={formik.values.selling_price}
                            onChange={formik.handleChange}
                            className='bg-inherit border-2 rounded-sm py-2 focus:outline-none focus:ring-1 focus:ring-black'
                        />
                        {formik.errors.selling_price &&
                        formik.touched.selling_price ? (
                            <p className='text-delete-red'>
                                {formik.errors.selling_price}
                            </p>
                        ) : null}
                    </div>
                    <div className='col-span-2 flex justify-center items-center'>
                        <button
                            type='submit'
                            className='btn btn-sm border-none bg-edit-blue text-slate-50'
                        >
                            Add Product
                        </button>
                    </div>
                </form>
                {newProductSuccess ? (
                    <div className='flex justify-center items-center'>
                        <p className='text-white bg-edit-blue w-2/5 rounded-sm mt-2'>
                            Product added successfully.
                        </p>
                    </div>
                ) : null}
            </section>
        </>
    )
}

export default AddProduct
