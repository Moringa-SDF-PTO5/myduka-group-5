function PaymentItem({ productItem, handlePayment }) {
    return (
        <div className='grid grid-cols-3 justify-between items-center gap-x-3 my-2'>
            <div>{productItem.product_name}</div>
            <div className='flex justify-center items-center'>
                {productItem.is_paid ? (
                    <button
                        type='button'
                        className='btn btn-xs btn-active bg-edit-blue text-slate-50 border-none pointer-events-none'
                    >
                        Paid
                    </button>
                ) : (
                    <button
                        type='button'
                        className='btn btn-xs bg-delete-red text-slate-50 border-none pointer-events-none'
                    >
                        Not Paid
                    </button>
                )}
            </div>
            <div className='flex justify-center items-center'>
                {productItem.is_paid ? (
                    <button
                        type='button'
                        className='btn btn-sm bg-slate-700 text-slate-50 border-none pointer-events-none'
                    >
                        Pay
                    </button>
                ) : (
                    <button
                        type='button'
                        className='btn btn-sm bg-edit-blue text-slate-50 border-none'
                        onClick={() => handlePayment(productItem)}
                    >
                        Pay
                    </button>
                )}
            </div>
        </div>
    )
}

export default PaymentItem
