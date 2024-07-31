import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import {
    getAllSupplyRequests,
    editSupplyRequest,
    resetIsReqSuccess,
} from '../features/supplyRequests/supReqSlice'
import SupReqItem from '../Components/SupReqItem'
import Spinner from '../Components/Spinner'

function SupplyRequest() {
    const { supplyRequests, supplyRequest, isReqLoading } = useSelector(
        (state) => state.supplyRequests
    )
    const dispatch = useDispatch()

    const navigate = useNavigate()

    useEffect(() => {
        dispatch(getAllSupplyRequests())

        return () => {
            dispatch(resetIsReqSuccess())
        }
    }, [dispatch])

    function handleApproval(item) {
        const id = item.id
        const supReqData = {
            id,
            product_id: item.product_id,
            number_requested: item.number_requested,
            is_approved: !item.is_approved,
        }

        dispatch(editSupplyRequest({ id, supReqData }))
        dispatch(getAllSupplyRequests())
    }

    if (isReqLoading) {
        return <Spinner />
    }

    return (
        <div>
            <section>
                <div className='flex justify-between'>
                    <h2 className='text-base font-bold md-2'>
                        Supply Requests
                    </h2>
                    <button
                        className='btn btn-sm bg-black text-slate-50'
                        onClick={() => navigate('/products')}
                    >
                        Back
                    </button>
                </div>
                <div className='grid grid-cols-4 justify-between items-center gap-x-3 mb-2'>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Name
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Number Requested
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Approved
                    </div>
                    <div className='flex justify-center items-center font-bold text-black'>
                        Action
                    </div>
                </div>
                <div>
                    {supplyRequests.map((request) => (
                        <SupReqItem
                            key={request.id}
                            supReqItem={
                                Object.keys(supplyRequest).length &&
                                supplyRequest.id === request.id
                                    ? supplyRequest
                                    : request
                            }
                            handleApproval={handleApproval}
                        />
                    ))}
                </div>
            </section>
        </div>
    )
}

export default SupplyRequest
