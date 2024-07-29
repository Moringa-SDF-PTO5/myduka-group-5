import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { getAllSupplyRequests } from '../features/supplyRequests/supReqSlice'
import SupReqItem from '../Components/SupReqItem'

function SupplyRequest() {
    const { supplyRequests } = useSelector((state) => state.supplyRequests)
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllSupplyRequests())
    }, [dispatch])

    console.log(supplyRequests)

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
                        />
                    ))}
                </div>
            </section>
        </div>
    )
}

export default SupplyRequest
