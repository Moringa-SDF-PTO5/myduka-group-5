import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { getAllProducts } from '../features/products/productSlice'
import ProductItem from '../Components/ProductItem'

const ProductsPage = () => {
    const { products, isLoading, isSuccess } = useSelector(
        (state) => state.products
    )
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllProducts())
    }, [dispatch])

    if (isLoading) {
        return <h3 className='text-4xl'>Loading...</h3>
    }
    return (
        <div>
            <div className='grid grid-cols-5 justify-between items-center gap-x-3'>
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
            {products.map((product) => (
                <ProductItem
                    key={product.product_id}
                    productItem={product}
                />
            ))}
        </div>
    )
}

export default ProductsPage
