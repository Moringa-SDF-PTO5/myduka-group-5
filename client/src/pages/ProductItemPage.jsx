import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import {
    getOneProduct,
    editOneProduct,
    reset,
} from '../features/products/productSlice'
import Spinner from '../Components/Spinner'

function ProductItemPage() {
    const { product, updatedProduct, isLoading, isSuccess } = useSelector(
        (state) => state.products
    )
    const [formData, setFormData] = useState({
        numberDispatched: 0,
        numberReceived: 0,
    })

    const { numberDispatched, numberReceived } = formData
    const { productItemId } = useParams()

    const dispatch = useDispatch()
    const navigate = useNavigate()

    //I've added this to help with displaying the updated changes when they happen
    //instead of refreshing the page or making another request to the db
    //since on update, I'm returning the updated object from the db.
    const displayProduct =
        Object.keys(updatedProduct).length > 0
            ? { ...updatedProduct }
            : { ...product }

    useEffect(() => {
        dispatch(getOneProduct(productItemId))

        return () => {
            dispatch(reset())
        }
    }, [productItemId, dispatch])

    function handleChange(e) {
        setFormData((prevState) => ({
            ...prevState,
            [e.target.id]: e.target.value,
        }))
    }

    function handleSubmit(e) {
        e.preventDefault()

        const updateData = {
            buying_price: product.buying_price,
            is_paid: product.is_paid,
            number_dispatched:
                parseInt(product.number_dispatched) +
                parseInt(numberDispatched),
            number_received:
                parseInt(product.number_received) + parseInt(numberReceived),
            product_name: product.product_name,
            selling_price: product.selling_price,
            store_id: product.store_id,
        }

        dispatch(editOneProduct({ productItemId, updateData }))
        setFormData(() => ({
            numberDispatched: 0,
            numberReceived: 0,
        }))
    }

    if (isLoading) {
        return <Spinner />
    }

    return (
        <>
            <section>
                <div className='flex justify-between'>
                    <h2 className='text-base font-bold md-2'>Edit Product</h2>
                    <button
                        className='btn btn-sm bg-black text-slate-50'
                        onClick={() => navigate('/products')}
                    >
                        Back
                    </button>
                </div>
            </section>
            <section>
                <form onSubmit={handleSubmit}>
                    <div className='grid grid-cols-3 grid-rows-3 gap-3'>
                        <div className='flex flex-col'>
                            <label htmlFor='product_name'>Name</label>
                            <input
                                type='text'
                                id='product_name'
                                name='product_name'
                                value={displayProduct.product_name}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black text-slate-500'
                                disabled
                            />
                        </div>
                        <div className='flex flex-col'>
                            <label htmlFor='product_id'>ID</label>
                            <input
                                type='text'
                                id='product_id'
                                name='product_id'
                                value={displayProduct.product_id}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black text-slate-500'
                                disabled
                            />
                        </div>
                        <div className='flex flex-col'>
                            <label htmlFor='in_stock'>In Stock</label>
                            <input
                                type='text'
                                id='in_stock'
                                name='in_stock'
                                value={(
                                    displayProduct.number_received -
                                    displayProduct.number_dispatched
                                ).toString()}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black text-slate-500'
                                disabled
                            />
                        </div>
                        <div className='flex flex-col'>
                            <label htmlFor='is_paid'>Is Paid</label>
                            <input
                                type='text'
                                id='is_paid'
                                name='is_paid'
                                value={displayProduct.is_paid ? 'Yes' : 'No'}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black text-slate-500'
                                disabled
                            />
                        </div>
                        <div className='flex flex-col'>
                            <label htmlFor='numberDispatched'>
                                To Dispatch
                            </label>
                            <input
                                type='number'
                                id='numberDispatched'
                                name='numberDispatched'
                                value={numberDispatched}
                                onChange={handleChange}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black'
                                disabled={
                                    displayProduct.number_received -
                                        displayProduct.number_dispatched ===
                                    0
                                        ? true
                                        : false
                                }
                            />
                        </div>
                        <div className='flex flex-col'>
                            <label htmlFor='numberReceived'>Received</label>
                            <input
                                type='number'
                                id='numberReceived'
                                name='numberReceived'
                                value={numberReceived}
                                onChange={handleChange}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black'
                            />
                        </div>
                        <div className='flex flex-col'>
                            <label htmlFor='buying_price'>Buying Price</label>
                            <input
                                type='number'
                                step={'any'}
                                id='buying_price'
                                name='buying_price'
                                value={displayProduct.buying_price}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black text-slate-500'
                                disabled
                            />
                        </div>
                        <div className='flex flex-col'>
                            <label htmlFor='selling_price'>Selling Price</label>
                            <input
                                type='number'
                                step={'any'}
                                id='selling_price'
                                name='selling_price'
                                value={displayProduct.selling_price}
                                className='bg-inherit border-2 rounded-sm py-2 px-1 focus:outline-none focus:ring-1 focus:ring-black text-slate-500'
                                disabled
                            />
                        </div>
                    </div>
                    <div className='flex justify-center items-center mt-2'>
                        <button
                            type='submit'
                            className='btn btn-ghost w-1/2 hover:bg-edit-blue hover:text-slate-50'
                        >
                            Edit Product
                        </button>
                    </div>
                </form>
            </section>
        </>
    )
}

export default ProductItemPage
