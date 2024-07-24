import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { getAllProducts } from '../features/products/productSlice'

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
            {products.map((product) => (
                <p key={product.product_id}>{product.product_name}</p>
            ))}
        </div>
    )
}

export default ProductsPage
