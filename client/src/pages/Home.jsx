import { useNavigate } from 'react-router-dom'

function Home() {
    const navigate = useNavigate()

    return (
        <div className='min-h-full flex flex-col justify-center items-center gap-y-5'>
            <h1 className='text-center text-5xl text-black'>
                MyDuka Inventory Management
            </h1>
            <button
                type='button'
                className='btn btn-outline border-black text-black'
                onClick={() => navigate('/login')}
            >
                Go To Login
            </button>
        </div>
    )
}

export default Home
