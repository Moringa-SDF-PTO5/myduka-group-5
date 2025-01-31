import { Link, useNavigate } from 'react-router-dom'
import EditIcon from '@mui/icons-material/Edit'
import AddIcon from '@mui/icons-material/Add'

function ProductItem({ productItem, focusInput }) {
    const inStock = productItem.number_received - productItem.number_dispatched
    const navigate = useNavigate()

    function viewProduct(productItemId) {
        navigate(`/products/${productItemId}`)
    }

    return (
        <div className='grid grid-cols-5 justify-between items-center gap-x-3 mb-2'>
            <div>{productItem.product_id}</div>
            <div>{productItem.product_name}</div>
            <div>
                {inStock <= 10 ? (
                    <p className='text-delete-red font-bold'>{inStock}</p>
                ) : (
                    <p>{inStock}</p>
                )}
            </div>
            <div>{productItem.store.store_name}</div>
            <div className='flex justify-around'>
                <button
                    className='btn btn-xs bg-edit-blue border-none'
                    onClick={() => viewProduct(productItem.product_id)}
                >
                    <EditIcon
                        fontSize='small'
                        className='text-slate-50'
                    />
                </button>
                <button
                    className='btn btn-xs bg-delete-red border-none'
                    onClick={focusInput}
                >
                    <AddIcon
                        fontSize='small'
                        className='text-slate-50'
                    />
                </button>
            </div>
        </div>
    )
}

export default ProductItem
