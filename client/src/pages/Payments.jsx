import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import {
    getAllProducts,
    editOneProduct,
} from '../features/products/productSlice'
import PaymentItem from '../Components/PaymentItem'
import Spinner from '../Components/Spinner'

function Payments() {
    const { products, isLoading } = useSelector((state) => state.products)
    const [editedProduct, setEditedProduct] = useState({})
    const dispatch = useDispatch()
    const navigate = useNavigate()

    useEffect(() => {
        dispatch(getAllProducts())
    }, [dispatch])

    function handlePayment(item) {
        const productItemId = item.product_id
        const updateData = {
            buying_price: item.buying_price,
            is_paid: !item.is_paid,
            number_dispatched: item.number_dispatched,
            number_received: item.number_received,
            product_name: item.product_name,
            selling_price: item.selling_price,
            store_id: item.store_id,
        }

        dispatch(editOneProduct({ productItemId, updateData }))
        setEditedProduct(() => ({
            ...updateData,
            product_id: item.product_id,
        }))
    }

    if (isLoading) {
        return <Spinner />
    }

    return (
        <div>
            <section>
                <div className='flex justify-between'>
                    <h2 className='text-base font-bold md-2'>
                        Manage Payments
                    </h2>
                    <button
                        className='btn btn-sm bg-black text-slate-50'
                        onClick={() => navigate('/products')}
                    >
                        Back
                    </button>
                </div>
            </section>
            <section>
                <div className='grid grid-cols-3 justify-between items-center gap-x-3 my-2'>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Name
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Status
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Action
                    </div>
                </div>
                <div>
                    {products.map((productItem) => (
                        <PaymentItem
                            key={productItem.product_id}
                            productItem={
                                Object.keys(editedProduct).length > 0 &&
                                editedProduct.product_id ===
                                    productItem.product_id
                                    ? editedProduct
                                    : productItem
                            }
                            handlePayment={handlePayment}
                        />
                    ))}
                </div>
            </section>
        </div>
    )
}

export default Payments
