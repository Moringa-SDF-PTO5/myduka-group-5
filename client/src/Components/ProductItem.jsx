function ProductItem({ productItem }) {
    return (
        <div className='grid grid-cols-5 justify-between items-center gap-x-3'>
            <div>{productItem.product_id}</div>
            <div>{productItem.product_name}</div>
            <div>
                {productItem.number_received - productItem.number_dispatched}
            </div>
            <div>{productItem.store.store_name}</div>
        </div>
    )
}

export default ProductItem
