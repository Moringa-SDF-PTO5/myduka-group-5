import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {
    getAllSupplyRequests,
    editSupplyRequest,
} from '../features/supplyRequests/supReqSlice'
import SupReqItem from '../Components/SupReqItem'

function SupplyRequest() {
    const { supplyRequests } = useSelector((state) => state.supplyRequests)
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllSupplyRequests())
    }, [dispatch])

    // console.log(supplyRequests)

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

    return (
        <div>
            <section>
                <h2 className='text-base font-bold md-2'>Supply Requests</h2>
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
                            supReqItem={request}
                            handleApproval={handleApproval}
                        />
                    ))}
                </div>
            </section>
        </div>
    )
}

export default SupplyRequest
