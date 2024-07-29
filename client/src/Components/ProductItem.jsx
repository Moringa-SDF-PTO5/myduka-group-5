import { Link } from 'react-router-dom'
import EditIcon from '@mui/icons-material/Edit'
import AddIcon from '@mui/icons-material/Add'

function ProductItem({ productItem }) {
    return (
        <div className='grid grid-cols-5 justify-between items-center gap-x-3 mb-2'>
            <div>{productItem.product_id}</div>
            <div>{productItem.product_name}</div>
            <div>
                {productItem.number_received - productItem.number_dispatched}
            </div>
            <div>{productItem.store.store_name}</div>
            <div className='flex justify-around'>
                <button className='btn btn-xs bg-edit-blue border-none'>
                    <EditIcon
                        fontSize='small'
                        className='text-slate-50'
                    />
                </button>
                <Link
                    to={'#supply-request'}
                    className='btn btn-xs bg-delete-red border-none'
                >
                    <AddIcon
                        fontSize='small'
                        className='text-slate-50'
                    />
                </Link>
            </div>
        </div>
    )
}

export default ProductItem
