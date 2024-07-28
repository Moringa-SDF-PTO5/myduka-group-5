import { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {
    editSupplyRequest,
    resetIsReqSuccess,
} from '../features/supplyRequests/supReqSlice'

function SupReqItem({ supReqItem, handleApproval }) {
    const { supplyRequest, isReqSuccess, isReqError, reqMessage } = useSelector(
        (state) => state.supplyRequests
    )
    // console.log(supplyRequest)

    const dispatch = useDispatch()

    // function handleApproval(item) {
    //     const id = item.id
    //     const supReqData = {
    //         id,
    //         product_id: item.product_id,
    //         number_requested: item.number_requested,
    //         is_approved: !item.is_approved,
    //     }
    //     // console.log(itemId, itemCopy)
    //     dispatch(editSupplyRequest({ id, supReqData }))
    //     // console.log(supplyRequest)
    // }
    return (
        <div className='grid grid-cols-4 justify-between items-center gap-x-3 mb-2'>
            <div>{supReqItem.product.product_name}</div>
            <div>{supReqItem.number_requested}</div>
            <div>{supReqItem.is_approved ? 'True' : 'False'}</div>
            <div className='flex justify-center'>
                <button
                    className='btn btn-sm w-min bg-edit-blue border-none text-slate-50'
                    onClick={() => handleApproval(supReqItem)}
                >
                    Approve
                </button>
            </div>
        </div>
    )
}

export default SupReqItem
