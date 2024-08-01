/* eslint-disable react/prop-types */

const Card = ({ icon, title, count }) => {
    return (
        <div className='bg-white text-dark p-4 rounded-lg shadow-md flex items-center space-x-6'>
            <div className='text-3x1 text-gray-500'>{icon}</div>
            <div>
                <h2 className='text-lg font-semi-bold'>{title}</h2>
                <p>{count}</p>
            </div>
        </div>
    )
}

export default Card
