function SupReqItem({ supReqItem }) {
    return (
        <div className='grid grid-cols-4 justify-between items-center gap-x-3 mb-2'>
            <div>{supReqItem.product.product_name}</div>
            <div>{supReqItem.number_requested}</div>
            <div>{supReqItem.is_approved ? 'True' : 'False'}</div>
            <div className='flex justify-center'>
                <button className='btn btn-sm w-min bg-edit-blue border-none text-slate-50'>
                    Approve
                </button>
            </div>
        </div>
    )
}

export default SupReqItem
