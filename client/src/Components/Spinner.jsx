import { BallTriangle } from 'react-loading-icons'

function Spinner() {
    return (
        <div className='fixed inset-x-0 inset-y-0 z-30 flex justify-center items-center bg-spinner-bg'>
            <BallTriangle
                fill='rgba(0, 0, 0, 1)'
                strokeWidth={5}
                stroke='2E6C7F'
            />
        </div>
    )
}

export default Spinner
